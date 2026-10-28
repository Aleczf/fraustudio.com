import { getContent } from "@/content";
import type { Locale } from "@/content/types";

// Footer. La riga di voce "I concept sono inventati. Il codice è vero." è la
// firma del sito: Fraunces corsivo, centrata e isolata sopra i metadati.
export default function Footer({ locale = "it" }: { locale?: Locale }) {
  const { footer } = getContent(locale);

  return (
    <footer className="site-footer">
      <div className="container">
        <p className="site-footer__voice">{footer.voiceLine}</p>

        <div className="site-footer__meta">
          <span>{footer.identity}</span>
          <span>
            {footer.vatLabel} {footer.vat}
          </span>
          <span>{footer.location}</span>
          <span>&copy; {footer.year}</span>
        </div>
      </div>
    </footer>
  );
}
