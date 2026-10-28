import { getContent } from "@/content";
import type { Locale } from "@/content/types";
import Section from "./Section";

// Sezione METODO: tre fasi (ENTRO/CAPISCO/COSTRUISCO) con numerazione grande
// in Fraunces, poi le tre formule di ingaggio come mini-card sobrie.
export default function Method({ locale = "it" }: { locale?: Locale }) {
  const { method } = getContent(locale);

  return (
    <Section id="metodo" kicker={method.kicker} question={method.question} intro={method.intro}>
      <div className="method__phases">
        {method.phases.map((phase) => (
          <article key={phase.number} className="method__phase">
            <p className="method__number">{phase.number}</p>
            <h3>{phase.title}</h3>
            <p className="method__body">{phase.body}</p>
          </article>
        ))}
      </div>

      <div className="method__engagement">
        <p className="method__engagement-title">{method.engagementClosing}</p>
        <div className="method__engagement-grid">
          {method.engagementModes.map((mode) => (
            <div key={mode.title} className="method__engagement-card">
              <h3>{mode.title}</h3>
              <p>{mode.body}</p>
            </div>
          ))}
        </div>
      </div>
    </Section>
  );
}
