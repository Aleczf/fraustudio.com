import type { ReactNode } from "react";

// Card generica: bordo hairline su --paper, hover → bordo accento + lieve
// sollevamento. Nella Tranche 2 verrà riempita con i case study.
export interface CardProps {
  children: ReactNode;
  href?: string;
  target?: string;
  rel?: string;
  className?: string;
}

export default function Card({ children, href, target, rel, className }: CardProps) {
  const classes = ["card", className].filter(Boolean).join(" ");

  if (href) {
    return (
      <a href={href} target={target} rel={rel} className={classes}>
        {children}
      </a>
    );
  }

  return <div className={classes}>{children}</div>;
}
