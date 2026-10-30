# Les Chambres d'Or — archivio social

Archivio delle foto e delle regole usate da Claude per gestire Instagram e Facebook
di Les Chambres d'Or tramite Metricool.

> ⚠️ **Questo repository è pubblico.** Tutto quello che c'è qui va considerato visibile a chiunque.
> Niente password, chiavi, dati di ospiti o prenotazioni, foto con persone o documenti.

## Come funziona

1. Le foto arrivano (in chat o caricate qui), vengono ripulite dai metadati (GPS, modello del telefono),
   ridimensionate a 1440 px sul lato lungo e rinominate in modo descrittivo.
2. Claude sceglie le foto, scrive i testi seguendo `BRAND.md` e programma i post su Metricool
   usando il link pubblico della foto in questo repository.
3. Ogni post programmato viene annotato in `registro.csv`, per non ripetere foto e temi.
4. La famiglia può controllare, modificare o cancellare i post dal calendario di Metricool
   fino al momento della pubblicazione.

## Struttura

| Percorso | Contenuto |
|---|---|
| `foto/camere/` | camere |
| `foto/suite/` | suite |
| `foto/appartamento/` | appartamento |
| `foto/benvenuto-colazione/` | angolo di benvenuto, caffè, colazione |
| `foto/dettagli/` | dettagli, arredi, oggetti, luce |
| `foto/roma/` | quartiere e città |
| `grafiche/` | illustrazioni e grafiche già pronte da pubblicare |
| `BRAND.md` | regole di comunicazione: tono, lingue, stile, cosa non pubblicare |
| `registro.csv` | storico dei post programmati |

## Nomi dei file

`tema-soggetto-dettaglio-NN.jpg`, tutto minuscolo, parole separate da trattini, niente spazi né accenti.
Esempio: `suite-letto-luce-mattina-01.jpg`.
