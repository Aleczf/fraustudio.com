import type { WorkBadge } from "@/content/types";

// Il badge "CLIENTE REALE" (e la sua variante EN) è l'unico con accento pieno:
// segnala il lavoro con un committente vero. Tutti gli altri sono outline neutri.
const FILLED_BADGES: readonly WorkBadge[] = ["CLIENTE REALE", "REAL CLIENT"];

export interface BadgeProps {
  badge: WorkBadge;
  note?: string;
}

export default function Badge({ badge, note }: BadgeProps) {
  const filled = FILLED_BADGES.includes(badge);
  const classes = ["badge", filled ? "badge--filled" : null].filter(Boolean).join(" ");

  return (
    <span className="badge-group">
      <span className={classes}>{badge}</span>
      {note ? <span className="badge-note">{note}</span> : null}
    </span>
  );
}
