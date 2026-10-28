import { getContent } from "@/content";
import type { Locale } from "@/content/types";
import Section from "./Section";

// Sezione FAQ come <details>/<summary> accessibili (nativo, niente JS), con
// icona +/- ruotante in puro CSS. Aggiunge anche lo structured data FAQPage
// (JSON-LD) per la SEO.
export default function Faq({ locale = "it" }: { locale?: Locale }) {
  const { faq } = getContent(locale);

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: faq.items.map((item) => ({
      "@type": "Question",
      name: item.question,
      acceptedAnswer: {
        "@type": "Answer",
        text: item.answer,
      },
    })),
  };

  return (
    <Section id="faq" kicker={faq.kicker} question={faq.question}>
      <div className="faq__list">
        {faq.items.map((item) => (
          <details key={item.question} className="faq__item">
            <summary className="faq__question">
              <span>{item.question}</span>
              <span className="faq__icon" aria-hidden="true" />
            </summary>
            <p className="faq__answer prose-measure">{item.answer}</p>
          </details>
        ))}
      </div>

      {/* eslint-disable-next-line react/no-danger */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />
    </Section>
  );
}
