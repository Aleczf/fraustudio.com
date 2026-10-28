import type { MetadataRoute } from "next";
import { getContent } from "@/content";

const BASE_URL = "https://alessandrofrau.dev";

// Sitemap statica (Tranche 4): home + pagine caso, in entrambe le lingue,
// con hreflang alternates per ogni entry.
export default function sitemap(): MetadataRoute.Sitemap {
  const { works } = getContent("it");
  const slugs = works.cases.map((work) => work.slug);

  const entries: MetadataRoute.Sitemap = [
    {
      url: `${BASE_URL}/`,
      lastModified: new Date(),
      alternates: { languages: { it: `${BASE_URL}/`, en: `${BASE_URL}/en` } },
    },
    {
      url: `${BASE_URL}/en`,
      lastModified: new Date(),
      alternates: { languages: { it: `${BASE_URL}/`, en: `${BASE_URL}/en` } },
    },
  ];

  for (const slug of slugs) {
    entries.push({
      url: `${BASE_URL}/lavori/${slug}`,
      lastModified: new Date(),
      alternates: {
        languages: {
          it: `${BASE_URL}/lavori/${slug}`,
          en: `${BASE_URL}/en/lavori/${slug}`,
        },
      },
    });
    entries.push({
      url: `${BASE_URL}/en/lavori/${slug}`,
      lastModified: new Date(),
      alternates: {
        languages: {
          it: `${BASE_URL}/lavori/${slug}`,
          en: `${BASE_URL}/en/lavori/${slug}`,
        },
      },
    });
  }

  return entries;
}
