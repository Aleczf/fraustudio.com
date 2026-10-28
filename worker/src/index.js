// Endpoint del modulo di contatto di fraustudio.com.
// Riceve il form (JSON o form-urlencoded), lo valida, filtra lo spam e lo inoltra via email con Resend.
//
// Variabili (wrangler.toml / segreti):
//   RESEND_API_KEY   segreto: `npx wrangler secret put RESEND_API_KEY`
//   MAIL_TO          dove arrivano le richieste
//   MAIL_FROM        mittente; "onboarding@resend.dev" funziona senza DNS ma consegna solo
//                    all'indirizzo con cui è registrato l'account Resend
//   ALLOWED_ORIGINS  origini ammesse, separate da virgola
//   SITE_URL         pagina a cui tornare quando il form arriva senza JavaScript
// Binding facoltativo: CONTACT_LIMITER (rate limit per IP).

const LIMITS = { problema: [10, 5000], strumenti: [0, 500], nome: [2, 200], email: [5, 200] };
const MIN_FILL_MS = 3000; // un umano non compila il modulo in meno di 3 secondi
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";
    const allowed = (env.ALLOWED_ORIGINS || "https://fraustudio.com").split(",").map((s) => s.trim());
    const cors = allowed.includes(origin)
      ? { "Access-Control-Allow-Origin": origin, "Access-Control-Allow-Methods": "POST, OPTIONS", "Access-Control-Allow-Headers": "Content-Type", "Access-Control-Max-Age": "86400", Vary: "Origin" }
      : {};

    if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: cors });
    if (request.method !== "POST") return json({ ok: false, error: "method" }, 405, cors);
    if (origin && !allowed.includes(origin)) return json({ ok: false, error: "origin" }, 403, cors);

    const isForm = (request.headers.get("Content-Type") || "").includes("application/x-www-form-urlencoded");

    if (env.CONTACT_LIMITER) {
      const ip = request.headers.get("CF-Connecting-IP") || "unknown";
      const { success } = await env.CONTACT_LIMITER.limit({ key: ip });
      if (!success) return json({ ok: false, error: "rate" }, 429, cors);
    }

    let data;
    try {
      data = await readBody(request, isForm);
    } catch {
      return json({ ok: false, error: "body" }, 400, cors);
    }

    // Trappole anti-bot: rispondiamo "ok" senza inviare nulla, così il bot non impara niente.
    const elapsed = Number(data.t);
    if (data.sito || (Number.isFinite(elapsed) && elapsed < MIN_FILL_MS)) {
      return done(isForm, env, cors);
    }

    const fields = {};
    for (const [key, [min, max]] of Object.entries(LIMITS)) {
      const value = String(data[key] ?? "").trim();
      if (value.length < min || value.length > max) return json({ ok: false, error: "field", field: key }, 422, cors);
      fields[key] = value;
    }
    if (!EMAIL_RE.test(fields.email)) return json({ ok: false, error: "field", field: "email" }, 422, cors);

    const sent = await sendMail(env, fields);
    if (!sent) return json({ ok: false, error: "send" }, 502, cors);
    return done(isForm, env, cors);
  },
};

async function readBody(request, isForm) {
  if (isForm) return Object.fromEntries(new URLSearchParams(await request.text()));
  return await request.json();
}

function done(isForm, env, cors) {
  if (isForm) {
    // Invio senza JavaScript: si torna al sito.
    return Response.redirect(`${env.SITE_URL || "https://fraustudio.com"}/?inviato=1#contatto`, 303);
  }
  return json({ ok: true }, 200, cors);
}

async function sendMail(env, f) {
  const text = [
    `Nome e azienda: ${f.nome}`,
    `Email: ${f.email}`,
    `Strumenti: ${f.strumenti || "—"}`,
    "",
    "Cosa succede oggi:",
    f.problema,
  ].join("\n");

  const res = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      from: env.MAIL_FROM || "Frau Studio <onboarding@resend.dev>",
      to: [env.MAIL_TO],
      reply_to: f.email,
      subject: `Nuova richiesta dal sito: ${f.nome}`.slice(0, 150),
      text,
    }),
  });
  if (!res.ok) console.error("Resend", res.status, await res.text());
  return res.ok;
}

function json(body, status, headers) {
  return new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json", ...headers } });
}
