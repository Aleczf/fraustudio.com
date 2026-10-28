import Anthropic from "@anthropic-ai/sdk";
import { NextResponse } from "next/server";
import { getSystemPrompt, parseDiagnosis } from "@/lib/diagnoser-prompt";
import { rateLimit } from "@/lib/rate-limit";
import {
  MAX_INPUT_CHARS,
  type DiagnoseErrorResponse,
  type DiagnoseRequestBody,
  type DiagnoseResult,
} from "@/lib/diagnoser-types";

// Route dinamica: legge headers/body a runtime, non pre-renderizzabile.
export const runtime = "nodejs";
export const dynamic = "force-dynamic";

// Modello: Sonnet 4.5 — veloce ed economico, adatto a un tool pubblico che
// deve rispondere in fretta e a basso costo per richiesta. Uso l'alias
// "claude-sonnet-4-5" (l'SDK risolve alla snapshot corrente); volendo pinnare
// una versione deterministica si può passare a "claude-sonnet-4-5-20250929".
const MODEL = "claude-sonnet-4-5";
const MAX_TOKENS = 700;
const TIMEOUT_MS = 15_000;

// Errore gestito riutilizzabile: la UI mostra sempre lo stesso fallback
// cortese, senza mai vedere dettagli tecnici.
function errorResponse(status: number): NextResponse<DiagnoseErrorResponse> {
  const body: DiagnoseErrorResponse = { error: true };
  return NextResponse.json(body, { status });
}

function getClientIp(request: Request): string {
  const forwarded = request.headers.get("x-forwarded-for");
  if (forwarded) {
    // x-forwarded-for può essere "client, proxy1, proxy2": il primo è il client.
    return forwarded.split(",")[0].trim();
  }
  return request.headers.get("x-real-ip")?.trim() || "unknown";
}

export async function POST(
  request: Request
): Promise<NextResponse<DiagnoseResult | DiagnoseErrorResponse>> {
  // 1) Rate limit best-effort per IP (vedi nota in lib/rate-limit.ts).
  const ip = getClientIp(request);
  const limit = rateLimit(ip);
  if (!limit.allowed) {
    const res = errorResponse(429);
    res.headers.set("Retry-After", String(limit.retryAfterSeconds));
    return res;
  }

  // 2) Parsing e validazione del body.
  let body: unknown;
  try {
    body = await request.json();
  } catch {
    return errorResponse(400);
  }

  if (typeof body !== "object" || body === null) {
    return errorResponse(400);
  }

  const { processo, lingua } = body as Partial<DiagnoseRequestBody>;

  if (typeof processo !== "string") {
    return errorResponse(400);
  }

  const trimmed = processo.trim();
  if (trimmed.length === 0 || trimmed.length > MAX_INPUT_CHARS) {
    return errorResponse(400);
  }

  // Tranche 4: il Diagnoser risponde nella lingua della pagina.
  const locale: "it" | "en" = lingua === "en" ? "en" : "it";

  // 3) Chiave API: se manca, errore gestito (la UI mostra il fallback).
  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) {
    return errorResponse(503);
  }

  // 4) Chiamata al modello, con timeout via AbortController.
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), TIMEOUT_MS);

  try {
    const client = new Anthropic({ apiKey });

    const message = await client.messages.create(
      {
        model: MODEL,
        max_tokens: MAX_TOKENS,
        system: getSystemPrompt(locale),
        messages: [{ role: "user", content: trimmed }],
      },
      { signal: controller.signal }
    );

    // `content` è una discriminated union sui blocchi: prendiamo solo il testo.
    const raw = message.content
      .map((block) => (block.type === "text" ? block.text : ""))
      .join("\n")
      .trim();

    if (!raw) {
      return errorResponse(502);
    }

    const result = parseDiagnosis(raw);
    return NextResponse.json(result, { status: 200 });
  } catch {
    // Qualsiasi fallimento (rete, timeout/abort, errore SDK) → fallback gestito.
    // Non logghiamo dettagli sensibili né li restituiamo al client.
    return errorResponse(503);
  } finally {
    clearTimeout(timeout);
  }
}
