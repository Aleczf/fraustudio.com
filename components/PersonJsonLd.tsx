// Structured data Person per la home (entrambe le lingue) — Tranche 4.
// Si aggiunge al JSONLD FAQPage già presente in Faq.tsx.
export default function PersonJsonLd() {
  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "Person",
    name: "Alessandro Frau",
    jobTitle: "AI Process Engineer",
    url: "https://alessandrofrau.dev",
    address: {
      "@type": "PostalAddress",
      addressLocality: "Milano",
      addressCountry: "IT",
    },
    sameAs: ["https://github.com/Aleczf"],
  };

  return (
    <script
      type="application/ld+json"
      // eslint-disable-next-line react/no-danger
      dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
    />
  );
}
