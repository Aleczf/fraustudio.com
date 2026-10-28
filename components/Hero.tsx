import { getContent } from "@/content";
import type { Locale } from "@/content/types";
import Button from "./Button";

// Hero definitivo. Server component: il testo è statico, l'animazione delle tre
// negazioni è puro CSS (fade-in-up scaglionato di 120ms via animation-delay,
// una sola volta, rispetta prefers-reduced-motion). Nessun JS necessario.
export default function Hero({ locale = "it" }: { locale?: Locale }) {
  const { hero, contextBar } = getContent(locale);
  const lastIndex = hero.headingLines.length - 1;

  return (
    <section id="top" className="hero">
      <div className="container">
        <p className="kicker hero__kicker">{hero.kicker}</p>

        <h1 className="hero__heading">
          {hero.headingLines.map((line, index) => (
            <span
              key={line}
              className="hero__line"
              style={{ animationDelay: `${index * 120}ms` }}
            >
              {index === lastIndex ? (
                <span className="hero__line-accent">{line}</span>
              ) : (
                line
              )}
            </span>
          ))}
        </h1>

        <p className="hero__sub prose-measure">{hero.sub}</p>

        <div className="hero__cta-row">
          <Button href={hero.ctaPrimaryHref} variant="primary">
            {hero.ctaPrimary}
          </Button>
          <Button href={hero.ctaSecondaryHref} variant="secondary">
            {hero.ctaSecondary}
          </Button>
        </div>

        <p className="hero__context caption">{contextBar.text}</p>
      </div>
    </section>
  );
}
