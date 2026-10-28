import { notFound } from "next/navigation";
import { getContent } from "@/content";
import type { Locale } from "@/content/types";
import Badge from "@/components/Badge";
import Button from "@/components/Button";

// Contenuto condiviso della pagina caso studio (Tranche 2, reso locale-aware
// in Tranche 4): usato sia da app/(it)/lavori/[slug] sia da app/en/lavori/[slug],
// così la struttura e i testi restano un'unica fonte di verità.
export default function CaseStudyContent({ slug, locale = "it" }: { slug: string; locale?: Locale }) {
  const { works, contact } = getContent(locale);
  const work = works.cases.find((item) => item.slug === slug);

  if (!work) {
    notFound();
  }

  const backHref = locale === "en" ? "/en#lavori" : "/#lavori";
  const contactHref = `mailto:${contact.email}`;

  return (
    <main className="case-study">
      <div className="container case-study__inner">
        <a href={backHref} className="case-study__back">
          &larr; {works.question}
        </a>

        <Badge badge={work.badge} note={work.badgeNote} />
        <p className="kicker case-study__category">{work.category}</p>
        <h1 className="case-study__title">{work.name}</h1>

        <dl className="case-study__body">
          <div className="case-study__block">
            <dt className="kicker">{work.challengeLabel}</dt>
            <dd className="prose-measure">{work.challenge}</dd>
          </div>

          <div className="case-study__block">
            <dt className="kicker">{work.interventionLabel}</dt>
            <dd className="prose-measure">{work.intervention}</dd>
          </div>

          <div className="case-study__block case-study__block--outcome">
            <dt className="kicker">{work.outcomeLabel}</dt>
            <dd className="case-study__outcome">{work.outcome}</dd>
          </div>
        </dl>

        <p className="caption case-study__stack">
          {work.stackLabel}: {work.stack}
        </p>

        {work.externalLink ? (
          <a
            href={work.externalLink.href}
            target="_blank"
            rel="noopener noreferrer"
            className="case-study__external"
          >
            {work.externalLink.label} <span aria-hidden="true">&#8599;</span>
          </a>
        ) : null}

        <div className="case-study__cta">
          <h2>{contact.question}</h2>
          <Button href={contactHref} variant="primary">
            {contact.closingLine}
          </Button>
        </div>
      </div>
    </main>
  );
}
