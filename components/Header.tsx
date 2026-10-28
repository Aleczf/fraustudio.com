"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { usePathname } from "next/navigation";
import type { NavContent } from "@/content/types";
import Button from "./Button";

// Chiave sessionStorage usata per conservare la posizione di scroll quando si
// cambia lingua (Tranche 4): è una navigazione a pagina intera (le due lingue
// sono alberi di route separati), quindi il browser azzererebbe lo scroll di
// default — lo ripristiniamo a mano al mount della pagina di destinazione.
const SCROLL_RESTORE_KEY = "lang-switch-scroll";

// Header fisso minimale. Blur leggero attivato via classe .is-scrolled quando
// si scrolla oltre pochi px. Su mobile: menu overlay a schermo pieno con
// chiusura da Escape, focus riportato al toggle, e trap di focus minimo (Tab).
export default function Header({ nav }: { nav: NavContent }) {
  const [scrolled, setScrolled] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);

  const toggleRef = useRef<HTMLButtonElement>(null);
  const closeRef = useRef<HTMLButtonElement>(null);
  const overlayRef = useRef<HTMLDivElement>(null);

  const pathname = usePathname() ?? "/";
  const isEn = pathname === "/en" || pathname.startsWith("/en/");
  const homeHref = isEn ? "/en#top" : "/#top";
  const diagnoserHref = isEn ? "/en#diagnoser" : "/#diagnoser";
  // Mappa la pagina corrente sulla sua equivalente nell'altra lingua: gli
  // alberi /(it) e /en sono speculari (stessi slug), quindi basta
  // aggiungere/rimuovere il prefisso /en.
  const altHref = isEn ? pathname.replace(/^\/en/, "") || "/" : `/en${pathname === "/" ? "" : pathname}`;

  const closeMenu = useCallback(() => {
    setMenuOpen(false);
    toggleRef.current?.focus();
  }, []);

  // Blur allo scroll.
  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 8);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  // Ripristina lo scroll dopo un cambio lingua (vedi handleLangSwitch sotto).
  useEffect(() => {
    const stored = window.sessionStorage.getItem(SCROLL_RESTORE_KEY);
    if (stored === null) return;
    window.sessionStorage.removeItem(SCROLL_RESTORE_KEY);
    const y = Number(stored);
    if (Number.isFinite(y)) {
      requestAnimationFrame(() => window.scrollTo(0, y));
    }
  }, []);

  const handleLangSwitch = useCallback(() => {
    window.sessionStorage.setItem(SCROLL_RESTORE_KEY, String(window.scrollY));
    // Nessun preventDefault: la navigazione nativa verso altHref procede normalmente.
  }, []);

  // Gestione tastiera + blocco scroll body quando il menu è aperto.
  useEffect(() => {
    if (!menuOpen) return;

    closeRef.current?.focus();
    const previousOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";

    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        event.preventDefault();
        closeMenu();
        return;
      }

      if (event.key !== "Tab") return;

      const focusables = overlayRef.current?.querySelectorAll<HTMLElement>(
        'a[href], button:not([disabled])'
      );
      if (!focusables || focusables.length === 0) return;

      const first = focusables[0];
      const last = focusables[focusables.length - 1];

      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    };

    document.addEventListener("keydown", onKeyDown);
    return () => {
      document.removeEventListener("keydown", onKeyDown);
      document.body.style.overflow = previousOverflow;
    };
  }, [menuOpen, closeMenu]);

  return (
    <header className={`site-header${scrolled ? " is-scrolled" : ""}`}>
      <div className="container site-header__inner">
        <a href={homeHref} className="wordmark">
          {nav.brand}
        </a>

        <nav className="site-nav" aria-label={isEn ? "Main navigation" : "Navigazione principale"}>
          <ul className="site-nav__list">
            {nav.links.map((link) => (
              <li key={link.href}>
                <a href={link.href} className="site-nav__link">
                  {link.label}
                </a>
              </li>
            ))}
          </ul>
        </nav>

        <div className="site-header__actions">
          <a
            href={altHref}
            className="lang-switch"
            aria-label={isEn ? "Switch to Italian" : "Passa all'inglese"}
            onClick={handleLangSwitch}
          >
            <span className={isEn ? undefined : "is-active"}>IT</span>
            <span aria-hidden="true"> / </span>
            <span className={isEn ? "is-active" : undefined}>EN</span>
          </a>

          <Button href={diagnoserHref} variant="primary" className="site-header__cta">
            {nav.cta}
          </Button>

          <button
            ref={toggleRef}
            type="button"
            className="menu-toggle"
            aria-expanded={menuOpen}
            aria-controls="mobile-menu"
            aria-label={isEn ? "Open menu" : "Apri il menu"}
            onClick={() => setMenuOpen(true)}
          >
            <svg
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="1.5"
              aria-hidden="true"
            >
              <line x1="3" y1="8" x2="21" y2="8" />
              <line x1="3" y1="16" x2="21" y2="16" />
            </svg>
          </button>
        </div>
      </div>

      {menuOpen ? (
        <div
          ref={overlayRef}
          id="mobile-menu"
          className="mobile-menu"
          role="dialog"
          aria-modal="true"
          aria-label="Menu"
        >
          <div className="container mobile-menu__top">
            <span className="wordmark">{nav.brand}</span>
            <button
              ref={closeRef}
              type="button"
              className="menu-toggle"
              aria-label={isEn ? "Close menu" : "Chiudi il menu"}
              onClick={closeMenu}
            >
              <svg
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.5"
                aria-hidden="true"
              >
                <line x1="5" y1="5" x2="19" y2="19" />
                <line x1="19" y1="5" x2="5" y2="19" />
              </svg>
            </button>
          </div>

          <nav className="container mobile-menu__nav" aria-label={isEn ? "Mobile navigation" : "Navigazione mobile"}>
            {nav.links.map((link) => (
              <a
                key={link.href}
                href={link.href}
                className="mobile-menu__link"
                onClick={closeMenu}
              >
                {link.label}
              </a>
            ))}
          </nav>

          <div className="container mobile-menu__footer">
            <Button href={diagnoserHref} variant="primary" onClick={closeMenu}>
              {nav.cta}
            </Button>
            <a
              href={altHref}
              className="lang-switch mobile-menu__lang"
              aria-label={isEn ? "Switch to Italian" : "Passa all'inglese"}
              onClick={handleLangSwitch}
            >
              <span className={isEn ? undefined : "is-active"}>IT</span>
              <span aria-hidden="true"> / </span>
              <span className={isEn ? "is-active" : undefined}>EN</span>
            </a>
          </div>
        </div>
      ) : null}
    </header>
  );
}
