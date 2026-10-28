import { getContent } from "@/content";
import Button from "@/components/Button";

// 404 nella voce del sito, non generica.
export default function NotFound() {
  const { notFound } = getContent("it");

  return (
    <main className="container not-found">
      <p className="kicker">404</p>
      <h1>{notFound.title}</h1>
      <p className="not-found__body">{notFound.body}</p>
      <Button href="/" variant="secondary">
        {notFound.cta}
      </Button>
    </main>
  );
}
