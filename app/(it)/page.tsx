import Hero from "@/components/Hero";
import Diagnoser from "@/components/Diagnoser";
import Method from "@/components/Method";
import Works from "@/components/Works";
import About from "@/components/About";
import Writing from "@/components/Writing";
import Faq from "@/components/Faq";
import Contact from "@/components/Contact";
import PersonJsonLd from "@/components/PersonJsonLd";

// Home (locale IT). La shell (Header/Footer) vive in app/(it)/layout.tsx così
// da comparire anche su /lavori/[slug]. Il Diagnoser è subito sotto l'hero.
export default function Home() {
  return (
    <main>
      <PersonJsonLd />
      <Hero />
      <Diagnoser />
      <Method />
      <Works />
      <About />
      <Writing />
      <Faq />
      <Contact />
    </main>
  );
}
