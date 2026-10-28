import type { ReactNode } from "react";

// Shared component (no "use client"): renderizzato server-side quando riceve
// solo href/testo, oppure incluso nel bundle client quando un genitore client
// gli passa un onClick. In entrambi i casi le props restano coerenti.
export interface ButtonProps {
  children: ReactNode;
  variant?: "primary" | "secondary";
  href?: string;
  onClick?: () => void;
  type?: "button" | "submit";
  target?: string;
  rel?: string;
  className?: string;
  ariaLabel?: string;
  disabled?: boolean;
}

export default function Button({
  children,
  variant = "primary",
  href,
  onClick,
  type = "button",
  target,
  rel,
  className,
  ariaLabel,
  disabled = false,
}: ButtonProps) {
  const classes = ["btn", `btn-${variant}`, className].filter(Boolean).join(" ");

  // Il bottone secondario è "testo + freccia": la freccia è decorativa e
  // vive nel componente, mentre il testo può essere sottolineato all'hover.
  const inner =
    variant === "secondary" ? (
      <>
        <span className="btn-label">{children}</span>
        <span className="btn-arrow" aria-hidden="true">
          &rarr;
        </span>
      </>
    ) : (
      children
    );

  if (href) {
    return (
      <a
        href={href}
        className={classes}
        onClick={onClick}
        target={target}
        rel={rel}
        aria-label={ariaLabel}
      >
        {inner}
      </a>
    );
  }

  return (
    <button
      type={type}
      className={classes}
      onClick={onClick}
      aria-label={ariaLabel}
      disabled={disabled}
    >
      {inner}
    </button>
  );
}
