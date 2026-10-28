"use client";

import { useEffect, useRef } from "react";
import type { ReactNode } from "react";

// Sistema di sezione riutilizzabile: apre con kicker maiuscoletto + H2 in forma
// di domanda (pattern Catobi), e rivela il contenuto in fade-in-up allo scroll
// (una sola volta, threshold 0.2, poi disconnette). Rispetta prefers-reduced-motion
// via la classe .reveal definita in globals.css.
export interface SectionProps {
  id: string;
  kicker: string;
  question: string;
  intro?: string;
  children: ReactNode;
  className?: string;
}

export default function Section({
  id,
  kicker,
  question,
  intro,
  children,
  className,
}: SectionProps) {
  const ref = useRef<HTMLElement>(null);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;

    if (typeof IntersectionObserver === "undefined") {
      el.classList.add("is-visible");
      return;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            el.classList.add("is-visible");
            observer.disconnect();
            break;
          }
        }
      },
      { threshold: 0.2 }
    );

    observer.observe(el);
    return () => observer.disconnect();
  }, []);

  const classes = ["section", "reveal", className].filter(Boolean).join(" ");

  return (
    <section id={id} ref={ref} className={classes}>
      <div className="container">
        <p className="kicker">{kicker}</p>
        <h2 className="section-question">{question}</h2>
        {intro ? <p className="section-intro prose-measure">{intro}</p> : null}
        {children}
      </div>
    </section>
  );
}
