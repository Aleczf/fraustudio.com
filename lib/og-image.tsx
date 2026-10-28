import { ImageResponse } from "next/og";

// Genera l'immagine Open Graph/Twitter (1200×630) usata da
// app/(it)/opengraph-image.tsx e app/en/opengraph-image.tsx. Stile coerente
// con DESIGN.md: fondo --paper, tipografia Fraunces, un solo dettaglio in
// --accent (il punto dopo il nome, eco del gesto tipografico dell'hero).
export function renderOgImage(tagline: string) {
  return new ImageResponse(
    (
      <div
        style={{
          width: "1200px",
          height: "630px",
          display: "flex",
          flexDirection: "column",
          alignItems: "flex-start",
          justifyContent: "center",
          padding: "96px",
          backgroundColor: "#FAFAF7",
          color: "#101418",
          fontFamily: "serif",
        }}
      >
        <div
          style={{
            fontSize: 30,
            letterSpacing: "0.08em",
            textTransform: "uppercase",
            color: "#5C6470",
            marginBottom: 28,
            display: "flex",
          }}
        >
          {tagline}
        </div>
        <div style={{ fontSize: 92, lineHeight: 1.05, display: "flex", alignItems: "baseline" }}>
          <span>Alessandro Frau</span>
          <span style={{ color: "#0062AD", marginLeft: 6 }}>.</span>
        </div>
        <div
          style={{
            marginTop: 40,
            width: 120,
            height: 4,
            backgroundColor: "#0062AD",
            display: "flex",
          }}
        />
      </div>
    ),
    { width: 1200, height: 630 }
  );
}
