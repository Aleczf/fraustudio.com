import { getContent } from "@/content";
import Button from "@/components/Button";

// 404 nella voce del sito (EN) — gemella di app/(it)/not-found.tsx.
export default function NotFoundEn() {
  const { notFound } = getContent("en");

  return (
    <main className="container not-found">
      <p className="kicker">404</p>
      <h1>{notFound.title}</h1>
      <p className="not-found__body">{notFound.body}</p>
      <Button href="/en" variant="secondary">
        {notFound.cta}
      </Button>
    </main>
  );
}
