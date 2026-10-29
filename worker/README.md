# Worker del modulo di contatto

Riceve il form di fraustudio.com e inoltra ogni richiesta via email con [Resend](https://resend.com).

## Primo deploy

1. Crea un account Resend con l'indirizzo che deve ricevere le richieste (`alessandro.frau88@gmail.com`) e genera una API key.
   Con il mittente `onboarding@resend.dev` non serve toccare i DNS, ma Resend consegna solo a quell'indirizzo.
2. Da questa cartella:

   ```sh
   npx wrangler login
   npx wrangler deploy
   npx wrangler secret put RESEND_API_KEY
   ```

3. Copia l'URL che `wrangler deploy` stampa (`https://fraustudio-contatto.fraustudio.workers.dev`)
   in `FORM_ENDPOINT` dentro `scripts/build.py`, poi rigenera il sito con `python3 scripts/build.py`.

## Test

```sh
node test.mjs
```

## Più avanti

- Mittente sul dominio: verifica un sottodominio (es. `mail.fraustudio.com`) su Resend aggiungendo i record DNS su IONOS, poi cambia `MAIL_FROM`.
- Scrittura del lead in Odoo: aggiungi una chiamata JSON-RPC a `crm.lead` dopo `sendMail`.
