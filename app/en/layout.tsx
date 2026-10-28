import type { Metadata } from "next";
import { Fraunces, Inter } from "next/font/google";
import "../globals.css";
import { getContent } from "@/content";
import Header from "@/components/Header";
import Footer from "@/components/Footer";

const fraunces = Fraunces({
  subsets: ["latin"],
  weight: ["400", "600"],
  style: ["normal", "italic"],
  variable: "--font-fraunces",
  display: "swap",
});

const inter = Inter({
  subsets: ["latin"],
  weight: ["400", "500", "600"],
  variable: "--font-inter",
  display: "swap",
});

const site = getContent("en");

// Root layout dell'albero inglese ("/en" e "/en/lavori/[slug]"). Radice
// separata da app/(it)/layout.tsx: stesso pattern "multiple root layouts",
// necessario per avere <html lang="en"> corretto (vedi commento gemello lì).
export const metadata: Metadata = {
  metadataBase: new URL("https://alessandrofrau.dev"),
  title: { default: site.meta.title, template: `%s — Alessandro Frau` },
  description: site.meta.description,
  alternates: {
    canonical: "/en",
    languages: {
      it: "/",
      en: "/en",
    },
  },
  openGraph: {
    title: site.meta.title,
    description: site.meta.description,
    url: "/en",
    siteName: "Alessandro Frau",
    locale: "en_US",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: site.meta.title,
    description: site.meta.description,
  },
  icons: {
    icon: "/favicon.svg",
  },
};

export default function EnRootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${fraunces.variable} ${inter.variable}`}>
      <body>
        <Header nav={site.nav} />
        {children}
        <Footer locale="en" />
      </body>
    </html>
  );
}
