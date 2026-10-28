import { it } from "./it";
import { en } from "./en";
import type { Locale, SiteContent } from "./types";

export const content: Record<Locale, SiteContent> = { it, en };

export function getContent(locale: Locale): SiteContent {
  return content[locale];
}

export * from "./types";
