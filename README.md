# Alessandro Frau — Portfolio

Sito portfolio personale. Next.js (App Router) + TypeScript + Tailwind CSS v4.
Fonti di verità: [`DESIGN.md`](./DESIGN.md) (sistema visivo) e [`CONTENT.md`](./CONTENT.md) (testi). Non deviare da questi file senza motivo esplicito.

## Setup

```bash
npm install
cp .env.example .env.local   # poi compila ANTHROPIC_API_KEY (vedi sotto)
npm run dev
```

Apri http://localhost:3000.

## Diagnoser e `ANTHROPIC_API_KEY`

Il Diagnoser (sezione interattiva sotto l'hero) chiama l'API Anthropic **solo lato server**, dalla route `app/api/diagnose/route.ts`. La chiave non raggiunge mai il browser: niente `NEXT_PUBLIC_`, nessuna chiave passata a componenti client.

**In locale:** metti la chiave in `.env.local` (mai committato):

```bash
# .env.local
ANTHROPIC_API_KEY=sk-ant-...
```

Ottieni la chiave da https://console.anthropic.com/.

**Su Vercel:** Project → Settings → Environment Variables → aggiungi `ANTHROPIC_API_KEY` (Production, e Preview se vuoi testare i deploy di anteprima). Dopo averla aggiunta, fai un redeploy perché venga letta.

**Senza chiave il sito resta presentabile:** se `ANTHROPIC_API_KEY` manca o la chiamata fallisce (rete, timeout, rate limit), la route risponde con un errore gestito e il Diagnoser mostra un messaggio cortese di fallback ("Il Diagnoser sta riposando — scrivimi direttamente"). Nessuno stack trace, nessun dettaglio tecnico lato utente.

Protezioni del tool pubblico: input max 800 caratteri (client + server), rate limit best-effort in memoria (5 richieste / 10 minuti per IP), `max_tokens` contenuto e timeout di 15s.

## Comandi

| Comando | Cosa fa |
|---|---|
| `npm run dev` | Server di sviluppo |
| `npm run build` | Build di produzione (SSG) |
| `npm run start` | Avvia la build di produzione |
| `npm run lint` | ESLint |
| `npm run typecheck` | Controllo TypeScript senza emettere output |

## Struttura

```
app/(it)/       albero italiano (default): "/" e "/lavori/[slug]", con il proprio
                root layout (<html lang="it">)
app/en/         albero inglese: "/en" e "/en/lavori/[slug]", proprio root layout
                (<html lang="en">) — stessi componenti dell'italiano, prop locale="en"
app/api/        route API (/api/diagnose)
app/sitemap.ts  sitemap.xml generata (entrambe le lingue, con hreflang)
app/robots.ts   robots.txt
components/     un file per componente, condivisi tra IT e EN via prop `locale`
content/        testi tipizzati { it, en } — CONTENT.md è la fonte per l'IT,
                l'EN è una traduzione curata con lo stesso registro
lib/            utility (rate limiting, system prompt del Diagnoser, immagine OG)
public/         asset statici
DESIGN.md       design system — fonte di verità visiva
CONTENT.md      contenuti — fonte di verità testuale (italiano)
```

### Perché due root layout (`app/(it)/layout.tsx` e `app/en/layout.tsx`)

Next.js permette un solo `<html>` per root layout. Per avere `<html lang="it">` e `<html lang="en">` corretti (accessibilità + SEO) senza un unico layout condiviso, si usa il pattern ufficiale "multiple root layouts": niente `app/layout.tsx` in cima, un route group `app/(it)/` (le parentesi non contano nell'URL) e una cartella reale `app/en/`, ciascuna con il proprio layout. I componenti di sezione (Hero, Method, Works, ecc.) sono condivisi e ricevono `locale="it"|"en"` come prop — nessun testo duplicato, solo `content/it.ts` / `content/en.ts`.

Limite noto di questo pattern: un URL completamente estraneo a entrambi gli alberi (che non esiste comunque, dato che tutte le pagine reali sono coperte) non avrebbe un layout root a cui appoggiarsi. Non è un problema nella pratica, ma se in futuro si aggiungono route dinamiche generiche vale la pena ricontrollarlo.

## Deploy su Vercel

1. Push del repo su GitHub (o import diretto della cartella in Vercel).
2. Su vercel.com → New Project → importa il repo.
3. Framework preset: Next.js (rilevato automaticamente).
4. Environment Variables → aggiungi `ANTHROPIC_API_KEY` (necessaria solo per il Diagnoser; senza, il sito resta comunque presentabile con il fallback gestito). Vedi la sezione "Diagnoser e `ANTHROPIC_API_KEY`" qui sopra.
5. Deploy. Dominio personalizzato: Project → Settings → Domains.

## Verifica dopo `npm run build` (i18n/SEO — Tranche 4)

Non essendo stato possibile eseguire la build durante la scrittura (vedi nota sotto), controlla in locale:

- `/` e `/en` caricano entrambe, con `<html lang="it">` / `<html lang="en">` corretti (ispeziona l'elemento).
- Lo switch lingua nell'header porta dalla home IT a `/en` e viceversa, e da una pagina caso IT alla sua gemella EN (es. `/lavori/vas-3` ↔ `/en/lavori/vas-3`), conservando la posizione di scroll.
- `view-source:` su `/` e `/en` mostra tutto il testo nell'HTML (nessun contenuto solo client-side).
- `/sitemap.xml` e `/robots.txt` rispondono ed elencano home + le 4 pagine caso in entrambe le lingue.
- `/opengraph-image` (dentro `/` e dentro `/en`) genera un'immagine 1200×630 leggibile; verificala anche con un validator OG (es. Facebook Sharing Debugger o metatags.io) una volta online.
- Lighthouse (Chrome DevTools) su home e una pagina caso, in entrambe le lingue: target Performance/A11y/SEO ≥95 da DESIGN.md. Se qualcosa è sotto soglia, è materiale per la Tranche 5 (QA finale).

## Nota sull'origine di questo progetto

Il progetto è stato costruito a mano, sezione per sezione, seguendo il piano di orchestrazione in `portfolio_orchestrazione.md` (tranche 0→5). Il codice è stato scritto in un ambiente sandbox senza accesso di rete, quindi **non è stato possibile eseguire `npm install` / `npm run build` / Lighthouse in fase di scrittura**: la prima cosa da fare in locale è lanciare `npm install && npm run build` e segnalare eventuali errori, così vengono corretti.

## Placeholder da completare (`[DA COMPLETARE]`)

Cercali con:

```bash
grep -rn "DA COMPLETARE\|—\"" content/ app/
```

Elenco noto: numero ore recuperate caso VAS 3, foto professionale (About), URL LinkedIn, email di contatto, P.IVA, link articolo "Liquid Gastronomy 2026".
