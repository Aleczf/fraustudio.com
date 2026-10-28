import type { Metadata } from "next";
import { getContent } from "@/content";
import CaseStudyContent from "@/components/CaseStudyContent";

// Pagina caso statica (SSG, locale EN) — gemella di app/(it)/lavori/[slug].

export function generateStaticParams() {
  const { works } = getContent("en");
  return works.cases.map((work) => ({ slug: work.slug }));
}

type CaseParams = Promise<{ slug: string }>;

export async function generateMetadata({ params }: { params: CaseParams }): Promise<Metadata> {
  const { slug } = await params;
  const { works } = getContent("en");
  const work = works.cases.find((item) => item.slug === slug);
  if (!work) return {};

  return {
    title: work.name,
    description: work.challenge,
    alternates: {
      canonical: `/en/lavori/${slug}`,
      languages: { it: `/lavori/${slug}`, en: `/en/lavori/${slug}` },
    },
    openGraph: { title: `${work.name} — Alessandro Frau`, description: work.challenge },
  };
}

export default async function CaseStudyPageEn({ params }: { params: CaseParams }) {
  const { slug } = await params;
  return <CaseStudyContent slug={slug} locale="en" />;
}
