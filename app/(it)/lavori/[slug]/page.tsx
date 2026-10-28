import type { Metadata } from "next";
import { getContent } from "@/content";
import CaseStudyContent from "@/components/CaseStudyContent";

// Pagina caso statica (SSG, locale IT). Il markup vive in
// components/CaseStudyContent.tsx (condiviso con l'albero /en).

export function generateStaticParams() {
  const { works } = getContent("it");
  return works.cases.map((work) => ({ slug: work.slug }));
}

// Next.js 15: params è una Promise nelle pagine dinamiche (Dynamic APIs).
type CaseParams = Promise<{ slug: string }>;

export async function generateMetadata({ params }: { params: CaseParams }): Promise<Metadata> {
  const { slug } = await params;
  const { works } = getContent("it");
  const work = works.cases.find((item) => item.slug === slug);
  if (!work) return {};

  return {
    title: work.name,
    description: work.challenge,
    alternates: {
      canonical: `/lavori/${slug}`,
      languages: { it: `/lavori/${slug}`, en: `/en/lavori/${slug}` },
    },
    openGraph: { title: `${work.name} — Alessandro Frau`, description: work.challenge },
  };
}

export default async function CaseStudyPage({ params }: { params: CaseParams }) {
  const { slug } = await params;
  return <CaseStudyContent slug={slug} locale="it" />;
}
