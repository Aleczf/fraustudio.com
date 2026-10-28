import { getContent } from "@/content";
import type { Locale } from "@/content/types";
import Section from "./Section";

// Sezione CONTATTO: domanda H2, testo, mailto + link, riga finale "30 minuti".
export default function Contact({ locale = "it" }: { locale?: Locale }) {
  const { contact } = getContent(locale);

  return (
    <Section id="contatto" kicker={contact.kicker} question={contact.question}>
      <p className="prose-measure contact__body">{contact.body}</p>

      <div className="contact__links">
        <a href={`mailto:${contact.email}`} className="contact__link contact__link--primary">
          {contact.emailLabel}: {contact.email}
        </a>
        <a href={contact.linkedinHref} className="contact__link">
          {contact.linkedinLabel}
        </a>
        <a href={contact.githubHref} className="contact__link">
          {contact.githubLabel}
        </a>
      </div>

      <p className="contact__closing caption">{contact.closingLine}</p>
    </Section>
  );
}
