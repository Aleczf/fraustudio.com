import { renderOgImage } from "@/lib/og-image";

export const runtime = "edge";
export const alt = "Alessandro Frau — AI Process Engineering";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

export default function OgImage() {
  return renderOgImage("AI Process Engineering · Milano");
}
