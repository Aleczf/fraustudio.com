import type { Locale, WorkCase } from "@/content/types";
import Card from "./Card";
import Badge from "./Badge";

// Card di un caso studio nella griglia LAVORI. L'intera card è cliccabile verso
// /lavori/[slug] (o /en/lavori/[slug]) tramite un "stretched link" (un <a> a
// copertura assoluta) invece di avvolgere tutto in un <a>: serve a poter
// ospitare, quando c'è, un secondo link reale (il sito esterno FERØ) senza
// annidare <a> dentro <a> (HTML invalido).
export default function WorkCard({
  work,
  viewCaseLabel,
  locale = "it",
}: {
  work: WorkCase;
  viewCaseLabel: string;
  locale?: Locale;
}) {
  const caseHref = locale === "en" ? `/en/lavori/${work.slug}` : `/lavori/${work.slug}`;
  const newTabLabel = locale === "en" ? "open in new tab" : "apri in nuova scheda";

  return (
    <Card className="work-card">
      <a href={caseHref} className="work-card__stretched-link" aria-label={`${work.name} — ${viewCaseLabel}`} />
      <Badge badge={work.badge} note={work.badgeNote} />
      <p className="kicker work-card__category">{work.category}</p>
      <h3 className="work-card__name">{work.name}</h3>
      <p className="work-card__challenge">{work.challenge}</p>
      <p className="work-card__outcome">{work.outcome}</p>
      <div className="work-card__footer">
        <span className="work-card__cta">
          {viewCaseLabel} <span aria-hidden="true">&rarr;</span>
        </span>
        {work.externalLink ? (
          <a
            href={work.externalLink.href}
            target="_blank"
            rel="noopener noreferrer"
            className="work-card__external"
            aria-label={`${work.externalLink.label} — ${newTabLabel}`}
          >
            {work.externalLink.label} <span aria-hidden="true">&#8599;</span>
          </a>
        ) : null}
      </div>
    </Card>
  );
}
