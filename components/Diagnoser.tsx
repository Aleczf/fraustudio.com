"use client";

import { useEffect, useState, type FormEvent } from "react";
import { getContent } from "@/content";
import type { Locale } from "@/content/types";
import Button from "./Button";
import {
  MAX_INPUT_CHARS,
  isDiagnoseError,
  type DiagnoseResponse,
  type DiagnoseResult,
} from "@/lib/diagnoser-types";

// Diagnoser interattivo (Tranche 3, i18n in Tranche 4). Unica isola client del
// sito: gestisce input, stato di caricamento con frasi che ruotano, chiamata
// alla route /api/diagnose e rendering dell'output. La chiave API vive solo
// lato server: qui non arriva mai (nessuna prop, nessun NEXT_PUBLIC_).
// Risponde nella lingua della pagina: il parametro "lingua" segue la route,
// che sceglie il system prompt corrispondente.
type Phase = "idle" | "loading" | "done" | "error";

export default function Diagnoser({ locale = "it" }: { locale?: Locale }) {
  const { diagnoser } = getContent(locale);
  const contactHref = locale === "en" ? "/en#contatto" : "/#contatto";

  const [value, setValue] = useState("");
  const [phase, setPhase] = useState<Phase>("idle");
  const [result, setResult] = useState<DiagnoseResult | null>(null);
  const [loadingIndex, setLoadingIndex] = useState(0);

  const trimmedLength = value.trim().length;
  const tooLong = value.length > MAX_INPUT_CHARS;
  const canSubmit =
    trimmedLength > 0 && !tooLong && phase !== "loading";

  // Frasi di attesa che ruotano ogni ~1.5s (niente spinner generico).
  useEffect(() => {
    if (phase !== "loading") return;

    setLoadingIndex(0);
    const id = window.setInterval(() => {
      setLoadingIndex((i) => (i + 1) % diagnoser.loadingPhrases.length);
    }, 1500);

    return () => window.clearInterval(id);
  }, [phase, diagnoser.loadingPhrases.length]);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!canSubmit) return;

    setPhase("loading");
    setResult(null);

    try {
      const response = await fetch("/api/diagnose", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ processo: value.trim(), lingua: locale }),
      });

      // Un errore HTTP (chiave mancante, rate limit, timeout…) porta al
      // fallback cortese, mai a messaggi tecnici.
      if (!response.ok) {
        setPhase("error");
        return;
      }

      const payload = (await response.json()) as DiagnoseResponse;

      if (isDiagnoseError(payload)) {
        setPhase("error");
        return;
      }

      setResult(payload);
      setPhase("done");
    } catch {
      setPhase("error");
    }
  }

  return (
    <section id="diagnoser" className="diagnoser">
      <div className="container">
        <h2 className="diagnoser__title">{diagnoser.title}</h2>
        <p className="diagnoser__sub prose-measure">{diagnoser.sub}</p>

        <form className="diagnoser__form" onSubmit={handleSubmit}>
          <label htmlFor="diagnoser-input" className="sr-only">
            {diagnoser.title}
          </label>
          <textarea
            id="diagnoser-input"
            className="diagnoser__textarea"
            placeholder={diagnoser.placeholder}
            value={value}
            onChange={(e) => setValue(e.target.value)}
            rows={4}
            maxLength={MAX_INPUT_CHARS}
            aria-describedby="diagnoser-counter"
          />

          <div className="diagnoser__controls">
            <span
              id="diagnoser-counter"
              className={`diagnoser__counter caption${
                tooLong ? " is-over" : ""
              }`}
            >
              {value.length}/{MAX_INPUT_CHARS} {diagnoser.charLimitLabel}
            </span>

            <Button
              type="submit"
              variant="primary"
              className="diagnoser__submit"
              ariaLabel={diagnoser.button}
              disabled={!canSubmit}
            >
              {phase === "loading" ? diagnoser.buttonLoading : diagnoser.button}
            </Button>
          </div>
        </form>

        {phase === "loading" ? (
          <p className="diagnoser__loading caption" aria-live="polite">
            {diagnoser.loadingPhrases[loadingIndex]}
          </p>
        ) : null}

        {phase === "error" ? (
          <p className="diagnoser__error" role="status">
            {diagnoser.errorFallback}
          </p>
        ) : null}

        {phase === "done" && result !== null ? (
          <div
            className="diagnoser__output"
            role="status"
            aria-live="polite"
          >
            {result.status === "redirect" ? (
              <p className="diagnoser__redirect prose-measure">
                {result.message}
              </p>
            ) : (
              <>
                <div className="diagnoser__part">
                  <p className="diagnoser__label kicker">
                    {diagnoser.bottleneckLabel}
                  </p>
                  <p className="diagnoser__text prose-measure">
                    {result.bottleneck}
                  </p>
                </div>

                <div className="diagnoser__part">
                  <p className="diagnoser__label kicker">
                    {diagnoser.approachLabel}
                  </p>
                  <p className="diagnoser__text prose-measure">
                    {result.approach}
                  </p>
                </div>

                <div className="diagnoser__part diagnoser__part--magnitude">
                  <p className="diagnoser__label kicker">
                    {diagnoser.magnitudeLabel}
                  </p>
                  <p className="diagnoser__magnitude">{result.magnitude}</p>
                </div>

                <p className="diagnoser__disclaimer caption prose-measure">
                  {diagnoser.disclaimer}
                </p>

                <a href={contactHref} className="diagnoser__cta">
                  {diagnoser.ctaAfterOutput}
                </a>
              </>
            )}
          </div>
        ) : null}
      </div>
    </section>
  );
}
