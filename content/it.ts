import type { SiteContent } from "./types";

export const it: SiteContent = {
  locale: "it",
  meta: {
    title: "Alessandro Frau — AI Process Engineering",
    description:
      "Le più grandi aziende tech stanno investendo miliardi in ingegneri che costruiscono dentro i processi dei clienti. Io porto lo stesso metodo alle aziende reali italiane.",
  },
  nav: {
    brand: "Alessandro Frau",
    links: [
      { label: "Metodo", href: "/#metodo" },
      { label: "Lavori", href: "/#lavori" },
      { label: "Chi sono", href: "/#chi-sono" },
      { label: "Scrittura", href: "/#scrittura" },
    ],
    cta: "Descrivimi un processo",
    langSwitchLabel: "EN",
  },
  hero: {
    kicker: "AI PROCESS ENGINEERING · MILANO",
    headingLines: ["Non un'agenzia.", "Non un dipendente.", "Non il solito freelance."],
    sub: "Entro nei processi della tua azienda e costruisco l'automazione che serve — in giorni, non in trimestri. Analisi sul campo, AI dove conviene davvero, soluzioni che il tuo team sa mantenere.",
    ctaPrimary: "Descrivimi un processo →",
    ctaPrimaryHref: "/#diagnoser",
    ctaSecondary: "Guarda come lavoro",
    ctaSecondaryHref: "/#metodo",
  },
  contextBar: {
    text: "Le più grandi aziende tech stanno investendo miliardi in ingegneri che costruiscono dentro i processi dei clienti. Io porto lo stesso metodo alle aziende reali italiane.",
  },
  method: {
    kicker: "METODO",
    question: "Come lavoro?",
    intro: "Tre fasi, sempre le stesse. Cambia solo il tuo processo.",
    phases: [
      {
        number: "01",
        title: "Entro",
        body: "Mi siedo dove il lavoro succede davvero: il gestionale, le email, il foglio Excel delle 18:30. Otto anni nelle brigate di cucine stellate mi hanno insegnato a leggere i sistemi di produzione sotto pressione: flussi, colli di bottiglia, cosa si rompe e perché.",
      },
      {
        number: "02",
        title: "Capisco",
        body: "Identifico dove l'automazione e l'AI convengono davvero — e dove no. Non ogni processo va automatizzato: alcuni vanno semplificati, altri lasciati alle persone. La diagnosi è il prodotto, non un preambolo.",
      },
      {
        number: "03",
        title: "Costruisco",
        body: "Sviluppo la soluzione su misura, dentro gli strumenti che già usi, e te la consegno in modo che il tuo team possa mantenerla. Quello che richiedeva quattro fornitori e mesi, oggi è una persona e qualche settimana.",
      },
    ],
    engagementClosing: "Mi ingaggi in tre modi:",
    engagementModes: [
      { title: "Diagnosi singola", body: "Una prima lettura del tuo processo, mirata e concreta." },
      { title: "Progetto chiuso", body: "Analisi e costruzione della soluzione, con consegna definita." },
      {
        title: "Fractional",
        body: "Presenza continuativa part-time, senza il costo di un'assunzione.",
      },
    ],
  },
  works: {
    kicker: "LAVORI",
    question: "Cosa ho costruito?",
    transparencyNote:
      "Alcuni lavori sono per clienti reali, altri sono concept che ho costruito per dimostrare il metodo. È sempre indicato quale.",
    viewCaseLabel: "Leggi il caso",
    cases: [
      {
        slug: "vas-3",
        badge: "CLIENTE REALE",
        name: "VAS 3",
        category: "Automazione di processo · AI",
        challengeLabel: "Sfida",
        challenge:
          "Un ristorante affogava nella fatturazione passiva: ogni settimana, ore a smistare a mano fatture tra food, no-food e spese generali.",
        interventionLabel: "Intervento",
        intervention:
          "Sono entrato nel processo e ho costruito un sistema che classifica automaticamente ogni fattura con AI, dentro gli strumenti che il cliente già usava — così può mantenerlo senza dipendere da me. Scelta deliberata: la soluzione più semplice che regge, non la più sofisticata.",
        outcomeLabel: "Esito",
        outcome: "— ore a settimana recuperate. Classificazione automatica in produzione.",
        stackLabel: "Stack",
        stack: "Google Apps Script · Claude API",
      },
      {
        slug: "fero",
        badge: "CONCEPT DIMOSTRATIVO",
        badgeNote: "il codice è vero",
        name: "FERØ",
        category: "Sistema completo · AI · E-commerce",
        challengeLabel: "Sfida",
        challenge:
          "Una piccola impresa che vende un prodotto premium ha bisogno di vetrina credibile, scelta assistita, acquisizione contatti e back-office: di norma quattro fornitori diversi e settimane di coordinamento.",
        interventionLabel: "Intervento",
        intervention:
          "L'ho costruito intero, da solo: sito editoriale, advisor AI che abbina prodotto e occasione come farebbe un sommelier, flusso di prenotazione con conferma automatica, back-office che classifica gli ordini da sé.",
        outcomeLabel: "Esito",
        outcome: "Quattro fornitori, uno. Settimane, giorni.",
        stackLabel: "Stack",
        stack: "Next.js · Claude API · Vercel",
        externalLink: { href: "https://fero-site.vercel.app", label: "fero-site.vercel.app" },
      },
      {
        slug: "sofia",
        badge: "PRODOTTO",
        name: "SOFIA",
        category: "Agente AI · WhatsApp",
        challengeLabel: "Sfida",
        challenge:
          "In ogni database aziendale dormono clienti che hanno già comprato e non sono mai tornati. Ricontattarli a mano non scala; non ricontattarli è fatturato perso.",
        interventionLabel: "Intervento",
        intervention:
          "Un agente AI su WhatsApp che riattiva i clienti dormienti: conversa in modo naturale, qualifica l'interesse e riporta all'acquisto o all'appuntamento. Il motore è generale; la personalità e il contesto si modulano sul settore del cliente.",
        outcomeLabel: "Esito",
        outcome: "Conversazioni 24/7 su un canale che in Italia ha tassi di apertura che l'email si sogna.",
        stackLabel: "Stack",
        stack: "Node.js · Claude API · WhatsApp · SQLite",
      },
      {
        slug: "nolo-hub",
        badge: "IN COSTRUZIONE",
        name: "NOLO HUB",
        category: "Piattaforma editoriale · Sistema agentico",
        challengeLabel: "Sfida",
        challenge: "Il mondo no/low alcohol cresce, ma in Italia nessuno lo racconta con profondità gastronomica.",
        interventionLabel: "Intervento",
        intervention:
          "Sto costruendo una piattaforma editoriale AI-native: pipeline di contenuto orchestrata da agenti con supervisione umana — gli agenti producono, le persone decidono. Architettura: nessun agente è mai responsabile ultimo; lo è sempre un umano.",
        outcomeLabel: "Esito",
        outcome: "In sviluppo. È il mio laboratorio a cielo aperto: quello che imparo qui finisce nei progetti dei clienti.",
        stackLabel: "Stack",
        stack: "Astro · TypeScript · n8n · Notion",
      },
    ],
  },
  about: {
    kicker: "CHI SONO",
    question: "Chi c'è dietro?",
    body: "Sono Alessandro. Prima di scrivere codice ho passato otto anni nelle cucine e nelle sale di ristoranti stellati, e sono sommelier AIS. In una brigata impari a leggere un sistema di produzione sotto pressione — flussi, ruoli, colli di bottiglia, cosa cede per primo quando il ritmo sale. È esattamente quello che faccio oggi nelle aziende: solo che ora, dopo la diagnosi, la soluzione la costruisco anch'io. Mi sono formato da autodidatta su sviluppo full-stack e AI, e in project management. Ho anche fondato un progetto deep-tech di autenticazione ottica per il vino, in fase di tutela della proprietà intellettuale. Vivo e lavoro a Milano.",
    photoAlt: "Ritratto di Alessandro Frau",
    photoPlaceholder: "A.",
    links: [
      { label: "GitHub", href: "https://github.com/Aleczf" },
      { label: "LinkedIn", href: "#" },
    ],
  },
  writing: {
    kicker: "SCRITTURA",
    question: "Cosa penso?",
    comingSoonLabel: "In arrivo",
    cards: [
      { title: "Liquid Gastronomy 2026", href: "#" },
      { title: "Quello che una brigata stellata insegna sui processi aziendali", comingSoon: true },
    ],
  },
  faq: {
    kicker: "FAQ",
    question: "Domande frequenti",
    items: [
      {
        question: "Che differenza c'è tra te e un'agenzia di automazione?",
        answer:
          "Un'agenzia ti vende il suo pacchetto. Io entro nel tuo processo, capisco cosa serve davvero — a volte è meno di quello che pensavi — e costruisco solo quello. E resto una persona sola: chi diagnostica è chi costruisce.",
      },
      {
        question: 'Cosa significa "fractional"?',
        answer:
          "Presenza continuativa part-time: un numero di ore o giornate al mese concordato, dentro il tuo team, senza il costo e il vincolo di un'assunzione. Mi prendi per il problema, non a tempo pieno.",
      },
      {
        question: "Lavori solo nel food & beverage?",
        answer:
          "No. Il metodo vale per qualsiasi azienda con processi ripetitivi: amministrazione, vendite, operations. Il food è dove ho vissuto più a lungo, quindi lì ho una marcia in più — ma i processi si somigliano più di quanto sembri.",
      },
      {
        question: "Che tecnologie usi?",
        answer:
          "Le più semplici che reggono il tuo caso. A volte è un foglio Google potenziato con AI, a volte un agente su WhatsApp, a volte un'applicazione completa. La tecnologia è una conseguenza della diagnosi, mai il punto di partenza.",
      },
      {
        question: "Quanto costa?",
        answer:
          "Dipende dal problema, non dal mio umore: dopo una prima conversazione ti do un prezzo chiuso o una tariffa chiara, con la manutenzione esplicitata a parte. Niente sorprese a consuntivo.",
      },
    ],
  },
  contact: {
    kicker: "CONTATTO",
    question: "Che processo ti rallenta?",
    body: "Descrivimelo in due righe. Ti dico come lo automatizzerei — e se non conviene automatizzarlo, ti dico anche quello.",
    emailLabel: "Email",
    email: "nome@dominio.it",
    linkedinLabel: "LinkedIn",
    linkedinHref: "#",
    githubLabel: "GitHub",
    githubHref: "https://github.com/Aleczf",
    closingLine: "30 minuti sul tuo processo, senza impegno.",
  },
  footer: {
    identity: "Alessandro Frau",
    vatLabel: "P.IVA",
    vat: "—",
    location: "Milano",
    year: "2026",
    voiceLine: "I concept sono inventati. Il codice è vero.",
  },
  diagnoser: {
    title: "Prova il metodo, adesso.",
    sub: "Descrivi un processo che ti porta via tempo. Ti restituisco una prima diagnosi: dove sta il collo di bottiglia, che approccio userei, quanto tempo potresti recuperare.",
    placeholder:
      'Es.: "Ogni lunedì passo due ore a copiare gli ordini dalle email in un Excel e a mandare conferme una per una…"',
    button: "Diagnostica →",
    buttonLoading: "Diagnostico…",
    disclaimer:
      "Questa è una prima lettura automatica, non una consulenza. La diagnosi vera si fa guardando il processo dal vivo — ed è il mio lavoro.",
    ctaAfterOutput: "Vuoi la diagnosi vera? Scrivimi →",
    charLimitLabel: "caratteri",
    loadingPhrases: ["Leggo il processo…", "Cerco il collo di bottiglia…", "Preparo la diagnosi…"],
    comingSoonLabel: "Presto attivo",
    errorFallback: "Il Diagnoser sta riposando — scrivimi direttamente.",
    bottleneckLabel: "Il collo di bottiglia",
    approachLabel: "L'approccio",
    magnitudeLabel: "Ordine di grandezza",
  },
  notFound: {
    title: "Questa pagina non esiste.",
    body: "Il metodo sì.",
    cta: "← Torna alla home",
  },
};
