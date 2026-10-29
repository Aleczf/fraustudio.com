// Test del Worker senza rete: simula Resend e il rate limit.
import assert from "node:assert/strict";
import worker from "./src/index.js";

const sentMails = [];
globalThis.fetch = async (url, init) => {
  sentMails.push({ url, body: JSON.parse(init.body) });
  return new Response("{}", { status: 200 });
};

const env = { RESEND_API_KEY: "test", MAIL_TO: "a@b.it", ALLOWED_ORIGINS: "https://fraustudio.com", SITE_URL: "https://fraustudio.com" };
const ok = { problema: "Ricopiamo a mano gli ordini nel gestionale ogni settimana.", strumenti: "Excel", nome: "Mario, Rossi Srl", email: "mario@rossi.it", sito: "", t: "15000" };
const post = (body, headers = {}) =>
  new Request("https://w.dev/", { method: "POST", headers: { Origin: "https://fraustudio.com", "Content-Type": "application/json", ...headers }, body: typeof body === "string" ? body : JSON.stringify(body) });

let r = await worker.fetch(new Request("https://w.dev/", { method: "OPTIONS", headers: { Origin: "https://fraustudio.com" } }), env);
assert.equal(r.status, 204);
assert.equal(r.headers.get("Access-Control-Allow-Origin"), "https://fraustudio.com");

r = await worker.fetch(post(ok), env);
assert.equal(r.status, 200);
assert.equal(sentMails.length, 1);
assert.equal(sentMails[0].body.reply_to, "mario@rossi.it");
assert.match(sentMails[0].body.text, /Ricopiamo a mano/);

r = await worker.fetch(post({ ...ok, sito: "spam.com" }), env);
assert.equal(r.status, 200, "honeypot: risposta ok");
r = await worker.fetch(post({ ...ok, t: "800" }), env);
assert.equal(r.status, 200, "troppo veloce: risposta ok");
assert.equal(sentMails.length, 1, "nessuna email per i bot");

r = await worker.fetch(post({ ...ok, email: "non-una-mail" }), env);
assert.equal(r.status, 422);
r = await worker.fetch(post({ ...ok, problema: "corto" }), env);
assert.equal(r.status, 422);
r = await worker.fetch(post("{rotto"), env);
assert.equal(r.status, 400);
r = await worker.fetch(post(ok, { Origin: "https://altro.it" }), env);
assert.equal(r.status, 403);

r = await worker.fetch(post(new URLSearchParams(ok).toString(), { "Content-Type": "application/x-www-form-urlencoded" }), env);
assert.equal(r.status, 303, "senza JS: redirect al sito");

r = await worker.fetch(post(ok), { ...env, CONTACT_LIMITER: { limit: async () => ({ success: false }) } });
assert.equal(r.status, 429);

globalThis.fetch = async () => new Response("errore", { status: 500 });
r = await worker.fetch(post(ok), env);
assert.equal(r.status, 502);

console.log("Tutti i test passati");
