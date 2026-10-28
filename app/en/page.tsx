import Hero from "@/components/Hero";
import Diagnoser from "@/components/Diagnoser";
import Method from "@/components/Method";
import Works from "@/components/Works";
import About from "@/components/About";
import Writing from "@/components/Writing";
import Faq from "@/components/Faq";
import Contact from "@/components/Contact";
import PersonJsonLd from "@/components/PersonJsonLd";

// Home (locale EN). Stessa struttura dell'italiano, stessi componenti,
// solo locale="en" così ognuno legge content/en.ts.
export default function HomeEn() {
  return (
    <main>
      <PersonJsonLd />
      <Hero locale="en" />
      <Diagnoser locale="en" />
      <Method locale="en" />
      <Works locale="en" />
      <About locale="en" />
      <Writing locale="en" />
      <Faq locale="en" />
      <Contact locale="en" />
    </main>
  );
}
