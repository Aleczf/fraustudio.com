# BACKLOG — migliorie identificate ma NON implementate

Raccolte durante la Tranche 5 (QA critico). Sono fuori dallo scope "rifinire, non
aggiungere": ognuna richiede dati reali, asset, o una feature/struttura nuova.
Ordinate per impatto sulla prima impressione.

## Contenuti reali da inserire (bloccano la credibilità, servono i dati veri)
- **Esito VAS 3**: sia in IT (`content/it.ts`) sia in EN (`content/en.ts`) l'outcome
  inizia con un trattino dove dovrebbe esserci un numero ("— ore a settimana
  recuperate" / "— hours a week recovered"). Va inserita la cifra reale, altrimenti
  il caso più forte (unico "CLIENTE REALE") sembra incompleto.
- **Email di contatto**: placeholder `nome@dominio.it` / `name@domain.com` in
  `content/*.ts` (`contact.email`). Da sostituire con l'indirizzo reale (alimenta
  anche i `mailto:` delle pagine caso).
- **LinkedIn**: `href: "#"` in `about.links` e `contact.linkedinHref` (entrambe le
  lingue). Da collegare all'URL reale.
- **P.IVA**: `footer.vat` è "—". Da inserire quando disponibile.
- **Scrittura, card 1** ("Liquid Gastronomy 2026"): `href: "#"`. Da collegare
  all'articolo reale, oppure marcarla `comingSoon` come la card 2.

## Asset mancanti
- **Ritratto About**: oggi è un monogramma placeholder (`.about__photo`, "A."). Un
  ritratto vero (sobrio, luce naturale — vedi CONTENT.md) rafforzerebbe molto la
  prima impressione con l'imprenditore PMI e l'art director.
- **Favicon reale**: `public/favicon.svg` è un monogramma placeholder. Va bene per
  ora ed è referenziato correttamente in entrambi i layout, ma un set completo
  (favicon.ico multi-size + apple-touch-icon 180×180 + eventuale
  `icon-512.png`/manifest) è il dettaglio che un recruiter nota.
- **Font self-hosted**: `public/fonts/` esiste ma è vuota. `next/font/google` scarica
  Fraunces/Inter a build-time (richiede rete durante la build) e poi li self-hosta.
  Per build totalmente riproducibili/offline si potrebbero committare i file `.woff2`
  e passare a `next/font/local`.

## SEO / social
- **OG image in Fraunces**: `lib/og-image.tsx` usa `fontFamily: "serif"` (serif di
  sistema), non Fraunces. Per far combaciare l'immagine social con il brand va
  passato il font data a `ImageResponse` (richiede il binario del font). DESIGN.md
  prevede Fraunces nell'OG: oggi il fallback è un serif generico, editoriale ma non
  di marca.

## Feature (esplicitamente fuori scope in questa sessione)
- **Pagina Servizi / Prezzi**: l'imprenditore PMI non tecnico esce dal sito senza un
  range di prezzo. Oggi la risposta è solo nella FAQ "Quanto costa?" ("dipende dal
  problema"). Una pagina/box con 3 formule di ingaggio e ordini di grandezza di
  prezzo/tempo ridurrebbe la frizione. NON implementata (nuova sezione).
- **Streaming della risposta del Diagnoser**: oggi l'output arriva in un colpo dopo
  le frasi di attesa. Uno streaming SSE token-per-token darebbe percezione di
  velocità e “vita”. NON implementato (cambia la route e il componente).

## Note tecniche da verificare con la build reale (non confermabili in sandbox)
- La build Next richiede rete per `next/font/google` e per il primo `npm install`:
  questo sandbox è offline, quindi build/lint/typecheck non sono stati eseguiti qui.
  Da lanciare sul Mac: `npm install && npm run typecheck && npm run build`.
- `opengraph-image.tsx` usa `runtime = "edge"`: verificare che l'export OG generi
  correttamente in build (è il pattern standard, ma va confermato a build reale).
</content>
