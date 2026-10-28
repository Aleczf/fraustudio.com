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

const site = getContent("it");

// Root layout dell'albero italiano (route group "(it)", copre "/" e
// "/lavori/[slug]"). Radice separata da app/en/layout.tsx — pattern
// "multiple root layouts" di Next.js, l'unico modo per avere <html lang>
// corretto per lingua senza un unico root layout condiviso.
export const metadata: Metadata = {
  metadataBase: new URL("https://alessandrofrau.dev"),
  title: { default: site.meta.title, template: `%s — Alessandro Frau` },
  description: site.meta.description,
  alternates: {
    canonical: "/",
    languages: {
      it: "/",
      en: "/en",
    },
  },
  openGraph: {
    title: site.meta.title,
    description: site.meta.description,
    url: "/",
    siteName: "Alessandro Frau",
    locale: "it_IT",
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

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="it" className={`${fraunces.variable} ${inter.variable}`}>
      <body>
        <Header nav={site.nav} />
        {children}
        <Footer />
      </body>
    </html>
  );
}
