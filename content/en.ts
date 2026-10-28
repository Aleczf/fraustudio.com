import type { SiteContent } from "./types";

// Traduzione EN — Tranche 4. Registro identico all'italiano: prima persona,
// diretto, zero corporate-speak. "Fractional" e "forward-deployed" restano in
// inglese (nel mercato anglofono sono termini riconosciuti e forti — vedi
// piano di orchestrazione). Non è una traduzione meccanica: alcune frasi sono
// riformulate per suonare naturali in inglese mantenendo lo stesso senso.
export const en: SiteContent = {
  locale: "en",
  meta: {
    title: "Alessandro Frau — AI Process Engineering",
    description:
      "The biggest tech companies are investing billions in engineers who build inside their clients' processes. I bring the same method to real Italian businesses.",
  },
  nav: {
    brand: "Alessandro Frau",
    links: [
      // Gli id di sezione restano gli stessi in entrambe le lingue (definiti
      // nei componenti Section): sono fragment identifier, non contenuto
      // visibile, quindi non li traduciamo per non dover parametrizzare ogni
      // componente. Vedi Method/Works/About/Writing per gli id reali.
      { label: "Method", href: "/en#metodo" },
      { label: "Work", href: "/en#lavori" },
      { label: "About", href: "/en#chi-sono" },
      { label: "Writing", href: "/en#scrittura" },
    ],
    cta: "Describe a process",
    langSwitchLabel: "IT",
  },
  hero: {
    kicker: "AI PROCESS ENGINEERING · MILAN",
    headingLines: ["Not an agency.", "Not an employee.", "Not another freelancer."],
    sub: "I get inside your company's processes and build the automation that's actually needed — in days, not quarters. Field analysis, AI where it genuinely pays off, solutions your team can maintain.",
    ctaPrimary: "Describe a process →",
    ctaPrimaryHref: "/en#diagnoser",
    ctaSecondary: "See how I work",
    ctaSecondaryHref: "/en#metodo",
  },
  contextBar: {
    text: "The biggest tech companies are investing billions in forward-deployed engineers who build inside their clients' processes. I bring the same method to real Italian businesses.",
  },
  method: {
    kicker: "METHOD",
    question: "How do I work?",
    intro: "Three phases, always the same. Only your process changes.",
    phases: [
      {
        number: "01",
        title: "I get in",
        body: "I sit where the work actually happens: the management software, the emails, the Excel sheet still open at 6:30pm. Eight years in Michelin-starred kitchen brigades taught me to read production systems under pressure: flows, bottlenecks, what breaks first and why.",
      },
      {
        number: "02",
        title: "I understand",
        body: "I identify where automation and AI genuinely pay off — and where they don't. Not every process should be automated: some need simplifying, others are best left to people. The diagnosis is the product, not a preamble.",
      },
      {
        number: "03",
        title: "I build",
        body: "I develop the solution tailored to you, inside the tools you already use, and hand it over so your team can maintain it. What used to take four vendors and months now takes one person and a few weeks.",
      },
    ],
    engagementClosing: "You can bring me in three ways:",
    engagementModes: [
      { title: "Single Diagnosis", body: "A first, targeted, concrete read of your process." },
      { title: "Fixed-scope project", body: "Analysis and build of the solution, with a defined delivery." },
      {
        title: "Fractional",
        body: "Ongoing part-time presence, without the cost of a hire.",
      },
    ],
  },
  works: {
    kicker: "WORK",
    question: "What have I built?",
    transparencyNote:
      "Some of this work is for real clients, some are concepts I built to demonstrate the method. It's always labeled which is which.",
    viewCaseLabel: "Read the case",
    cases: [
      {
        slug: "vas-3",
        badge: "REAL CLIENT",
        name: "VAS 3",
        category: "Process automation · AI",
        challengeLabel: "Challenge",
        challenge:
          "A restaurant was drowning in supplier invoices: every week, hours spent manually sorting them between food, non-food, and general expenses.",
        interventionLabel: "Intervention",
        intervention:
          "I got inside the process and built a system that automatically classifies every invoice with AI, inside the tools the client already used — so they can maintain it without depending on me. A deliberate choice: the simplest solution that holds up, not the most sophisticated one.",
        outcomeLabel: "Outcome",
        outcome: "— hours a week recovered. Automatic classification in production.",
        stackLabel: "Stack",
        stack: "Google Apps Script · Claude API",
      },
      {
        slug: "fero",
        badge: "DEMO CONCEPT",
        badgeNote: "the code is real",
        name: "FERØ",
        category: "Full system · AI · E-commerce",
        challengeLabel: "Challenge",
        challenge:
          "A small business selling a premium product needs a credible storefront, assisted selection, lead capture, and back-office — normally four different vendors and weeks of coordination.",
        interventionLabel: "Intervention",
        intervention:
          "I built the whole thing myself: an editorial website, an AI advisor that pairs product and occasion the way a sommelier would, a booking flow with automatic confirmation, a back-office that classifies orders on its own.",
        outcomeLabel: "Outcome",
        outcome: "Four vendors, one. Weeks, days.",
        stackLabel: "Stack",
        stack: "Next.js · Claude API · Vercel",
        externalLink: { href: "https://fero-site.vercel.app", label: "fero-site.vercel.app" },
      },
      {
        slug: "sofia",
        badge: "PRODUCT",
        name: "SOFIA",
        category: "AI agent · WhatsApp",
        challengeLabel: "Challenge",
        challenge:
          "Every company database has dormant customers who've already bought and never came back. Reaching out manually doesn't scale; not reaching out is lost revenue.",
        interventionLabel: "Intervention",
        intervention:
          "An AI agent on WhatsApp that reactivates dormant customers: it converses naturally, qualifies interest, and brings them back to a purchase or an appointment. The engine is general-purpose; personality and context are tuned to the client's industry.",
        outcomeLabel: "Outcome",
        outcome: "24/7 conversations on a channel that, in Italy, has open rates email can only dream of.",
        stackLabel: "Stack",
        stack: "Node.js · Claude API · WhatsApp · SQLite",
      },
      {
        slug: "nolo-hub",
        badge: "IN PROGRESS",
        name: "NOLO HUB",
        category: "Editorial platform · Agentic system",
        challengeLabel: "Challenge",
        challenge: "The no/low alcohol world is growing, but in Italy nobody covers it with real gastronomic depth.",
        interventionLabel: "Intervention",
        intervention:
          "I'm building an AI-native editorial platform: a content pipeline orchestrated by agents with human oversight — agents produce, people decide. Architecture: no agent is ever the final decision-maker; a human always is.",
        outcomeLabel: "Outcome",
        outcome: "In development. It's my living lab: what I learn here ends up in client projects.",
        stackLabel: "Stack",
        stack: "Astro · TypeScript · n8n · Notion",
      },
    ],
  },
  about: {
    kicker: "ABOUT",
    question: "Who's behind this?",
    body: "I'm Alessandro. Before writing code I spent eight years in the kitchens and dining rooms of Michelin-starred restaurants, and I'm an AIS-certified sommelier. In a brigade you learn to read a production system under pressure — flows, roles, bottlenecks, what gives first when the pace picks up. That's exactly what I do in companies today: except now, after the diagnosis, I build the solution too. I'm self-taught in full-stack development, AI, and project management. I also founded a deep-tech project on optical authentication for wine, currently in IP protection. I live and work in Milan.",
    photoAlt: "Portrait of Alessandro Frau",
    photoPlaceholder: "A.",
    links: [
      { label: "GitHub", href: "https://github.com/Aleczf" },
      { label: "LinkedIn", href: "#" },
    ],
  },
  writing: {
    kicker: "WRITING",
    question: "What do I think?",
    comingSoonLabel: "Coming soon",
    cards: [
      { title: "Liquid Gastronomy 2026", href: "#" },
      { title: "What a Michelin-starred brigade teaches about business processes", comingSoon: true },
    ],
  },
  faq: {
    kicker: "FAQ",
    question: "Frequently asked questions",
    items: [
      {
        question: "What's the difference between you and an automation agency?",
        answer:
          "An agency sells you its package. I get inside your process, figure out what's actually needed — sometimes it's less than you thought — and build only that. And I stay one person: whoever diagnoses is whoever builds.",
      },
      {
        question: 'What does "fractional" mean?',
        answer:
          "Ongoing part-time presence: an agreed number of hours or days per month, inside your team, without the cost and commitment of a hire. You bring me in for the problem, not full-time.",
      },
      {
        question: "Do you only work in food & beverage?",
        answer:
          "No. The method applies to any business with repeatable processes: admin, sales, operations. Food is where I spent the most time, so I have an edge there — but processes resemble each other more than you'd think.",
      },
      {
        question: "What technologies do you use?",
        answer:
          "The simplest ones that hold up for your case. Sometimes it's a Google Sheet powered by AI, sometimes a WhatsApp agent, sometimes a full application. Technology is a consequence of the diagnosis, never the starting point.",
      },
      {
        question: "How much does it cost?",
        answer:
          "It depends on the problem, not my mood: after an initial conversation I give you a fixed price or a clear rate, with maintenance spelled out separately. No surprises on the invoice.",
      },
    ],
  },
  contact: {
    kicker: "CONTACT",
    question: "What process is slowing you down?",
    body: "Describe it to me in two lines. I'll tell you how I'd automate it — and if it's not worth automating, I'll tell you that too.",
    emailLabel: "Email",
    email: "name@domain.com",
    linkedinLabel: "LinkedIn",
    linkedinHref: "#",
    githubLabel: "GitHub",
    githubHref: "https://github.com/Aleczf",
    closingLine: "30 minutes on your process, no strings attached.",
  },
  footer: {
    identity: "Alessandro Frau",
    vatLabel: "VAT",
    vat: "—",
    location: "Milan, Italy",
    year: "2026",
    voiceLine: "The concepts are invented. The code is real.",
  },
  diagnoser: {
    title: "Try the method, right now.",
    sub: "Describe a process that's costing you time. I'll give you a first diagnosis: where the bottleneck is, what approach I'd take, how much time you could get back.",
    placeholder:
      'E.g.: "Every Monday I spend two hours copying orders from emails into a spreadsheet and sending confirmations one by one…"',
    button: "Diagnose →",
    buttonLoading: "Diagnosing…",
    disclaimer:
      "This is a first automated read, not a consultation. The real diagnosis comes from looking at the process live — and that's my job.",
    ctaAfterOutput: "Want the real diagnosis? Write to me →",
    charLimitLabel: "characters",
    loadingPhrases: ["Reading the process…", "Looking for the bottleneck…", "Preparing the diagnosis…"],
    comingSoonLabel: "Coming online soon",
    errorFallback: "The Diagnoser is resting — write to me directly.",
    bottleneckLabel: "The bottleneck",
    approachLabel: "The approach",
    magnitudeLabel: "Order of magnitude",
  },
  notFound: {
    title: "This page doesn't exist.",
    body: "The method does.",
    cta: "← Back to home",
  },
};
