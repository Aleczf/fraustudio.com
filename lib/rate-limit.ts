// Rate limit in-memory, senza dipendenze esterne.
//
// LIMITE NOTO — è "best effort", non una garanzia: su Vercel (serverless) ogni
// istanza/regione ha la sua memoria, quindi questa Map NON è condivisa tra
// invocazioni servite da lambda diverse. Un utente determinato potrebbe quindi
// superare la soglia colpendo istanze differenti. Per un tool pubblico e a
// basso rischio come il Diagnoser è un compromesso accettabile: alza il costo
// dell'abuso banale senza introdurre infrastruttura (Redis, KV) sproporzionata.

const WINDOW_MS = 10 * 60 * 1000; // 10 minuti
const MAX_REQUESTS = 5; // per IP, per finestra

// IP -> timestamp (ms) delle richieste recenti.
const hits = new Map<string, number[]>();

export interface RateLimitResult {
  allowed: boolean;
  /** Secondi da attendere prima di riprovare (solo quando allowed === false). */
  retryAfterSeconds: number;
}

/**
 * Registra un tentativo per l'IP dato e dice se è consentito.
 * Chiamare una sola volta per richiesta: la chiamata conta come tentativo.
 */
export function rateLimit(ip: string): RateLimitResult {
  const now = Date.now();
  const windowStart = now - WINDOW_MS;

  // Tieni solo i timestamp ancora dentro la finestra.
  const recent = (hits.get(ip) ?? []).filter((t) => t > windowStart);

  if (recent.length >= MAX_REQUESTS) {
    hits.set(ip, recent);
    const oldest = recent[0];
    const retryAfterSeconds = Math.max(
      1,
      Math.ceil((oldest + WINDOW_MS - now) / 1000)
    );
    return { allowed: false, retryAfterSeconds };
  }

  recent.push(now);
  hits.set(ip, recent);

  // Pulizia opportunistica: evita che la Map cresca senza limite quando molti
  // IP diversi colpiscono una singola istanza long-lived.
  if (hits.size > 5000) {
    for (const [key, times] of hits) {
      const stillRecent = times.filter((t) => t > windowStart);
      if (stillRecent.length === 0) {
        hits.delete(key);
      } else {
        hits.set(key, stillRecent);
      }
    }
  }

  return { allowed: true, retryAfterSeconds: 0 };
}
