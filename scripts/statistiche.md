# Statistiche del sito (Umami Cloud)

Il codice è già pronto: lo script di Umami e il tracciamento eventi si accendono quando
`UMAMI_WEBSITE_ID` in `scripts/build.py` non è vuoto. Finché è vuoto il sito non carica nulla
e la privacy dice che non ci sono statistiche.

## Attivazione (una volta)

1. Vai su https://umami.is, **Get started** / **Sign up**, scegli il piano gratuito (Hobby).
   Se in fase di iscrizione puoi scegliere la regione dei dati, scegli **EU**.
2. Nel pannello: **Settings → Websites → Add website**.
   - Name: `Frau Studio`
   - Domain: `fraustudio.com`
3. Apri il sito appena creato → **Edit** (o *Tracking code*): copia il **Website ID**
   (formato `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`).
4. In `scripts/build.py` incollalo in `UMAMI_WEBSITE_ID = "..."`, poi:

   ```bash
   python3 scripts/build.py
   ```

   e committa i file generati. La privacy si aggiorna da sola (aggiunge Umami tra i fornitori).
5. Verifica: apri https://fraustudio.com, poi nel pannello Umami → **Realtime**: devi vederti.

### Escludere le tue visite

Su ogni browser/dispositivo che usi, apri fraustudio.com, poi la console del browser
(Mac: `Cmd+Option+J` su Chrome, `Cmd+Option+C` su Safari) e scrivi:

```js
localStorage.setItem("umami.disabled", "1")
```

Da quel momento Umami ignora quel browser. Per riattivarlo: `localStorage.removeItem("umami.disabled")`.

## Cosa registra

Automatico (Umami): pagine viste, visitatori unici, durata e rimbalzo, sito di provenienza,
parametri UTM, paese/regione/città, dispositivo, browser, sistema operativo, lingua.
Nella vista **Sessions** vedi il percorso del singolo visitatore anonimo (pagine + eventi).

Eventi personalizzati (pannello → **Events**; le proprietà tra parentesi sono in *Event data*):

| Evento | Quando | Proprietà |
|---|---|---|
| `clic-cta-contatto` | clic su un bottone/link verso il contatto | `posizione` (header, top, contatto, pagina del caso…), `testo` |
| `apri-caso` | apertura di un caso studio | `caso` (slug), `posizione` |
| `clic-email` | clic su un link email | `posizione` |
| `clic-whatsapp-demo` | clic sulla demo WhatsApp | `posizione` |
| `clic-linkedin`, `clic-github` | clic sui profili | `posizione` |
| `link-esterno` | clic su altri link esterni | `url`, `posizione` |
| `clic-menu` | clic su una voce del menu | `voce` |
| `sezione-vista` | una sezione della home arriva a metà schermo | `sezione` |
| `scroll` | profondità 25/50/75/100% | `percentuale`, `pagina` |
| `faq-aperta` | apertura di una FAQ | `domanda` |
| `modulo-iniziato` | primo campo del modulo toccato | — |
| `modulo-abbandonato` | uscita dalla pagina con modulo iniziato e non inviato | `ultimo_campo` |
| `invio-modulo` | modulo inviato con successo | — |
| `errore-modulo` | invio fallito (Worker giù o rete) | — |
| `pagina-404` | qualcuno arriva su un indirizzo inesistente | `percorso`, `provenienza` |

Un funnel utile da creare in **Reports → Funnel**: pagina `/` → `sezione-vista` lavori →
`apri-caso` → `modulo-iniziato` → `invio-modulo`.

Limiti onesti: non ci sono heatmap né registrazioni dello schermo, e non si identifica chi visita
(niente cookie, niente IP salvato). `modulo-abbandonato` è affidabile al 90%: alcuni browser
mobili chiudono la pagina prima di spedire l'evento.

## UTM: sapere da dove arriva chi visita

Ogni volta che condividi il sito usa un link con i parametri. Umami li legge da solo
(**Reports → UTM** e filtro per `utm_source`/`utm_campaign`).

Schema: `utm_source` = dove, `utm_medium` = tipo di canale, `utm_campaign` = cosa.
Tutto minuscolo, trattini al posto degli spazi.

| Dove | Link |
|---|---|
| Profilo LinkedIn (sito nel profilo) | `https://fraustudio.com/?utm_source=linkedin&utm_medium=profilo` |
| Post LinkedIn | `https://fraustudio.com/?utm_source=linkedin&utm_medium=post&utm_campaign=<tema-del-post>` |
| Messaggio LinkedIn diretto | `https://fraustudio.com/?utm_source=linkedin&utm_medium=messaggio` |
| Firma email | `https://fraustudio.com/?utm_source=email&utm_medium=firma` |
| Proposta / preventivo PDF | `https://fraustudio.com/?utm_source=proposta&utm_medium=pdf&utm_campaign=<cliente>` |
| Biglietto da visita / QR | `https://fraustudio.com/?utm_source=biglietto&utm_medium=qr` |
| GitHub (profilo o README) | `https://fraustudio.com/?utm_source=github&utm_medium=profilo` |
| Caso specifico in un post | `https://fraustudio.com/lavori/pico/?utm_source=linkedin&utm_medium=post&utm_campaign=pico` |

Nei post LinkedIn il link lungo si vede poco (LinkedIn mostra l'anteprima), quindi non serve
accorciarlo.
