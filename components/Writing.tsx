import { getContent } from "@/content";
import type { Locale } from "@/content/types";
import Section from "./Section";
import Card from "./Card";

// Sezione SCRITTURA: due card orizzontali. La card "in arrivo" è presente ma
// non cliccabile (opacità ridotta, label dedicata).
export default function Writing({ locale = "it" }: { locale?: Locale }) {
  const { writing } = getContent(locale);

  return (
    <Section id="scrittura" kicker={writing.kicker} question={writing.question}>
      <div className="writing__grid">
        {writing.cards.map((card) =>
          card.comingSoon ? (
            <div key={card.title} className="card writing__card writing__card--soon">
              <h3>{card.title}</h3>
              <span className="badge">{writing.comingSoonLabel}</span>
            </div>
          ) : (
            <Card key={card.title} href={card.href} className="writing__card">
              <h3>{card.title}</h3>
            </Card>
          )
        )}
      </div>
    </Section>
  );
}
