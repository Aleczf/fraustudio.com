import type { Locale } from "@/content/types";

// Tipi condivisi tra la route (server) e il componente Diagnoser (client).
// Questo file NON contiene runtime pesante (niente SDK, niente system prompt):
// così il client può importarlo con `import type` senza trascinare nulla nel
// bundle. L'unico valore runtime è MAX_INPUT_CHARS, una costante numerica
// innocua e utile a entrambi i lati per validare la stessa soglia.

/** Limite di caratteri dell'input, validato sia lato client che lato server. */
export const MAX_INPUT_CHARS = 800;

/** Corpo della richiesta POST verso /api/diagnose. */
export interface DiagnoseRequestBody {
  processo: string;
  lingua: Locale;
}

/**
 * Esito applicativo della diagnosi (HTTP 200):
 * - "diagnosis": input riconosciuto come processo → tre parti distinte.
 * - "redirect": input fuori tema / vuoto / tentativo di injection → una riga
 *   gentile che riporta al tema (il modello non ha eseguito altro).
 */
export type DiagnoseResult =
  | {
      status: "diagnosis";
      bottleneck: string;
      approach: string;
      magnitude: string;
    }
  | {
      status: "redirect";
      message: string;
    };

/** Risposta di errore gestito (chiave mancante, timeout, rate limit, ecc.). */
export interface DiagnoseErrorResponse {
  error: true;
}

/** Unione di ciò che la route può restituire nel body JSON. */
export type DiagnoseResponse = DiagnoseResult | DiagnoseErrorResponse;

/** Type guard: distingue l'errore gestito da un esito valido. */
export function isDiagnoseError(
  payload: DiagnoseResponse
): payload is DiagnoseErrorResponse {
  return (payload as DiagnoseErrorResponse).error === true;
}
