#!/usr/bin/env python3
"""Genera le pagine statiche di fraustudio.com.

Testi e struttura stanno qui (equivalente di content/it.ts del portfolio Next.js);
lo stile sta in assets/style.css. Dopo una modifica:

    python3 scripts/build.py

e committa i file generati: index.html, 404.html, lavori/<slug>/index.html, sitemap.xml.
"""
from html import escape
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent.parent
CSS_VERSION = hashlib.sha256((ROOT / "assets/style.css").read_bytes()).hexdigest()[:10]
FONTS_VERSION = hashlib.sha256((ROOT / "assets/fonts.css").read_bytes()).hexdigest()[:10]
SITE_URL = "https://fraustudio.com"
EMAIL = "alessandro.frau88@gmail.com"
GITHUB = "https://github.com/Aleczf"
LINKEDIN = "https://www.linkedin.com/in/alessandro-frau-095b60153/"
VAT = "14815310967"

# Statistiche senza cookie (Umami sulla VPS). Finché UMAMI_WEBSITE_ID è vuoto lo script non viene caricato.
UMAMI_SRC = "https://stats.fraustudio.com/script.js"
UMAMI_WEBSITE_ID = ""

META = {
    "title": "Frau Studio · Alessandro Frau, AI Process Engineering",
    "description": "Entro nei processi delle PMI e costruisco l'automazione che serve: integrazioni su misura, Odoo, dashboard con AI e agenti WhatsApp. Milano, ibrido o remoto.",
}

NAV = {
    "brand": "Frau Studio",
    "links": [
        ("Metodo", "/#metodo"),
        ("Servizi", "/#servizi"),
        ("Lavori", "/#lavori"),
        ("Chi sono", "/#chi-sono"),
    ],
    "cta": "Descrivimi un processo",
    "cta_href": "/#contatto",
}

HERO = {
    "lines": ["Non un'agenzia.", "Non un dipendente.", "Non il solito freelance."],
    "sub": "Entro nei processi della tua azienda e costruisco l'automazione che serve, in giorni e non in trimestri. Analisi sul campo, AI dove conviene davvero, soluzioni che il tuo team sa mantenere.",
    "cta_primary": "Descrivimi un processo →",
    "cta_primary_href": "/#contatto",
    "cta_secondary": "Guarda come lavoro",
    "cta_secondary_href": "/#metodo",
    "context": "Le più grandi aziende tech stanno investendo miliardi in ingegneri che costruiscono dentro i processi dei clienti. Io porto lo stesso metodo alle aziende reali italiane.",
}

METHOD = {
    "kicker": "METODO",
    "question": "Come lavoro?",
    "intro": "Tre fasi, sempre le stesse. Cambia solo il tuo processo.",
    "phases": [
        ("01", "Entro", "Mi siedo dove il lavoro succede davvero: il gestionale, le email, il foglio Excel delle 18:30. Prima di proporre qualcosa guardo come il processo regge sotto pressione: flussi, colli di bottiglia, cosa si rompe e perché."),
        ("02", "Capisco", "Identifico dove l'automazione e l'AI convengono davvero, e dove no. Non ogni processo va automatizzato: alcuni vanno semplificati, altri lasciati alle persone. La diagnosi è il prodotto, non un preambolo."),
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
    "items": [
        ("Integrazioni su misura", "Collego gestionali, piattaforme di settore, e-commerce e canali di messaggistica via API, con scritture senza doppioni e riallineamenti automatici."),
        ("Dashboard con AI", "Cruscotti costruiti sui dati che l'azienda ha già, con modelli linguistici che classificano, analizzano e smistano al posto delle persone."),
        ("Odoo", "Moduli personalizzati, configurazione e migrazioni da ERP proprietari."),
        ("Agenti WhatsApp", "Agenti che conversano con clienti e team su WhatsApp, vocali compresi, e scrivono nei sistemi aziendali."),
    ],
}

# Un caso: badge (+ nota), categoria, nome, sfida, intervento (+ punti), esito, stack, link esterno.
# "filled": solo i lavori con un cliente reale hanno il badge pieno.
WORKS = {
    "kicker": "LAVORI",
    "question": "Cosa ho costruito?",
    "transparency": "Alcuni lavori sono per clienti reali, altri sono prodotti miei o concept che ho costruito per dimostrare il metodo. È sempre indicato quale, insieme a dove si trova oggi il progetto.",
    "view_case": "Leggi il caso",
    "cases": [
        {
            "slug": "controllo-costi-ristorante",
            "summary": "Ore ogni settimana a smistare a mano le fatture passive, senza sapere quanto pesassero davvero food e beverage.",
            "badge": "CLIENTE REALE", "filled": True, "note": "in produzione",
            "name": "Controllo costi per un ristorante",
            "category": "Ristorazione · Controllo di gestione · AI",
            "challenge": "Un ristorante affogava nella fatturazione passiva: ogni settimana, ore a smistare a mano fatture tra food, no-food e spese generali. E il titolare decideva gli acquisti senza conoscere il peso reale di alimenti e bevande: i dati c'erano, chiusi negli XML delle fatture elettroniche.",
            "intervention": "Sono entrato nel processo e ho costruito un sistema che legge le fatture FatturaPA, classifica ogni riga per centro di costo e mostra costi e margine in una dashboard, dentro gli strumenti che il cliente già usava, così può mantenerlo senza dipendere da me. Un modello linguistico classifica solo i prodotti nuovi; gli altri arrivano dal catalogo. I limiti di Apps Script sono diventati scelte di progetto:",
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
            "summary": "Nei CRM dormono contatti che hanno già chiesto un preventivo o comprato. Nessuno li ricontatta.",
            "badge": "PRODOTTO", "note": "in produzione",
            "name": "Pico",
            "category": "Agente AI · WhatsApp · Riattivazione clienti",
            "challenge": "In ogni CRM dormono contatti che hanno chiesto un preventivo o comprato una volta, poi sono spariti. Ricontattarli a mano non scala; non ricontattarli è fatturato perso.",
            "intervention": "Pico è un mio prodotto: un agente AI che scrive su WhatsApp ai contatti fermi nel CRM, porta avanti la conversazione in modo naturale, capisce anche i vocali e passa all'attività chi è pronto a comprare o prenotare. Il motore è generale; la personalità e il contesto si modulano sul settore del cliente.",
            "points": [
                ("API ufficiali di Meta.", "Integrazione diretta con WhatsApp Cloud API, trascrizione dei vocali, stato delle conversazioni persistito."),
                ("Architettura riusabile.", "La sto adattando a un secondo caso d'uso: la reportistica dei team sul campo."),
            ],
            "outcome": "Il primo cliente ha registrato un aumento delle vendite dai lead tornati attivi.",
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
            "intervention": "Un modulo di intake su Odoo. Ogni richiesta viene registrata, analizzata da un modello linguistico e assegnata all'avvocato giusto. Una dashboard mostra tutto, e gli avvocati possono correggere l'assegnazione dalla dashboard o direttamente da WhatsApp.",
            "points": [
                ("Sopra Odoo, non accanto.", "Invece di un'app separata, Odoo con un'interfaccia alleggerita nei colori dello studio: CRM, firma degli incarichi e storico nello stesso posto."),
                ("Gli strumenti esistenti restano.", "Lo studio usava già un proprio assistente AI personalizzato e non voleva perderlo: la dashboard lo interroga."),
                ("Dati sensibili.", "L'infrastruttura gira su cloud dedicato, con la sicurezza come requisito di partenza."),
                ("Demo funzionante prima del contratto.", "Prototipo su Odoo in container con dati inventati, usato nella trattativa con lo studio."),
            ],
            "outcome": "Ogni richiesta registrata, analizzata e assegnata all'avvocato giusto.",
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
                ("MVP sullo stesso stack del prodotto finale,", "ripreso dal sistema di controllo costi per la ristorazione. Quello che il cliente prova è quello che riceverà."),
                ("Manutenibile senza teleassistenza.", "È un requisito di progetto. In valutazione il passaggio a un database PostgreSQL ospitato, con preventivo separato per hosting e manutenzione."),
            ],
            "outcome": "Ogni capo tracciabile fino al filato e al suo lotto.",
            "stack": "JavaScript · Google Apps Script · Google Sheets",
        },
        {
            "slug": "fero",
            "summary": "Vetrina, scelta assistita, contatti e back-office: di norma quattro fornitori e settimane di coordinamento.",
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
            "summary": "L'anticontraffazione per il vino chiede chip, RFID o etichette speciali che molte cantine non sostengono.",
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
            "badge": "IN COSTRUZIONE",
            "name": "NOLO HUB",
            "category": "Piattaforma editoriale · Sistema agentico",
            "challenge": "Il mondo no/low alcohol cresce, ma in Italia nessuno lo racconta con profondità gastronomica.",
            "intervention": "Sto costruendo una piattaforma editoriale AI-native: pipeline di contenuto orchestrata da agenti con supervisione umana: gli agenti producono, le persone decidono. Architettura: nessun agente è mai responsabile ultimo; lo è sempre un umano.",
            "outcome": "Il mio laboratorio a cielo aperto: quello che imparo qui finisce nei progetti dei clienti.",
            "stack": "Astro · TypeScript · n8n · Notion",
        },
        {
            "slug": "cold-outreach",
            "badge": "STRUMENTO INTERNO", "note": "in avvio",
            "name": "Cold outreach a costo quasi nullo",
            "category": "Lead generation B2B · Automazione",
            "challenge": "Lo stack tipico per trovare e contattare aziende costa 100-150 € al mese tra abbonamenti diversi.",
            "intervention": "Una pipeline che sostituisce tre abbonamenti con codice proprio, eseguita su job programmati. È pronta e in fase di avvio.",
            "points": [
                ("Ricerca delle aziende.", "Le attività di un territorio e di un settore arrivano dalla API di Google Places, al posto dei database a pagamento."),
                ("Messaggi personalizzati.", "Un modello linguistico leggero scrive l'apertura di ogni email a partire dai dati dell'azienda."),
                ("Esecuzione senza server.", "I job girano su GitHub Actions a orari fissi: niente macchina da mantenere accesa."),
                ("Reputazione protetta.", "Gli invii partono da un dominio dedicato, separato da quello principale, così un problema di consegna non tocca la posta di lavoro."),
            ],
            "outcome": "Da 100-150 € a 3-5 € al mese, stimati.",
            "stack": "Node.js · GitHub Actions · Google Places API · Claude API · Zoho Mail",
        },
    ],
}

ABOUT = {
    "kicker": "CHI SONO",
    "question": "Chi c'è dietro?",
    "photo_alt": "Ritratto di Alessandro Frau",
    "paragraphs": [
        "Sono Alessandro, e Frau Studio sono io. Il mio lavoro parte sempre dallo stesso punto: capire come un'azienda funziona davvero, chi fa cosa, dove i flussi si inceppano e cosa cede per primo quando il ritmo sale. Poi, fatta la diagnosi, la soluzione la costruisco io.",
        "Ho lavorato anche come tester su app e dispositivi mobili per piattaforme di crowdtesting internazionali. Da lì viene un'abitudine che porto in ogni progetto: chiedermi come un sistema si può rompere prima di consegnarlo.",
        "Il mio core è tecnico: sviluppo full-stack e AI, messi alla prova costruendo sistemi che oggi girano presso clienti reali. Lo completa una formazione specifica in Project Management & AI, che mi permette di guidare un progetto dall'analisi alla consegna: perimetro, tempi, rischi e persone coinvolte, non solo il codice. Ho anche fondato WineGuard, un progetto deep-tech di autenticazione ottica per il vino, in fase di tutela della proprietà intellettuale. Lavoro dentro i progetti di agenzie e software house, oppure direttamente con le PMI. Vivo e lavoro a Milano, in ibrido o da remoto; parlo italiano, inglese e francese.",
    ],
    "links": [("GitHub", GITHUB), ("LinkedIn", LINKEDIN)],
}

WRITING = {
    "kicker": "SCRITTURA",
    "question": "Cosa penso?",
    "soon_label": "In arrivo",
    # (titolo, href) — href None = "in arrivo"
    "cards": [
    ],
}

FAQ = {
    "kicker": "FAQ",
    "question": "Cosa mi chiedono più spesso?",
    "items": [
        ("Che differenza c'è tra te e un'agenzia di automazione?", "Un'agenzia ti vende il suo pacchetto. Io entro nel tuo processo, capisco cosa serve davvero (a volte è meno di quello che pensavi) e costruisco solo quello. E resto una persona sola: chi diagnostica è chi costruisce."),
        ("Lavori anche con agenzie e software house?", "Sì. Entro nei progetti di altri team per la parte Odoo, integrazioni e AI, oppure lavoro direttamente con il cliente. Il metodo è lo stesso: capire come l'azienda lavora davvero, scegliere lo strumento più semplice che regge, collegarlo a quello che c'è già."),
        ('Cosa significa "fractional"?', "Presenza continuativa part-time: un numero di ore o giornate al mese concordato, dentro il tuo team, senza il costo e il vincolo di un'assunzione. Mi prendi per il problema, non a tempo pieno."),
        ("Lavori con Odoo e con i gestionali che uso già?", "Sì. Su Odoo sviluppo moduli personalizzati, lo configuro e migro i dati da ERP proprietari. Se usi già un altro gestionale, un CRM o un e-commerce, lo collego via API agli altri strumenti (fatture elettroniche, WhatsApp, piattaforme di settore) con scritture senza doppioni e riallineamenti automatici. Spesso non serve cambiare sistema: serve farli parlare tra loro."),
        ("Che tecnologie usi?", "Le più semplici che reggono il tuo caso. A volte è un foglio Google potenziato con AI, a volte un agente su WhatsApp, a volte Odoo o un'applicazione completa. La tecnologia è una conseguenza della diagnosi, mai il punto di partenza."),
        ("Quanto costa?", "Dipende dal problema, non dal mio umore: dopo una prima conversazione ti do un prezzo chiuso o una tariffa chiara, con la manutenzione esplicitata a parte. Niente sorprese a consuntivo."),
    ],
}

CONTACT = {
    "kicker": "CONTATTO",
    "question": "Che processo ti rallenta?",
    "body": "Descrivimelo in due righe. Ti dico come lo automatizzerei. E se non conviene automatizzarlo, ti dico anche quello.",
    "closing": "30 minuti sul tuo processo, senza impegno.",
}

FOOTER = {
    "meta": ["Frau Studio · Alessandro Frau", f"P.IVA {VAT}", "Milano", "© 2026"],
}

NOT_FOUND = {"title": "Questa pagina non esiste.", "body": "Il metodo sì.", "cta": "Torna alla home"}


# ---------------------------------------------------------------------------
# Template
# ---------------------------------------------------------------------------
e = escape


def analytics():
    if not UMAMI_WEBSITE_ID:
        return ""
    return f'\n<script defer src="{UMAMI_SRC}" data-website-id="{UMAMI_WEBSITE_ID}" data-domains="fraustudio.com"></script>'


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
<link rel="preload" href="/assets/fonts/inter-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/fraunces-latin-standard-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/fonts.css?v={FONTS_VERSION}">
<link rel="stylesheet" href="/assets/style.css?v={CSS_VERSION}">{analytics()}
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
    meta += '\n      <span><a href="/privacy/">Privacy</a></span>'
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="site-footer__meta">
{meta}
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

    // Statistiche: conta i clic che contano (email, WhatsApp, LinkedIn, GitHub). Solo se Umami è attivo.
    document.addEventListener("click", function (ev) {
      var a = ev.target.closest && ev.target.closest("a[href]");
      if (!a || !window.umami) return;
      var h = a.getAttribute("href");
      var name = h.indexOf("mailto:") === 0 ? "clic-email"
        : h.indexOf("wa.me") > -1 ? "clic-whatsapp-demo"
        : h.indexOf("linkedin.com") > -1 ? "clic-linkedin"
        : h.indexOf("github.com") > -1 ? "clic-github" : null;
      if (name) window.umami.track(name);
    });

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
</script>
</body>
</html>
"""


def page(title, description, path, main):
    return head(title, description, path) + header() + main + footer() + SCRIPT


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
        external = f'\n            <a href="{href}" target="_blank" rel="noopener noreferrer" class="work-card__external" aria-label="{e(label)}, apri in nuova scheda">{e(label)} <span aria-hidden="true">&#8599;</span></a>'
    return f"""        <div class="card work-card">
          <a href="{case_href(work)}" class="work-card__stretched-link" aria-label="{e(work["name"])}: {e(WORKS["view_case"])}"></a>
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
        "jobTitle": "AI Process Engineer",
        "worksFor": {"@type": "Organization", "name": "Frau Studio", "url": SITE_URL, "vatID": f"IT{VAT}"},
        "url": SITE_URL,
        "email": EMAIL,
        "address": {"@type": "PostalAddress", "addressLocality": "Milano", "addressCountry": "IT"},
        "sameAs": [GITHUB, LINKEDIN],
    }
    return json.dumps(data, ensure_ascii=False)


def home():
    lines = []
    last = len(HERO["lines"]) - 1
    for i, line in enumerate(HERO["lines"]):
        text = f'<span class="hero__line-accent">{e(line)}</span>' if i == last else e(line)
        lines.append(f'        <span class="hero__line" style="animation-delay: {i * 120}ms">{text}</span>')
    hero = f"""
<main>
  <script type="application/ld+json">{person_jsonld()}</script>
  <section id="top" class="hero">
    <div class="container">
      <h1 class="hero__heading">
{chr(10).join(lines)}
      </h1>
      <p class="hero__sub prose-measure">{e(HERO["sub"])}</p>
      <div class="hero__cta-row">
        <a href="{HERO["cta_primary_href"]}" class="btn btn-primary">{e(HERO["cta_primary"])}</a>
        <a href="{HERO["cta_secondary_href"]}" class="btn btn-secondary"><span class="btn-label">{e(HERO["cta_secondary"])}</span><span class="btn-arrow" aria-hidden="true">&rarr;</span></a>
      </div>
      <p class="hero__context caption">{e(HERO["context"])}</p>
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
          <h3>{e(t)}</h3>
          <p>{e(b)}</p>
        </div>""" for t, b in SERVICES["items"]) + "\n      </div>")

    works = section("lavori", WORKS["kicker"], WORKS["question"], f"""      <p class="works__transparency prose-measure caption">{e(WORKS["transparency"])}</p>
      <div class="works__grid">
{chr(10).join(work_card(w) for w in WORKS["cases"])}
      </div>""")

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

    contact = section("contatto", CONTACT["kicker"], CONTACT["question"], f"""      <p class="prose-measure contact__body">{e(CONTACT["body"])}</p>
      <div class="contact__links">
        <a href="mailto:{EMAIL}" class="contact__link contact__link--primary">Email: {EMAIL}</a>
        <a href="{LINKEDIN}" class="contact__link">LinkedIn</a>
        <a href="{GITHUB}" class="contact__link">GitHub</a>
      </div>
      <p class="contact__closing caption">{e(CONTACT["closing"])}</p>""")

    main = hero + method + services + works + about + writing + faq + contact + "</main>\n"
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
      <a href="mailto:{EMAIL}" class="btn btn-primary">{e(CONTACT["closing"])}</a>
    </div>
  </div>
</main>
"""
    return page(f"{work['name']} · Frau Studio", work["challenge"], case_href(work), main)


def not_found():
    main = f"""
<main class="container not-found">
  <p class="kicker">404</p>
  <h1>{e(NOT_FOUND["title"])}</h1>
  <p class="not-found__body">{e(NOT_FOUND["body"])}</p>
  <a href="/" class="btn btn-secondary"><span class="btn-arrow" aria-hidden="true">&larr;</span><span class="btn-label">{e(NOT_FOUND["cta"])}</span></a>
</main>
"""
    return page(f"{NOT_FOUND['title']} · Frau Studio", NOT_FOUND["body"], "/404.html", main)


def privacy():
    analytics_text = (
        "Il sito usa Umami, uno strumento di statistica installato su un nostro server in Germania. "
        "Non usa cookie e non raccoglie dati che identificano il visitatore: registra in forma aggregata "
        "pagine visitate, sito di provenienza, tipo di dispositivo e i clic sui contatti. "
        "Questi dati servono solo a capire quali contenuti sono utili."
    ) if UMAMI_WEBSITE_ID else (
        "Il sito non usa strumenti di statistica né cookie di profilazione."
    )
    blocks = [
        ("Titolare del trattamento",
         f"Alessandro Frau (Frau Studio), Milano, P.IVA {VAT}. Contatto per qualsiasi richiesta sulla privacy: {EMAIL}."),
        ("Navigazione del sito",
         "Il sito è ospitato da GitHub Pages (GitHub Inc.), che per motivi tecnici e di sicurezza registra "
         "nei propri log l'indirizzo IP di chi lo visita. I font sono ospitati direttamente sul sito: "
         "nessuna richiesta viene inviata a Google o ad altri servizi esterni. "
         "Il sito non installa cookie, né tecnici né di profilazione: per questo non è presente un banner."),
        ("Statistiche", analytics_text),
        ("Contatti via email",
         "Se mi scrivi, uso il tuo indirizzo e quello che mi racconti solo per risponderti e, se lo chiedi, "
         "per preparare una proposta. Base giuridica: la tua richiesta e le misure precontrattuali "
         "(art. 6.1.b GDPR). Conservo la corrispondenza per il tempo necessario alla trattativa e, se diventi "
         "cliente, per gli obblighi di legge."),
        ("Demo di Pico su WhatsApp",
         "Se scrivi al numero della demo, Pico (un agente di intelligenza artificiale) tratta il tuo numero, "
         "il nome del tuo profilo WhatsApp e i messaggi che invii, per farti provare il servizio e, se lo chiedi, "
         "per ricontattarti. Base giuridica: la tua richiesta (art. 6.1.b GDPR). Le conversazioni della demo "
         "vengono cancellate automaticamente 30 giorni dopo l'ultimo messaggio. "
         "Per non ricevere più messaggi basta scrivere STOP."),
        ("Fornitori che trattano i dati",
         "Meta Platforms Ireland (WhatsApp Business Platform), per la consegna dei messaggi della demo. "
         "Anthropic PBC, che fornisce il modello di intelligenza artificiale usato da Pico: i testi delle "
         "conversazioni vengono elaborati sui suoi server negli Stati Uniti, sulla base delle clausole "
         "contrattuali standard della Commissione europea, e non vengono usati per addestrare i modelli. "
         "Hetzner Online GmbH (Germania), che ospita i server della demo e delle statistiche. "
         "GitHub Inc., che ospita il sito."),
        ("I tuoi diritti",
         f"Puoi chiedere in qualsiasi momento di accedere ai tuoi dati, correggerli, cancellarli, limitarne "
         f"il trattamento o opporti (artt. 15-22 GDPR), scrivendo a {EMAIL}. "
         "Hai anche il diritto di presentare reclamo al Garante per la protezione dei dati personali "
         "(garanteprivacy.it)."),
    ]
    body = "\n".join(
        f"""      <section class="legal__block">
        <h2>{e(t)}</h2>
        <p class="prose-measure">{e(p)}</p>
      </section>""" for t, p in blocks)
    main = f"""
<main class="legal">
  <div class="container legal__inner">
    <p class="kicker">Informativa</p>
    <h1 class="legal__title">Privacy</h1>
    <p class="caption">Ultimo aggiornamento: ottobre 2026</p>
{body}
  </div>
</main>
"""
    return page("Privacy · Frau Studio", "Come Frau Studio tratta i dati di chi visita il sito, scrive o prova la demo di Pico.", "/privacy/", main)


def sitemap():
    urls = ["/"] + [case_href(w) for w in WORKS["cases"]] + ["/privacy/"]
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
    write("privacy/index.html", privacy())
    for w in WORKS["cases"]:
        write(f"lavori/{w['slug']}/index.html", case_page(w))
    write("sitemap.xml", sitemap())
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
