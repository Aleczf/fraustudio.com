import { getContent } from "@/content";
import type { Locale } from "@/content/types";
import Section from "./Section";

// Sezione ABOUT: testo + slot foto (placeholder monogramma finché non c'è un
// ritratto vero) + link GitHub/LinkedIn.
export default function About({ locale = "it" }: { locale?: Locale }) {
  const { about } = getContent(locale);

  return (
    <Section id="chi-sono" kicker={about.kicker} question={about.question}>
      <div className="about__layout">
        <div
          className="about__photo"
          role="img"
          aria-label={about.photoAlt}
        >
          <span aria-hidden="true">{about.photoPlaceholder}</span>
        </div>

        <div className="about__content">
          <p className="prose-measure">{about.body}</p>
          <div className="about__links">
            {about.links.map((link) => (
              <a key={link.label} href={link.href} className="about__link">
                {link.label} <span aria-hidden="true">&rarr;</span>
              </a>
            ))}
          </div>
        </div>
      </div>
    </Section>
  );
}
