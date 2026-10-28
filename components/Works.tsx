import { getContent } from "@/content";
import type { Locale } from "@/content/types";
import Section from "./Section";
import WorkCard from "./WorkCard";

// Sezione LAVORI: griglia 2x2 (desktop) / colonna (mobile) delle 4 card caso.
export default function Works({ locale = "it" }: { locale?: Locale }) {
  const { works } = getContent(locale);

  return (
    <Section id="lavori" kicker={works.kicker} question={works.question}>
      <p className="works__transparency prose-measure caption">{works.transparencyNote}</p>
      <div className="works__grid">
        {works.cases.map((work) => (
          <WorkCard key={work.slug} work={work} viewCaseLabel={works.viewCaseLabel} locale={locale} />
        ))}
      </div>
    </Section>
  );
}
