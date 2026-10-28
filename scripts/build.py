#!/usr/bin/env python3
"""Genera le pagine statiche di fraustudio.com.

Testi e struttura stanno qui (equivalente di content/it.ts del portfolio Next.js);
lo stile sta in assets/style.css. Dopo una modifica:

    python3 scripts/build.py

e committa i file generati: index.html, 404.html, lavori/<slug>/index.html, sitemap.xml.
"""
from html import escape
from urllib.parse import quote
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent.parent
CSS_VERSION = hashlib.sha256((ROOT / "assets/style.css").read_bytes()).hexdigest()[:10]
SITE_URL = "https://fraustudio.com"
EMAIL = "alessandro.frau88@gmail.com"
GITHUB = "https://github.com/Aleczf"
LINKEDIN = "https://www.linkedin.com/in/alessandro-frau-095b60153/"
VAT = "14815310967"
# Endpoint del Cloudflare Worker che riceve il form (cartella worker/). Da aggiornare dopo il deploy.
FORM_ENDPOINT = "https://fraustudio-contatto.REPLACE_ME.workers.dev"
# Link di prenotazione (Cal.com, Calendly...). Se None, il bottone apre una email precompilata.
BOOKING_URL = None

META = {
    "title": "Frau Studio — Automazione e integrazioni per PMI · Alessandro Frau",
    "description": "Collego i gestionali che usi già ed elimino il lavoro fatto due volte: integrazioni su misura, Odoo, dashboard con AI e agenti WhatsApp. Milano, in sede o da remoto.",
}

NAV = {
    "brand": "Frau Studio",
    "links": [
        ("Metodo", "/#metodo"),
        ("Servizi", "/#servizi"),
        ("Lavori", "/#lavori"),
        ("Chi sono", "/#chi-sono"),
        ("Per agenzie", "/#agenzie"),
    ],
    "cta": "Raccontami il problema",
    "cta_href": "/#contatto",
}

HERO = {
    "lines": ["Collego i gestionali che usi già.", "Elimino il lavoro fatto due volte."],
    "sub": "Fatture smistate a mano, dati ricopiati da un sistema all'altro, richieste perse tra WhatsApp, email e telefono. Entro nei processi della tua azienda e costruisco l'automazione che serve, in giorni e non in trimestri, con l'AI solo dove conviene davvero.",
    "cta_primary": "Raccontami il problema →",
    "cta_primary_href": "/#contatto",
    "cta_secondary": "Guarda i lavori",
    "cta_secondary_href": "/#lavori",
    "context_strong": "Non un'agenzia, non un dipendente.",
    "context": "Una persona sola che analizza e costruisce: chi fa la diagnosi è chi scrive il codice. Milano, in sede o da remoto.",
}

METHOD = {
    "kicker": "METODO",
    "question": "Come lavoro?",
    "intro": "Tre fasi, sempre le stesse. Cambia solo il tuo processo.",
    "phases": [
        ("01", "Entro", "Mi siedo dove il lavoro succede davvero: il gestionale, le email, il foglio Excel delle 18:30. Otto anni nelle brigate di cucine stellate mi hanno insegnato a leggere i sistemi di produzione sotto pressione: flussi, colli di bottiglia, cosa si rompe e perché."),
        ("02", "Capisco", "Identifico dove l'automazione e l'AI convengono davvero — e dove no. Non ogni processo va automatizzato: alcuni vanno semplificati, altri lasciati alle persone. La diagnosi è il prodotto, non un preambolo."),
        ("03", "Costruisco", "Sviluppo la soluzione su misura, dentro gli strumenti che già usi, e te la consegno in modo che il tuo team possa mantenerla. Quello che richiedeva quattro fornitori e mesi, oggi è una persona e qualche settimana."),
    ],
    "engagement_closing": "Mi ingaggi in tre modi:",
    "engagement": [
        ("Diagnosi singola", "Una prima lettura del tuo processo, mirata e concreta."),
        ("Progetto chiuso", "Analisi e costruzione della soluzione, con consegna definita."),
        ("Fractional", "Presenza continuativa part-time, senza il costo di un'assunzione."),
    ],
}

SERVICES = {
    "kicker": "SERVIZI",
    "question": "Su cosa intervengo?",
    # (problema, servizio, descrizione)
    "items": [
        ("Sistemi che non si parlano", "Integrazioni su misura", "Collego gestionali, piattaforme di settore, e-commerce e canali di messaggistica via API, con scritture senza doppioni e riallineamenti automatici."),
        ("Ore spese a leggere e smistare", "Dashboard con AI", "Cruscotti costruiti sui dati che l'azienda ha già, con modelli linguistici che classificano, analizzano e smistano al posto delle persone."),
        ("Un gestionale che è diventato un limite", "Odoo", "Moduli personalizzati, configurazione e migrazioni da ERP proprietari."),
        ("Clienti e richieste persi su WhatsApp", "Agenti WhatsApp", "Agenti che conversano con clienti e team su WhatsApp, vocali compresi, e scrivono nei sistemi aziendali."),
    ],
}

# Un caso: badge (+ nota), categoria, nome, sfida, intervento (+ punti), esito, stack, link esterno.
# "filled": solo i lavori con un cliente reale hanno il badge pieno.
# "lab": progetti miei, mostrati in forma compatta sotto i casi cliente.
# "hidden": la pagina non viene generata e il caso non compare sul sito.
WORKS = {
    "kicker": "LAVORI",
    "question": "Cosa ho costruito?",
    "transparency": "Lavori per clienti reali, raggruppati per il problema che risolvono. Per ognuno è indicato dove si trova oggi il progetto.",
    "view_case": "Leggi il caso",
    "groups": [
        ("Togliere lavoro manuale", "Documenti e richieste che oggi qualcuno legge e smista a mano.", ["controllo-costi-fatture", "intake-studio-legale"]),
        ("Far parlare i sistemi", "Lo stesso dato inserito in due posti, o sparso tra strumenti diversi.", ["odoo-cartsan", "crm-clinica"]),
        ("Cambiare o costruire il gestionale", "Quando lo strumento che c'è non basta più, o non c'è ancora.", ["migrazione-erp-odoo", "magazzino-filati", "gioielli-odoo"]),
    ],
    "lab_title": "Prodotti e laboratorio",
    "lab_desc": "Progetti miei: servono a provare il metodo prima di portarlo nei progetti dei clienti.",
    "cases": [
        {
            "slug": "controllo-costi-fatture",
            "summary": "Ore ogni settimana a smistare a mano le fatture passive, senza sapere quanto pesasse davvero ogni voce di costo.",
            "badge": "CLIENTE REALE", "filled": True, "note": "in produzione",
            "name": "Controllo costi sulle fatture passive",
            "category": "Controllo di gestione · Fatturazione elettronica · AI",
            "challenge": "Un'azienda affogava nella fatturazione passiva: ogni settimana, ore a smistare a mano le fatture tra materie prime, materiali di consumo e spese generali. E il titolare decideva gli acquisti senza conoscere il peso reale di ogni voce: i dati c'erano, chiusi negli XML delle fatture elettroniche.",
            "intervention": "Sono entrato nel processo e ho costruito un sistema che legge le fatture FatturaPA, classifica ogni riga per centro di costo e mostra costi e margine in una dashboard, dentro gli strumenti che il cliente già usava — così può mantenerlo senza dipendere da me. Un modello linguistico classifica solo i prodotti nuovi; gli altri arrivano dal catalogo. I limiti di Apps Script sono diventati scelte di progetto:",
            "points": [
                ("Il foglio non è il database.", "La fonte della verità sono gli XML su Drive: il foglio si ricostruisce da zero in qualsiasi momento."),
                ("Il limite di tempo diventa un lotto.", "La ricostruzione procede a blocchi, così anche anni di fatture non si interrompono a metà."),
                ("Le quote spingono al riuso.", "Più cresce il catalogo, meno chiamate al modello e classificazioni sempre coerenti."),
                ("Nessun server.", "Tutto resta nell'account Google del cliente, a costo quasi nullo."),
            ],
            "outcome": "Circa 4 ore a settimana recuperate. Classificazione automatica in produzione.",
            "stack": "Google Apps Script · Google Sheets · Google Drive · Claude API",
        },
        {
            "slug": "pico",
            "lab": True,
            "summary": "Nei CRM dormono contatti che hanno già chiesto un preventivo o comprato. Nessuno li ricontatta.",
            "lab_line": "Agente WhatsApp che ricontatta i lead fermi nel CRM. In produzione dal primo cliente.",
            "badge": "PRODOTTO", "note": "in produzione",
            "name": "Pico",
            "category": "Agente AI · WhatsApp · Riattivazione clienti",
            "challenge": "In ogni CRM dormono contatti che hanno chiesto un preventivo o comprato una volta, poi sono spariti. Ricontattarli a mano non scala; non ricontattarli è fatturato perso.",
            "intervention": "Pico è un mio prodotto: un agente AI che scrive su WhatsApp ai contatti fermi nel CRM, porta avanti la conversazione in modo naturale, capisce anche i vocali e passa all'attività chi è pronto a comprare o prenotare. Il motore è generale; la personalità e il contesto si modulano sul settore del cliente.",
            "points": [
                ("API ufficiali di Meta.", "Integrazione diretta con WhatsApp Cloud API, trascrizione dei vocali, stato delle conversazioni persistito."),
                ("Architettura riusabile.", "La sto adattando a un secondo caso d'uso: la reportistica dei team sul campo."),
            ],
            "outcome": "In produzione dal primo cliente, con vendite in crescita dai lead tornati attivi.",
            "stack": "Node.js · WhatsApp Cloud API · Claude API · SQLite · Whisper",
        },
        {
            "slug": "crm-clinica",
            "badge": "CLIENTE REALE", "filled": True, "note": "consegnato",
            "name": "CRM per una clinica",
            "category": "Medicina estetica · CRM · Odoo",
            "challenge": "Chiamate, messaggi e appuntamenti vivevano in strumenti separati, senza uno storico unico del paziente.",
            "intervention": "Un CRM su Odoo per il call center della clinica, in un team di tre sviluppatori. Ho curato la parte Odoo e le integrazioni.",
            "points": [
                ("Le chiamate entrano in Odoo.", "Ogni chiamata del centralino cloud si aggancia al contatto riconosciuto dal numero. Se il numero è nuovo, nasce un contatto e il primo interesse diventa un'opportunità."),
                ("WhatsApp nello stesso storico.", "Le conversazioni arrivano nella scheda del paziente accanto alle chiamate, e l'operatore risponde da Odoo senza cambiare strumento."),
                ("Un percorso fino all'appuntamento.", "La pipeline segue le fasi reali del call center, dal primo contatto alla visita, con promemoria per i richiami."),
                ("Sviluppo in un ambiente isolato.", "Odoo 17 in container con il proprio database, separato da ogni altro progetto: niente moduli o dati condivisi tra clienti."),
                ("Modulo neutro.", "Il modulo non porta il marchio di chi rivende il servizio, quindi si può installare su un altro cliente senza riscriverlo."),
            ],
            "outcome": "Chiamate, WhatsApp e appuntamenti in un unico storico del paziente.",
            "stack": "Odoo 17 · Docker · PostgreSQL · Aircall · WhatsApp",
        },
        {
            "slug": "odoo-cartsan",
            "summary": "Ogni assunzione o cessazione inserita due volte: nel gestionale e, a mano, su Cartsan.",
            "badge": "CLIENTE REALE", "filled": True, "note": "consegnato",
            "name": "Odoo collegato a Cartsan",
            "category": "Sicurezza sul lavoro · Integrazione gestionali",
            "challenge": "Una società di servizi per la sicurezza sul lavoro gestiva le aziende clienti con un gestionale datato. Ogni assunzione o cessazione andava poi riportata a mano su Cartsan, la piattaforma di medicina del lavoro: doppio inserimento ed errori.",
            "intervention": "Odoo al posto del vecchio gestionale, come unico punto di inserimento per aziende, dipendenti e calendario. Cartsan si aggiorna da solo.",
            "points": [
                ("Sincronizzazione su evento.", "Quando in Odoo si inserisce un dipendente o se ne registra la cessazione, Odoo chiama le Web API di Cartsan e aggiorna l'anagrafica. Niente esportazioni né reinserimenti."),
                ("Prima lo sviluppo, poi la produzione.", "L'integrazione è stata costruita e collaudata sull'ambiente di sviluppo di Cartsan, a partire dalla documentazione Swagger delle API, e solo dopo portata sui dati reali."),
                ("Mappatura tra due modelli dati.", "Aziende, sedi e dipendenti sono organizzati in modo diverso in Odoo e in Cartsan: la corrispondenza tra i campi è esplicita e documentata, così si può verificare e mantenere."),
                ("Errori visibili, non persi.", "Se Cartsan rifiuta un aggiornamento, l'operazione resta segnalata in Odoo e si può ripetere, invece di sparire in silenzio."),
                ("Recupero dello storico.", "Il database MySQL del vecchio gestionale è la base per migrare anagrafiche e rapporti esistenti."),
                ("Perimetro a fasi.", "Ho segnalato che il budget iniziale non copriva il progetto completo. Il primo rilascio è stato ristretto al flusso con più valore, la sincronizzazione dei dipendenti verso Cartsan."),
            ],
            "outcome": "Un solo inserimento: Cartsan si aggiorna da solo.",
            "stack": "Odoo · Cartsan Web API · Swagger · MySQL",
        },
        {
            "slug": "intake-studio-legale",
            "summary": "Richieste da telefono, social e WhatsApp, e ogni caso assegnato a mano a un avvocato.",
            "badge": "CLIENTE REALE", "filled": True, "note": "consegnato",
            "name": "Intake con AI per uno studio legale",
            "category": "Studio legale · Dashboard con AI · Odoo",
            "challenge": "Uno studio di una decina di persone riceveva richieste da telefono, social e WhatsApp senza un CRM né un sistema interno. Chi assegna un caso a quale avvocato lo decideva a mano, ogni volta.",
            "intervention": "Un modulo di intake su Odoo. Ogni richiesta viene registrata, analizzata da un modello linguistico e proposta all'avvocato giusto. Una dashboard mostra tutto, e gli avvocati possono correggere l'assegnazione dalla dashboard o direttamente da WhatsApp.",
            "points": [
                ("Sopra Odoo, non accanto.", "Invece di un'app separata, Odoo con un'interfaccia alleggerita nei colori dello studio: CRM, firma degli incarichi e storico nello stesso posto."),
                ("Gli strumenti esistenti restano.", "Lo studio usava già un proprio assistente AI personalizzato e non voleva perderlo: la dashboard lo interroga."),
                ("Dati sensibili.", "L'infrastruttura gira su cloud dedicato, con la sicurezza come requisito di partenza."),
                ("Demo funzionante prima del contratto.", "Prototipo su Odoo in container con dati inventati, usato nella trattativa con lo studio."),
            ],
            "outcome": "Ogni richiesta registrata, analizzata e proposta all'avvocato giusto. L'ultima parola resta a una persona.",
            "stack": "Odoo 17 · Claude API · WhatsApp · Docker · AWS",
        },
        {
            "slug": "migrazione-erp-odoo",
            "summary": "Un ERP proprietario su un server in sede, e un'azienda che vuole uscire dall'ecosistema del fornitore.",
            "badge": "CLIENTE REALE", "filled": True, "note": "in corso",
            "name": "Da un ERP proprietario a Odoo",
            "category": "PMI · ERP · Migrazione",
            "challenge": "L'azienda usa un ERP proprietario installato su un server in sede, gestito da un fornitore esterno. Vuole uscire dall'intero ecosistema del vecchio fornitore, non solo cambiare un modulo.",
            "intervention": "Il progetto è nato come integrazione via API con l'ERP esistente. Dall'analisi è emerso che la scelta giusta era una migrazione completa, e il perimetro è cambiato di conseguenza.",
            "points": [
                ("Analisi con il fornitore uscente.", "Partecipo agli incontri tecnici con chi gestisce oggi ERP e server, per mappare dati, database e dipendenze prima di pianificare il passaggio."),
                ("Dal server in sede al cloud gestito.", "L'ipotesi di arrivo è Odoo Enterprise su Odoo.sh per ERP e database, così l'azienda non dipende più da un server locale."),
                ("Migrazione come occasione.", "Oltre al trasferimento dei dati: dashboard su misura e revisione dei processi che oggi esistono solo perché il vecchio sistema li imponeva."),
            ],
            "outcome": "La diagnosi ha cambiato il progetto: da integrazione a migrazione completa.",
            "stack": "Odoo.sh · Odoo Enterprise · Migrazione ERP · Dashboard",
        },
        {
            "slug": "gioielli-odoo",
            "summary": "Un brand di gioielli personalizzati che parte da zero, senza sistemi da ereditare.",
            "badge": "CLIENTE REALE", "filled": True, "note": "in corso",
            "name": "Un brand di gioielli su Odoo",
            "category": "E-commerce · Gioielli personalizzati · Odoo",
            "challenge": "Un nuovo brand di gioielli personalizzati parte da zero: negozio online, clienti, magazzino e fatture devono stare in un unico sistema dal primo giorno.",
            "intervention": "Nel team mi occupo di Odoo e delle integrazioni: configurazione di CRM, magazzino e fatturazione, collegamento di WhatsApp al CRM e delle richieste di gioielli su misura.",
            "points": [
                ("Architettura valutata prima di scegliere.", "Avevo progettato un middleware tra un e-commerce esterno e Odoo, con verifica della firma dei webhook, scritture senza doppioni tramite ID esterno e riallineamento notturno. Il team ha poi scelto l'e-commerce nativo di Odoo, che elimina un sistema da mantenere."),
                ("Ipotesi scritte nella stima.", "Volumi, tipo di clienti e perimetro della fatturazione sono dichiarati nel preventivo, in giornate per blocco di lavoro, così ogni cambio di perimetro ha un costo visibile."),
            ],
            "outcome": "Negozio, clienti, magazzino e fatture in un solo sistema dal primo giorno.",
            "stack": "Odoo · E-commerce Odoo · WhatsApp · API JSON-2",
        },
        {
            "slug": "magazzino-filati",
            "summary": "Una trentina di filati da seguire per quantità, lotto e capi in cui finiscono.",
            "badge": "CLIENTE REALE", "filled": True, "note": "MVP in corso",
            "name": "Magazzino filati per un maglificio",
            "category": "Manifattura · Magazzino · Controllo di gestione",
            "challenge": "Un maglificio lavora con una trentina di filati e deve sapere quanto filato ha, da quale lotto, e in quali capi è finito.",
            "intervention": "Un gestionale con carico dei filati dai documenti di trasporto e scarico per ordine, più una pagina ordini per capi fatti con fino a cinque filati.",
            "points": [
                ("Il vincolo del lotto nel modello dati.", "Un ordine usa un solo lotto per colore, per evitare differenze di tinta: il sistema lo impone invece di affidarlo alla memoria di chi prepara l'ordine."),
                ("MVP sullo stesso stack del prodotto finale,", "ripreso dal sistema di controllo costi sulle fatture passive. Quello che il cliente prova è quello che riceverà."),
                ("Manutenibile senza teleassistenza.", "È un requisito di progetto. In valutazione il passaggio a un database PostgreSQL ospitato, con preventivo separato per hosting e manutenzione."),
            ],
            "outcome": "Ogni capo tracciabile fino al filato e al suo lotto.",
            "stack": "JavaScript · Google Apps Script · Google Sheets",
        },
        {
            "slug": "fero",
            "lab": True,
            "summary": "Vetrina, scelta assistita, contatti e back-office: di norma quattro fornitori e settimane di coordinamento.",
            "lab_line": "Vetrina, scelta assistita, contatti e back-office in un solo sistema, costruito in giorni.",
            "badge": "CONCEPT DIMOSTRATIVO",
            "name": "FERØ",
            "category": "Sistema completo · AI · E-commerce",
            "challenge": "Una piccola impresa che vende un prodotto premium ha bisogno di vetrina credibile, scelta assistita, acquisizione contatti e back-office: di norma quattro fornitori diversi e settimane di coordinamento.",
            "intervention": "L'ho costruito intero, da solo: sito editoriale, advisor AI che abbina prodotto e occasione come farebbe un sommelier, flusso di prenotazione con conferma automatica, back-office che classifica gli ordini da sé.",
            "outcome": "Quattro fornitori, uno. Settimane, giorni.",
            "stack": "Next.js · Claude API · Vercel",
            "external": ("https://fero-site.vercel.app", "fero-site.vercel.app"),
        },
        {
            "slug": "wineguard",
            "lab": True,
            "summary": "L'anticontraffazione per il vino chiede chip, RFID o etichette speciali che molte cantine non sostengono.",
            "lab_line": "Anticontraffazione per il vino con la sola fotocamera di uno smartphone.",
            "badge": "R&D", "note": "in test",
            "name": "WineGuard",
            "category": "Wine-tech · Anticontraffazione · Computer vision",
            "challenge": "Le soluzioni anticontraffazione per il vino chiedono chip, RFID o etichette speciali: costi e modifiche di linea che molte cantine non sostengono.",
            "intervention": "Un sistema solo software che riconosce un'etichetta autentica dalla struttura microscopica delle fibre della carta, unica per ogni foglio e impossibile da riprodurre. Lo sto validando così:",
            "points": [
                ("Test con criteri di arresto.", "Il prototipo deve superare tre prove binarie prima di andare avanti. Il protocollo in corso usa 24 fogli in sei condizioni diverse, con cicli di umidità, per verificare che la firma della carta resti leggibile nel tempo."),
                ("Il vantaggio sta nella carta.", "Il lavoro con i produttori di carte speciali punta a supporti progettati insieme, più difendibili di qualsiasi algoritmo."),
                ("Mercato scelto sui dati.", "Il primo segmento è il vino di fascia alta e i consorzi, dove la contraffazione esiste davvero e c'è disponibilità a pagare per difendersi."),
                ("Pensato per integrarsi.", "Affianca blockchain e passaporto digitale di prodotto: fornisce il legame fisico tra la bottiglia e il suo record digitale."),
            ],
            "outcome": "Basta la fotocamera di uno smartphone.",
            "stack": "Computer vision · Python",
        },
        {
            "slug": "nolo-hub",
            "lab": True,
            "lab_line": "Piattaforma editoriale con sistema agentico sul mondo no/low alcohol.",
            "badge": "IN COSTRUZIONE",
            "name": "NOLO HUB",
            "category": "Piattaforma editoriale · Sistema agentico",
            "challenge": "Il mondo no/low alcohol cresce, ma in Italia nessuno lo racconta con profondità.",
            "intervention": "Sto costruendo una piattaforma editoriale AI-native: pipeline di contenuto orchestrata da agenti con supervisione umana — gli agenti producono, le persone decidono. Architettura: nessun agente è mai responsabile ultimo; lo è sempre un umano.",
            "outcome": "Il mio laboratorio a cielo aperto: quello che imparo qui finisce nei progetti dei clienti.",
            "stack": "Astro · TypeScript · n8n · Notion",
        },
        {
            "slug": "cold-outreach",
            "hidden": True,
            "badge": "STRUMENTO INTERNO", "note": "in avvio",
            "name": "Cold outreach a costo quasi nullo",
            "category": "Lead generation B2B · Automazione",
            "challenge": "Lo stack tipico per trovare e contattare aziende costa 100–150 € al mese tra abbonamenti diversi.",
            "intervention": "Una pipeline che sostituisce tre abbonamenti con codice proprio, eseguita su job programmati. È pronta e in fase di avvio.",
            "points": [
                ("Ricerca delle aziende.", "Le attività di un territorio e di un settore arrivano dalla API di Google Places, al posto dei database a pagamento."),
                ("Messaggi personalizzati.", "Un modello linguistico leggero scrive l'apertura di ogni email a partire dai dati dell'azienda."),
                ("Esecuzione senza server.", "I job girano su GitHub Actions a orari fissi: niente macchina da mantenere accesa."),
                ("Reputazione protetta.", "Gli invii partono da un dominio dedicato, separato da quello principale, così un problema di consegna non tocca la posta di lavoro."),
            ],
            "outcome": "Da 100–150 € a 3–5 € al mese, stimati.",
            "stack": "Node.js · GitHub Actions · Google Places API · Claude API · Zoho Mail",
        },
    ],
}

TRUST = {
    "kicker": "AFFIDABILITÀ",
    "question": "Sei una persona sola. Cosa succede se ti fermi?",
    "intro": "È la domanda giusta. Ecco come lavoro perché il sistema che ti consegno non dipenda da me.",
    "items": [
        ("Il codice è tuo", "Repository, account e chiavi sono intestati alla tua azienda. Io lavoro con accessi che puoi revocare in qualsiasi momento."),
        ("Documentazione a ogni consegna", "Come funziona, dove si trova, cosa fare se qualcosa si ferma. Scritta perché la legga anche un altro sviluppatore."),
        ("Testato prima di consegnare", "Vengo dal QA testing di app e dispositivi: prima di consegnare provo i casi in cui il sistema si può rompere."),
        ("Dati riservati, accessi minimi", "Accedo solo ai dati che servono. Sulle decisioni delicate l'AI propone e una persona conferma."),
        ("Manutenzione esplicita", "Un accordo a parte, con tempi di risposta scritti. Sai prima cosa copre e quanto costa."),
        ("Quando serve più di me", "Sui progetti più grandi lavoro con altri sviluppatori e partner Odoo di fiducia, e te lo dico all'inizio."),
    ],
}

ABOUT = {
    "kicker": "CHI SONO",
    "question": "Chi c'è dietro?",
    "photo_alt": "Ritratto di Alessandro Frau",
    "paragraphs": [
        "Sono Alessandro, e Frau Studio sono io. Prima di scrivere codice ho passato otto anni nelle cucine e nelle sale di ristoranti stellati, e sono sommelier AIS. In una brigata impari a leggere un sistema di produzione sotto pressione — flussi, ruoli, colli di bottiglia, cosa cede per primo quando il ritmo sale. È esattamente quello che faccio oggi nelle aziende: solo che ora, dopo la diagnosi, la soluzione la costruisco anch'io.",
        "Dopo la cucina ho lavorato come sviluppatore full-stack, su applicazioni web, integrazioni e AI, e come QA tester su app e dispositivi mobili per piattaforme di crowdtesting internazionali. Dallo sviluppo viene il modo in cui costruisco; dal testing un'abitudine che porto in ogni progetto: chiedermi come un sistema si può rompere prima di consegnarlo.",
        "Ho fondato WineGuard, un sistema di autenticazione ottica per il vino in fase di tutela della proprietà intellettuale. Lavoro direttamente con le PMI oppure dentro i progetti di agenzie e software house. Vivo e lavoro a Milano, in sede o da remoto; parlo italiano, inglese e francese.",
    ],
    "links": [("GitHub", GITHUB), ("LinkedIn", LINKEDIN)],
}

AGENCY = {
    "kicker": "PER AGENZIE E SOFTWARE HOUSE",
    "question": "Vi serve una persona su Odoo, integrazioni o AI?",
    "intro": "Entro nel vostro progetto per la parte tecnica e consegno dentro i vostri tempi e le vostre regole.",
    "items": [
        ("Nei vostri strumenti", "Lavoro sul vostro repository, con il vostro sistema di ticket e le vostre convenzioni di codice."),
        ("Il cliente resta vostro", "Parlo con il cliente solo se e quando lo decidete voi."),
        ("Consegna documentata", "Ogni modulo o integrazione arriva con documentazione e passaggio di consegne al vostro team."),
    ],
    "cta": "Parliamo di una collaborazione →",
}

WRITING = {
    "kicker": "SCRITTURA",
    "question": "Cosa penso?",
    "soon_label": "In arrivo",
    # (titolo, href) — href None = "in arrivo"
    "cards": [
        ("Liquid Gastronomy 2026", None),
        ("Quello che una brigata stellata insegna sui processi aziendali", None),
    ],
}

FAQ = {
    "kicker": "FAQ",
    "question": "Cosa mi chiedono più spesso?",
    "items": [
        ("Devo sapere già cosa mi serve?", "No. Basta raccontarmi cosa succede oggi e dove si perde tempo. Capire quale strumento serve, e se serve, è il mio lavoro."),
        ("Che differenza c'è tra te e un'agenzia di automazione?", "Un'agenzia ti vende il suo pacchetto. Io entro nel tuo processo, capisco cosa serve davvero — a volte è meno di quello che pensavi — e costruisco solo quello. E resto una persona sola: chi diagnostica è chi costruisce."),
        ('Cosa significa "fractional"?', "Presenza continuativa part-time: un numero di ore o giornate al mese concordato, dentro il tuo team, senza il costo e il vincolo di un'assunzione. Mi prendi per il problema, non a tempo pieno."),
        ("Lavori con Odoo e con i gestionali che uso già?", "Sì. Su Odoo sviluppo moduli personalizzati, lo configuro e migro i dati da ERP proprietari. Se usi già un altro gestionale, un CRM o un e-commerce, lo collego via API agli altri strumenti — fatture elettroniche, WhatsApp, piattaforme di settore — con scritture senza doppioni e riallineamenti automatici. Spesso non serve cambiare sistema: serve farli parlare tra loro."),
        ("Che tecnologie usi?", "Le più semplici che reggono il tuo caso. A volte è un foglio Google potenziato con AI, a volte un agente su WhatsApp, a volte Odoo o un'applicazione completa. La tecnologia è una conseguenza della diagnosi, mai il punto di partenza."),
        ("Quanto costa?", "Dipende dal problema, non dal mio umore: dopo una prima conversazione ti do un prezzo chiuso o una tariffa chiara, con la manutenzione esplicitata a parte. Niente sorprese a consuntivo."),
    ],
}

CONTACT = {
    "kicker": "CONTATTO",
    "question": "Che processo ti rallenta?",
    "body": "Raccontamelo in poche righe. Ti dico come lo automatizzerei, e se non conviene automatizzarlo ti dico anche quello.",
    "steps": [
        ("1. Mi racconti il problema", "Poche righe, nessuna competenza tecnica richiesta."),
        ("2. Valutiamo il processo", "In 30 minuti capisco dove si perde tempo e se conviene intervenire."),
        ("3. Ricevi una proposta chiara", "Perimetro, risultato atteso, tempi, prezzo e manutenzione, prima di iniziare."),
    ],
    "form": {
        "problema": ("Cosa succede oggi?", "Es. ogni settimana una persona ricopia a mano gli ordini dall'e-commerce al gestionale."),
        "strumenti": ("Che strumenti usate?", "Es. gestionale, Excel, WhatsApp, e-commerce"),
        "nome": "Nome e azienda",
        "email": "Email",
        "submit": "Invia il problema →",
        "reply_time": "Ti rispondo entro 2 giorni lavorativi.",
        "privacy": "Uso questi dati solo per risponderti. Dettagli nell'",
        "sent": "Ricevuto. Ti rispondo entro 2 giorni lavorativi.",
        "error": "Non è partito. Riprova tra poco oppure scrivimi a",
    },
    "call_title": "Preferisci parlarne a voce?",
    "call_body": "30 minuti sul tuo processo, senza impegno.",
    "call_cta": "Prenota una chiamata →",
    "mail_title": "Oppure scrivimi",
    "closing": "30 minuti sul tuo processo, senza impegno.",
}

PRIVACY = {
    "title": "Informativa privacy",
    "updated": "Ultimo aggiornamento: ottobre 2026",
    "sections": [
        ("Chi tratta i dati", f"Il titolare del trattamento è Alessandro Frau (Frau Studio), P.IVA {VAT}, Milano. Per qualsiasi richiesta sui tuoi dati scrivi a {EMAIL}."),
        ("Quali dati", "Se compili il modulo di contatto: nome, azienda, indirizzo email e quello che scrivi nella descrizione del problema e degli strumenti. Il sito non usa cookie di profilazione né strumenti di analisi."),
        ("Perché e su quale base", "Uso questi dati solo per rispondere alla tua richiesta e, se lo vuoi, per preparare una proposta. La base giuridica è l'esecuzione di misure precontrattuali richieste da te (art. 6.1.b GDPR)."),
        ("Per quanto tempo", "Conservo la richiesta per il tempo necessario a gestirla e comunque non oltre 24 mesi, salvo che nasca un rapporto di lavoro: in quel caso valgono i tempi previsti per la documentazione contrattuale e fiscale."),
        ("Chi altro li vede", "Il modulo passa da Cloudflare, che riceve la richiesta, e da Resend, che me la inoltra via email; la casella di destinazione è su Google. Sono fornitori tecnici che trattano i dati per mio conto. Alcuni hanno sede negli Stati Uniti: il trasferimento avviene con le garanzie previste dal GDPR (clausole contrattuali standard o Data Privacy Framework). Non vendo né cedo i dati a nessuno."),
        ("I tuoi diritti", "Puoi chiedere accesso, rettifica, cancellazione, limitazione, opposizione e portabilità dei tuoi dati scrivendo all'indirizzo sopra. Se ritieni che il trattamento violi il GDPR puoi presentare reclamo al Garante per la protezione dei dati personali."),
    ],
}

FOOTER = {
    "meta": ["Frau Studio · Alessandro Frau", f"P.IVA {VAT}", "Milano", "© 2026"],
}

NOT_FOUND = {"title": "Questa pagina non esiste.", "body": "Il metodo sì.", "cta": "Torna alla home"}


# ---------------------------------------------------------------------------
# Template
# ---------------------------------------------------------------------------
e = escape


def head(title, description, path):
    url = SITE_URL + path
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{url}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:locale" content="it_IT">
<meta property="og:site_name" content="Frau Studio">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE_URL}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400;1,9..144,600&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="/assets/style.css?v={CSS_VERSION}">
<script>document.documentElement.classList.add("js")</script>
</head>
<body>
"""


def header():
    links = "\n".join(f'        <li><a href="{h}" class="site-nav__link">{e(l)}</a></li>' for l, h in NAV["links"])
    mlinks = "\n".join(f'  <a href="{h}" class="mobile-menu__link">{e(l)}</a>' for l, h in NAV["links"])
    return f"""
<header class="site-header">
  <div class="container site-header__inner">
    <a href="/#top" class="wordmark">{e(NAV["brand"])}</a>

    <nav class="site-nav" aria-label="Navigazione principale">
      <ul class="site-nav__list">
{links}
      </ul>
    </nav>

    <div class="site-header__actions">
      <a href="{NAV["cta_href"]}" class="btn btn-primary site-header__cta">{e(NAV["cta"])}</a>
      <button type="button" class="menu-toggle" aria-expanded="false" aria-controls="mobile-menu" aria-label="Apri il menu">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
          <line x1="3" y1="8" x2="21" y2="8" />
          <line x1="3" y1="16" x2="21" y2="16" />
        </svg>
      </button>
    </div>
  </div>
</header>

<div id="mobile-menu" class="mobile-menu" role="dialog" aria-modal="true" aria-label="Menu" hidden>
  <div class="container mobile-menu__top">
    <span class="wordmark">{e(NAV["brand"])}</span>
    <button type="button" class="menu-toggle" data-menu-close aria-label="Chiudi il menu">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
        <line x1="5" y1="5" x2="19" y2="19" />
        <line x1="19" y1="5" x2="5" y2="19" />
      </svg>
    </button>
  </div>
  <nav class="container mobile-menu__nav" aria-label="Navigazione mobile">
{mlinks}
  </nav>
  <div class="container mobile-menu__footer">
    <a href="{NAV["cta_href"]}" class="btn btn-primary">{e(NAV["cta"])}</a>
  </div>
</div>
"""


def footer():
    meta = "\n".join(f"      <span>{e(m)}</span>" for m in FOOTER["meta"])
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="site-footer__meta">
{meta}
      <span><a href="/privacy/">Privacy</a></span>
    </div>
  </div>
</footer>
"""


SCRIPT = """
<script>
  // Stessi comportamenti dei componenti React del portfolio, in JS semplice.
  (function () {
    // Header: blur e bordo quando si scrolla (Header.tsx)
    var header = document.querySelector(".site-header");
    function onScroll() { header.classList.toggle("is-scrolled", window.scrollY > 8); }
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });

    // Menu mobile a schermo pieno: Escape chiude, focus intrappolato, focus riportato al toggle
    var toggle = document.querySelector(".site-header__actions .menu-toggle");
    var menu = document.getElementById("mobile-menu");
    var closeBtn = menu.querySelector("[data-menu-close]");
    var prevOverflow = "";
    function openMenu() {
      menu.hidden = false;
      toggle.setAttribute("aria-expanded", "true");
      prevOverflow = document.body.style.overflow;
      document.body.style.overflow = "hidden";
      closeBtn.focus();
      document.addEventListener("keydown", onKey);
    }
    function closeMenu() {
      menu.hidden = true;
      toggle.setAttribute("aria-expanded", "false");
      document.body.style.overflow = prevOverflow;
      document.removeEventListener("keydown", onKey);
      toggle.focus();
    }
    function onKey(e) {
      if (e.key === "Escape") { e.preventDefault(); closeMenu(); return; }
      if (e.key !== "Tab") return;
      var f = menu.querySelectorAll("a[href], button:not([disabled])");
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
    toggle.addEventListener("click", openMenu);
    closeBtn.addEventListener("click", closeMenu);
    menu.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", closeMenu); });

    // Fade-in-up delle sezioni allo scroll, una volta sola (Section.tsx). Soglia 0 e non 0.2:
    // con 12 card la sezione Lavori su telefono è alta più di 5 schermi e il 20% non entra mai.
    var items = document.querySelectorAll(".reveal");
    if (!("IntersectionObserver" in window)) {
      items.forEach(function (el) { el.classList.add("is-visible"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("is-visible"); io.unobserve(e.target); }
      });
    }, { threshold: 0, rootMargin: "0px 0px -15% 0px" });
    items.forEach(function (el) { io.observe(el); });
  })();

  // Modulo di contatto: invio al Cloudflare Worker senza ricaricare la pagina.
  (function () {
    var form = document.getElementById("contact-form");
    if (!form || !window.fetch) return;
    var started = Date.now();
    var status = form.querySelector(".contact-form__status");
    var button = form.querySelector("button[type=submit]");
    var MSG_SENT = __MSG_SENT__;
    var MSG_ERROR = __MSG_ERROR__;
    var EMAIL = __EMAIL__;
    function show(text, isError) {
      status.hidden = false;
      status.textContent = text;
      status.classList.toggle("is-error", !!isError);
    }
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var data = {};
      new FormData(form).forEach(function (v, k) { data[k] = String(v); });
      data.t = String(Date.now() - started);
      button.disabled = true;
      fetch(form.action, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
      }).then(function (r) {
        if (!r.ok) throw new Error(String(r.status));
        form.reset();
        show(MSG_SENT, false);
      }).catch(function () {
        show(MSG_ERROR + " " + EMAIL + ".", true);
      }).then(function () { button.disabled = false; });
    });
  })();
</script>
</body>
</html>
"""


def script():
    f = CONTACT["form"]
    return (SCRIPT.replace("__MSG_SENT__", json.dumps(f["sent"], ensure_ascii=False))
                  .replace("__MSG_ERROR__", json.dumps(f["error"], ensure_ascii=False))
                  .replace("__EMAIL__", json.dumps(EMAIL)))


def page(title, description, path, main):
    return head(title, description, path) + header() + main + footer() + script()


def section(id_, kicker, question, inner, intro=None):
    intro_html = f'\n      <p class="section-intro prose-measure">{e(intro)}</p>' if intro else ""
    return f"""
  <section id="{id_}" class="section reveal">
    <div class="container">
      <p class="kicker">{e(kicker)}</p>
      <h2 class="section-question">{e(question)}</h2>{intro_html}
{inner}
    </div>
  </section>
"""


def badge(work):
    cls = "badge badge--filled" if work.get("filled") else "badge"
    note = f'<span class="badge-note">{e(work["note"])}</span>' if work.get("note") else ""
    return f'<span class="badge-group"><span class="{cls}">{e(work["badge"])}</span>{note}</span>'


def case_href(work):
    return f"/lavori/{work['slug']}/"


def work_card(work):
    external = ""
    if work.get("external"):
        href, label = work["external"]
        external = f'\n            <a href="{href}" target="_blank" rel="noopener noreferrer" class="work-card__external" aria-label="{e(label)} — apri in nuova scheda">{e(label)} <span aria-hidden="true">&#8599;</span></a>'
    return f"""        <div class="card work-card">
          <a href="{case_href(work)}" class="work-card__stretched-link" aria-label="{e(work["name"])} — {e(WORKS["view_case"])}"></a>
          {badge(work)}
          <p class="kicker work-card__category">{e(work["category"])}</p>
          <h3 class="work-card__name">{e(work["name"])}</h3>
          <p class="work-card__challenge">{e(work.get("summary", work["challenge"]))}</p>
          <p class="work-card__outcome">{e(work["outcome"])}</p>
          <div class="work-card__footer">
            <span class="work-card__cta">{e(WORKS["view_case"])} <span aria-hidden="true">&rarr;</span></span>{external}
          </div>
        </div>"""


def faq_jsonld():
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in FAQ["items"]
        ],
    }
    return json.dumps(data, ensure_ascii=False)


def person_jsonld():
    data = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Alessandro Frau",
        "jobTitle": "Consulente di automazione e integrazioni",
        "worksFor": {"@type": "Organization", "name": "Frau Studio", "url": SITE_URL, "vatID": f"IT{VAT}"},
        "url": SITE_URL,
        "email": EMAIL,
        "address": {"@type": "PostalAddress", "addressLocality": "Milano", "addressCountry": "IT"},
        "sameAs": [GITHUB, LINKEDIN],
    }
    return json.dumps(data, ensure_ascii=False)


def visible_cases():
    return [w for w in WORKS["cases"] if not w.get("hidden")]


def case_by_slug(slug):
    return next(w for w in WORKS["cases"] if w["slug"] == slug)


def booking_href():
    if BOOKING_URL:
        return BOOKING_URL
    return f"mailto:{EMAIL}?subject=" + quote("Chiamata di 30 minuti sul mio processo")


def home():
    lines = []
    last = len(HERO["lines"]) - 1
    for i, line in enumerate(HERO["lines"]):
        text = f'<span class="hero__line-accent">{e(line)}</span>' if i == last else e(line)
        lines.append(f'          <span class="hero__line">{text}</span>')
    hero = f"""
<main>
  <script type="application/ld+json">{person_jsonld()}</script>
  <section id="top" class="hero">
    <div class="container">
      <div class="hero__frame">
        <h1 class="hero__heading">
{chr(10).join(lines)}
        </h1>
        <p class="hero__sub prose-measure">{e(HERO["sub"])}</p>
        <div class="hero__cta-row">
          <a href="{HERO["cta_primary_href"]}" class="btn btn-primary">{e(HERO["cta_primary"])}</a>
          <a href="{HERO["cta_secondary_href"]}" class="btn btn-secondary"><span class="btn-label">{e(HERO["cta_secondary"])}</span><span class="btn-arrow" aria-hidden="true">&rarr;</span></a>
        </div>
        <p class="hero__context caption"><strong>{e(HERO["context_strong"])}</strong> {e(HERO["context"])}</p>
      </div>
    </div>
  </section>
"""

    phases = "\n".join(f"""        <article class="method__phase">
          <p class="method__number">{n}</p>
          <h3>{e(t)}</h3>
          <p class="method__body">{e(b)}</p>
        </article>""" for n, t, b in METHOD["phases"])
    modes = "\n".join(f"""          <div class="method__engagement-card">
            <h3>{e(t)}</h3>
            <p>{e(b)}</p>
          </div>""" for t, b in METHOD["engagement"])
    method = section("metodo", METHOD["kicker"], METHOD["question"], f"""      <div class="method__phases">
{phases}
      </div>
      <div class="method__engagement">
        <p class="method__engagement-title">{e(METHOD["engagement_closing"])}</p>
        <div class="method__engagement-grid">
{modes}
        </div>
      </div>""", intro=METHOD["intro"])

    services = section("servizi", SERVICES["kicker"], SERVICES["question"], '      <div class="services__grid">\n' + "\n".join(f"""        <div class="method__engagement-card">
          <p class="service__pain">{e(p)}</p>
          <h3>{e(t)}</h3>
          <p>{e(b)}</p>
        </div>""" for p, t, b in SERVICES["items"]) + "\n      </div>")

    groups = []
    for title, desc, slugs in WORKS["groups"]:
        groups.append(f"""      <div class="works__group">
        <div class="works__group-head">
          <h3 class="works__group-title">{e(title)}</h3>
          <p class="works__group-desc">{e(desc)}</p>
        </div>
        <div class="works__grid{" works__grid--3" if len(slugs) == 3 else ""}">
{chr(10).join(work_card(case_by_slug(s)) for s in slugs)}
        </div>
      </div>""")
    lab_rows = "\n".join(f"""          <a href="{case_href(w)}" class="lab__row">
            <span class="lab__name">{e(w["name"])}</span>
            <span class="lab__desc">{e(w["lab_line"])}</span>
            <span class="lab__status">{e(w["badge"])}{(" · " + e(w["note"])) if w.get("note") else ""}</span>
          </a>""" for w in visible_cases() if w.get("lab"))
    works = section("lavori", WORKS["kicker"], WORKS["question"], f"""      <p class="works__transparency prose-measure caption">{e(WORKS["transparency"])}</p>
{chr(10).join(groups)}
      <div class="lab">
        <div class="lab__head">
          <h3 class="works__group-title">{e(WORKS["lab_title"])}</h3>
          <p class="works__group-desc">{e(WORKS["lab_desc"])}</p>
        </div>
        <div class="lab__list">
{lab_rows}
        </div>
      </div>""")

    trust = section("affidabilita", TRUST["kicker"], TRUST["question"], '      <div class="trust__grid">\n' + "\n".join(f"""        <div class="method__engagement-card">
          <h3>{e(t)}</h3>
          <p>{e(b)}</p>
        </div>""" for t, b in TRUST["items"]) + "\n      </div>", intro=TRUST["intro"])

    about_p = "\n".join(f'          <p class="prose-measure">{e(p)}</p>' for p in ABOUT["paragraphs"])
    about_links = "\n".join(f'            <a href="{h}" class="about__link">{e(l)} <span aria-hidden="true">&rarr;</span></a>' for l, h in ABOUT["links"])
    about = section("chi-sono", ABOUT["kicker"], ABOUT["question"], f"""      <div class="about__layout">
        <img class="about__photo" src="/assets/alessandro-frau.webp" alt="{e(ABOUT["photo_alt"])}" width="800" height="800" loading="lazy" decoding="async">
        <div class="about__content">
{about_p}
          <div class="about__links">
{about_links}
          </div>
        </div>
      </div>""")

    agency_items = "\n".join(f"""          <div class="agency__item">
            <h3>{e(t)}</h3>
            <p>{e(b)}</p>
          </div>""" for t, b in AGENCY["items"])
    agency = f"""
  <section id="agenzie" class="agency">
    <div class="container agency__inner">
      <p class="kicker">{e(AGENCY["kicker"])}</p>
      <h2 class="section-question">{e(AGENCY["question"])}</h2>
      <p class="section-intro prose-measure">{e(AGENCY["intro"])}</p>
      <div class="agency__grid">
{agency_items}
      </div>
      <div class="agency__cta"><a href="/#contatto" class="btn btn-outline">{e(AGENCY["cta"])}</a></div>
    </div>
  </section>
"""

    cards = []
    for title, href in WRITING["cards"]:
        if href:
            cards.append(f'        <a href="{href}" class="card writing__card"><h3>{e(title)}</h3></a>')
        else:
            cards.append(f"""        <div class="card writing__card writing__card--soon">
          <h3>{e(title)}</h3>
          <span class="badge">{e(WRITING["soon_label"])}</span>
        </div>""")
    writing = "" if not any(href for _, href in WRITING["cards"]) else section("scrittura", WRITING["kicker"], WRITING["question"], '      <div class="writing__grid">\n' + "\n".join(cards) + "\n      </div>")

    items = "\n".join(f"""        <details class="faq__item">
          <summary class="faq__question"><span>{e(q)}</span><span class="faq__icon" aria-hidden="true"></span></summary>
          <p class="faq__answer prose-measure">{e(a)}</p>
        </details>""" for q, a in FAQ["items"])
    faq = section("faq", FAQ["kicker"], FAQ["question"], f"""      <div class="faq__list">
{items}
      </div>
      <script type="application/ld+json">{faq_jsonld()}</script>""")

    f = CONTACT["form"]
    steps = "\n".join(f"""        <div class="contact__step">
          <h3>{e(t)}</h3>
          <p>{e(b)}</p>
        </div>""" for t, b in CONTACT["steps"])
    contact = section("contatto", CONTACT["kicker"], CONTACT["question"], f"""      <p class="prose-measure contact__body">{e(CONTACT["body"])}</p>
      <div class="contact__steps">
{steps}
      </div>
      <div class="contact__layout">
        <form class="contact-form" id="contact-form" action="{FORM_ENDPOINT}" method="post" novalidate>
          <div class="field">
            <label for="f-problema">{e(f["problema"][0])}</label>
            <textarea id="f-problema" name="problema" rows="5" required minlength="10" maxlength="5000" placeholder="{e(f["problema"][1])}"></textarea>
          </div>
          <div class="field">
            <label for="f-strumenti">{e(f["strumenti"][0])} <span class="field__optional">(facoltativo)</span></label>
            <input id="f-strumenti" name="strumenti" type="text" maxlength="500" placeholder="{e(f["strumenti"][1])}">
          </div>
          <div class="contact-form__row">
            <div class="field">
              <label for="f-nome">{e(f["nome"])}</label>
              <input id="f-nome" name="nome" type="text" required maxlength="200" autocomplete="name">
            </div>
            <div class="field">
              <label for="f-email">{e(f["email"])}</label>
              <input id="f-email" name="email" type="email" required maxlength="200" autocomplete="email">
            </div>
          </div>
          <div class="field field--trap" aria-hidden="true">
            <label for="f-sito">Sito web</label>
            <input id="f-sito" name="sito" type="text" tabindex="-1" autocomplete="off">
          </div>
          <input type="hidden" name="t" value="">
          <div class="contact-form__foot">
            <button type="submit" class="btn btn-primary">{e(f["submit"])}</button>
            <p class="caption">{e(f["reply_time"])}</p>
          </div>
          <p class="caption contact-form__privacy">{e(f["privacy"])}<a href="/privacy/">informativa privacy</a>.</p>
          <p class="contact-form__status" role="status" aria-live="polite" hidden></p>
        </form>
        <div class="contact__side">
          <div class="contact__block">
            <h3>{e(CONTACT["call_title"])}</h3>
            <p>{e(CONTACT["call_body"])}</p>
            <a href="{booking_href()}" class="btn btn-outline"{' target="_blank" rel="noopener noreferrer"' if BOOKING_URL else ''}>{e(CONTACT["call_cta"])}</a>
          </div>
          <div class="contact__block">
            <h3>{e(CONTACT["mail_title"])}</h3>
            <a href="mailto:{EMAIL}" class="contact__mail">{EMAIL}</a>
            <div class="contact__links">
              <a href="{LINKEDIN}" class="contact__link">LinkedIn</a>
              <a href="{GITHUB}" class="contact__link">GitHub</a>
            </div>
          </div>
        </div>
      </div>""")

    main = hero + method + services + works + trust + about + agency + writing + faq + contact + "</main>\n"
    return page(META["title"], META["description"], "/", main)


def case_page(work):
    points = ""
    if work.get("points"):
        points = '\n              <ul class="case-study__points">\n' + "\n".join(
            f"                <li><strong>{e(s)}</strong> {e(t)}</li>" for s, t in work["points"]
        ) + "\n              </ul>"
    external = ""
    if work.get("external"):
        href, label = work["external"]
        external = f'\n    <a href="{href}" target="_blank" rel="noopener noreferrer" class="case-study__external">{e(label)} <span aria-hidden="true">&#8599;</span></a>'
    main = f"""
<main class="case-study">
  <div class="container case-study__inner">
    <a href="/#lavori" class="case-study__back">&larr; {e(WORKS["question"])}</a>
    <div class="case-study__badge">{badge(work)}</div>
    <p class="kicker case-study__category">{e(work["category"])}</p>
    <h1 class="case-study__title">{e(work["name"])}</h1>

    <dl class="case-study__body">
      <div class="case-study__block">
        <dt class="kicker">Sfida</dt>
        <dd class="prose-measure">{e(work["challenge"])}</dd>
      </div>
      <div class="case-study__block">
        <dt class="kicker">Intervento</dt>
        <dd class="prose-measure">{e(work["intervention"])}{points}
        </dd>
      </div>
      <div class="case-study__block case-study__block--outcome">
        <dt class="kicker">Esito</dt>
        <dd class="case-study__outcome">{e(work["outcome"])}</dd>
      </div>
    </dl>

    <p class="caption case-study__stack">Stack: {e(work["stack"])}</p>{external}

    <div class="case-study__cta">
      <h2>{e(CONTACT["question"])}</h2>
      <a href="/#contatto" class="btn btn-primary">{e(NAV["cta"])} &rarr;</a>
    </div>
  </div>
</main>
"""
    return page(f"{work['name']} — Frau Studio", work["challenge"], case_href(work), main)


def not_found():
    main = f"""
<main class="container not-found">
  <p class="kicker">404</p>
  <h1>{e(NOT_FOUND["title"])}</h1>
  <p class="not-found__body">{e(NOT_FOUND["body"])}</p>
  <a href="/" class="btn btn-secondary"><span class="btn-arrow" aria-hidden="true">&larr;</span><span class="btn-label">{e(NOT_FOUND["cta"])}</span></a>
</main>
"""
    return page(f"{NOT_FOUND['title']} — Frau Studio", NOT_FOUND["body"], "/404.html", main)


def privacy():
    blocks = "\n".join(f"""      <div class="case-study__block">
        <h2 class="privacy__heading">{e(t)}</h2>
        <p class="prose-measure">{e(b)}</p>
      </div>""" for t, b in PRIVACY["sections"])
    main = f"""
<main class="case-study">
  <div class="container case-study__inner">
    <a href="/" class="case-study__back">&larr; Torna alla home</a>
    <h1 class="case-study__title privacy__title">{e(PRIVACY["title"])}</h1>
    <p class="caption privacy__updated">{e(PRIVACY["updated"])}</p>
    <div class="case-study__body">
{blocks}
    </div>
  </div>
</main>
"""
    return page(f"{PRIVACY['title']} — Frau Studio", "Come Frau Studio tratta i dati inviati dal modulo di contatto.", "/privacy/", main)


def sitemap():
    urls = ["/"] + [case_href(w) for w in visible_cases()] + ["/privacy/"]
    body = "\n".join(f"  <url><loc>{SITE_URL}{u}</loc></url>" for u in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n'


def write(rel, text):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print("scritto", rel)


if __name__ == "__main__":
    write("index.html", home())
    write("404.html", not_found())
    for w in visible_cases():
        write(f"lavori/{w['slug']}/index.html", case_page(w))
    write("privacy/index.html", privacy())
    write("sitemap.xml", sitemap())
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
