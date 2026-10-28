export type Locale = "it" | "en";

export type WorkBadge =
  | "CLIENTE REALE"
  | "REAL CLIENT"
  | "CONCEPT DIMOSTRATIVO"
  | "DEMO CONCEPT"
  | "PRODOTTO"
  | "PRODUCT"
  | "IN COSTRUZIONE"
  | "IN PROGRESS";

export interface WorkCase {
  slug: string;
  badge: WorkBadge;
  badgeNote?: string; // es. "il codice è vero"
  name: string;
  category: string;
  challengeLabel: string;
  challenge: string;
  interventionLabel: string;
  intervention: string;
  outcomeLabel: string;
  outcome: string;
  stackLabel: string;
  stack: string;
  externalLink?: { href: string; label: string };
}

export interface NavContent {
  brand: string;
  links: { label: string; href: string }[];
  cta: string;
  langSwitchLabel: string;
}

export interface HeroContent {
  kicker: string;
  headingLines: string[];
  sub: string;
  ctaPrimary: string;
  ctaPrimaryHref: string;
  ctaSecondary: string;
  ctaSecondaryHref: string;
}

export interface MethodPhase {
  number: string;
  title: string;
  body: string;
}

export interface MethodContent {
  kicker: string;
  question: string;
  intro: string;
  phases: MethodPhase[];
  engagementClosing: string;
  engagementModes: { title: string; body: string }[];
}

export interface WorksContent {
  kicker: string;
  question: string;
  transparencyNote: string;
  cases: WorkCase[];
  viewCaseLabel: string;
}

export interface AboutContent {
  kicker: string;
  question: string;
  body: string;
  photoAlt: string;
  photoPlaceholder: string;
  links: { label: string; href: string }[];
}

export interface WritingCard {
  title: string;
  href?: string;
  comingSoon?: boolean;
}

export interface WritingContent {
  kicker: string;
  question: string;
  cards: WritingCard[];
  comingSoonLabel: string;
}

export interface FaqItem {
  question: string;
  answer: string;
}

export interface FaqContent {
  kicker: string;
  question: string;
  items: FaqItem[];
}

export interface ContactContent {
  kicker: string;
  question: string;
  body: string;
  emailLabel: string;
  email: string;
  linkedinLabel: string;
  linkedinHref: string;
  githubLabel: string;
  githubHref: string;
  closingLine: string;
}

export interface FooterContent {
  identity: string;
  vatLabel: string;
  vat: string;
  location: string;
  year: string;
  voiceLine: string;
}

export interface DiagnoserContent {
  title: string;
  sub: string;
  placeholder: string;
  button: string;
  buttonLoading: string;
  disclaimer: string;
  ctaAfterOutput: string;
  charLimitLabel: string;
  loadingPhrases: string[];
  comingSoonLabel: string;
  errorFallback: string;
  bottleneckLabel: string;
  approachLabel: string;
  magnitudeLabel: string;
}

export interface ContextBarContent {
  text: string;
}

export interface NotFoundContent {
  title: string;
  body: string;
  cta: string;
}

export interface SiteContent {
  locale: Locale;
  meta: {
    title: string;
    description: string;
  };
  nav: NavContent;
  hero: HeroContent;
  contextBar: ContextBarContent;
  method: MethodContent;
  works: WorksContent;
  about: AboutContent;
  writing: WritingContent;
  faq: FaqContent;
  contact: ContactContent;
  footer: FooterContent;
  diagnoser: DiagnoserContent;
  notFound: NotFoundContent;
}
