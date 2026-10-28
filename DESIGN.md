# DESIGN SYSTEM — Portfolio Alessandro
Fonte di verità per ogni decisione visiva. Nessun modello deve deviare da questo file senza istruzione esplicita dell'utente.

## Filosofia
Minimalismo editoriale. Il sito È il portfolio: deve dimostrare gusto, non gridare.
Riferimenti di spirito (non copiare asset o testi):
- FERØ (fero-site.vercel.app): voce editoriale, retorica della negazione, ritmo verticale ampio, sobrietà.
- Catobi (catobi.it): architettura a domande ("In che fase sei?"), formule di ingaggio nominate, CTA ricorrente a bassa frizione, una persona presentata come entità strutturata.
- Muri/Otro: fotografia dello spazio bianco, tipografia come protagonista.
Anti-riferimento: estetica "AI startup" (gradient viola, glassmorphism, particelle, dark mode di default). VIETATA.

## Colori
--ink:        #101418   (testo primario, quasi-nero caldo)
--paper:      #FAFAF7   (fondo, bianco carta)
--accent:     #0062AD   (blu — SOLO per: link, CTA, sottolineature attive, dettagli grafici. Mai per fondi di intere sezioni, mai per testi lunghi)
--accent-ink: #004B85   (hover/stati attivi dell'accento)
--muted:      #5C6470   (testo secondario, didascalie)
--line:       #E4E2DC   (bordi sottili, separatori)
Regola: il blu #0062AD copre <5% della superficie di ogni viewport. È un accento chirurgico, non un tema.

## Tipografia
- Display/titoli: "Fraunces" (Google Fonts), variable, ottica alta per i titoli grandi. Pesi: 400 e 600. Corsivo consentito per enfasi editoriale.
- Corpo/UI: "Inter" (Google Fonts). Pesi: 400, 500, 600.
- Scala (desktop): h1 clamp(2.8rem→4.5rem), h2 2rem, h3 1.35rem, body 1.0625rem/1.7, caption 0.875rem.
- Titoli: tracking leggermente negativo (-0.02em). Mai tutto maiuscolo su frasi lunghe; kicker di sezione in maiuscoletto (font Inter 0.8rem, letter-spacing 0.08em, colore --muted).
- Caricamento font: next/font, self-hosted, display swap.

## Layout e ritmo
- Container: max-width 1120px, padding laterale 24px mobile / 48px desktop.
- Ritmo verticale generoso: sezioni separate da 120–160px desktop, 72–96px mobile.
- Griglia: 12 colonne concettuali; i blocchi di testo lungo non superano 65ch.
- Separatori: hairline 1px --line, mai box-shadow pesanti. Angoli: raggio 6px max su card/bottoni; niente pill esagerate.

## Componenti chiave
- Bottone primario: fondo --accent, testo bianco, padding 14px 28px, hover --accent-ink, transizione 150ms. Bottone secondario: solo testo --ink con freccia →, underline all'hover in --accent.
- Card caso studio: bordo 1px --line su --paper, hover: bordo diventa --accent + translateY(-2px). Dentro: kicker categoria, titolo Fraunces, una riga di sfida, il numero/contrasto in grande.
- Kicker di sezione + domanda: ogni sezione apre con kicker maiuscoletto e un H2 in forma di DOMANDA (pattern Catobi). Es. kicker "METODO" → H2 "Come lavoro?".

## Micro-interazioni (budget rigido)
UNA sola idea interattiva memorabile nel sito: il Diagnoser. Tutto il resto è quieto:
- hover misurati (150–200ms ease-out), fade-in-up delle sezioni allo scroll (una volta sola, threshold 0.2, translateY 12px, durata 500ms, rispetta prefers-reduced-motion),
- NIENTE: parallax, cursori custom, marquee multipli, contatori animati, effetti typing nell'hero.

## Accessibilità e qualità
- Contrasto AA minimo ovunque (#0062AD su #FAFAF7 passa per testi grandi e UI; per body text su fondo chiaro usare --ink).
- Focus visibili (outline 2px --accent, offset 2px). Navigazione completa da tastiera.
- Immagini con alt significativi. Lighthouse target: Performance ≥95, A11y ≥95, SEO ≥95.
