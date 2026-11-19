# Regole di comunicazione — Les Chambres d'Or

Questo file è la guida che Claude segue ogni volta che prepara un post.
Se una regola cambia, si cambia qui.

## Chi siamo
- Les Chambres d'Or, struttura ricettiva a conduzione familiare a Roma: camere, suite e appartamento.
- Riga sotto il nome: nelle grafiche si scrive **come nel logo: "Hotel • Suite • Apartament"** (usata nel Welcome corner e nel post del 19/11/2026). In altre indicazioni della famiglia compare anche "Room • Suite • Apartment": **da confermare con la famiglia** quale sia quella definitiva.

## Tono
- Caldo, accogliente, familiare: come un padrone di casa che ti aspetta, non come una catena alberghiera.
- Elegante ma semplice. Frasi brevi, niente toni da pubblicità aggressiva.
- Simbolo ricorrente: il **cuoricino dorato** (nei testi: 💛; nelle grafiche: quello ufficiale).

## Lingue
- Ogni testo in **inglese e italiano**: prima l'inglese (la maggior parte degli ospiti è straniera), poi l'italiano.

## Stile grafico (per grafiche e testi sovrapposti alle foto)
- Font: **Cormorant Garamond** (titoli) e **Jost** (testi). Non usarne altri.
- Colore della struttura: **beige tortora**; accenti oro.
- Logo nella versione ufficiale, mai ridisegnato. Sulle foto si usa la versione **scura** (`brand/logo-scuro.svg`, scelta da Valerio); sulle illustrazioni chiare quella oro (`brand/logo-oro.svg`).

## Post con foto — stile approvato (Valerio, nov 2026)
Il modello pronto è `template/render.py`: usarlo sempre, così ogni post resta uguale. Le regole:
- Formato Instagram **4:5 (1080×1350)**. Foto **a tutto schermo**: niente cornici, niente angoli decorativi, niente spazio bianco attorno.
- **In alto**: logo scuro + "LES CHAMBRES D'OR" + riga sotto il nome, in marrone scuro (#2B1D13), su una **fascia orizzontale semitrasparente uniforme** (crema al 58%) dietro al logo.
- **Mai sfumature bianche** sulla foto (per Valerio "orribili"). L'unica sfumatura ammessa è quella scura in basso, dietro il testo.
- **In basso**: titolo in bianco (Cormorant Garamond), riga italiana in corsivo giallo chiaro (#E8D5A3), **cuoricino dorato** allineato alla base dell'ultima parola del titolo.
- Formato preferito: **carosello** — copertina (titolo EN + riga IT) e 1–3 slide interne, ognuna con una **foto diversa** e un breve testo prima in inglese poi in italiano.
- Le slide vanno dal "largo" al "vicino" (camera intera → dettagli), senza ripetere la stessa inquadratura.

## Scelta delle foto
- Elenco e note di ogni foto: `foto/INDICE.csv`. Leggere sempre la colonna `note` prima di usarla.
- **Niente carta igienica visibile**: le foto segnate "Carta igienica" si usano solo ritagliandola via; se è al centro, non usarle.
- Niente targhe d'auto leggibili, niente marchi di altri in evidenza (es. capsule Borbone), niente persone.
- Valerio (19/11/2026): nello stesso carosello niente foto troppo simili tra loro (es. due facciate di palazzo); per il tema Roma servono foto che facciano vedere la città. Le targhe si possono oscurare (sfocatura) invece di scartare la foto.
- Nei testi solo cose vere: gestione familiare, angolo di benvenuto con caffè, tè, acqua e minibar in ogni camera. Niente servizi o prezzi non confermati dalla famiglia.

## Automazione (dal 18/11/2026)
- **2 post a settimana**, giorni e orari scelti con i dati di Metricool (migliori orari del profilo), mai due post di fila con lo stesso tema.
- I post si programmano su Metricool **con almeno 3 giorni di anticipo**: chiunque della famiglia (Valerio, la madre, Cesare) può guardarli, modificarli o cancellarli dal calendario prima che escano.
- Ogni correzione della famiglia va riportata qui in BRAND.md, così i post successivi la rispettano.
- Ogni post va annotato in `registro.csv` e la data d'uso delle foto in `foto/INDICE.csv` (colonna `ultimo_uso`).

## Frasi già approvate
- "In Rome, do as the Romans do: coffee first" — Welcome corner / L'angolo del benvenuto
- "Your room, our care"
- "Making your stay golden"
- "Need help? Just ask me"
- "Your room, our care" / "La tua camera, la nostra cura" (carosello del 19/11/2026)

## Cosa pubblichiamo
- Camere, suite e appartamento: luce, dettagli, comfort.
- Angolo di benvenuto in ogni camera: acqua, caffè, tè, minibar.
- Dettagli e atmosfera della struttura.
- Roma e il quartiere: consigli, scorci, cose da fare.

## Cadenza
- **2 post a settimana** (massimo assoluto 4; piano gratuito Metricool: 20 post al mese).
- Alternare i temi: mai due post di fila con lo stesso tema o la stessa foto.
- Una foto già pubblicata non si ripete prima di 3 mesi (controllare `registro.csv`).

## Cosa NON pubblichiamo mai
- Foto con ospiti o persone riconoscibili senza consenso.
- Documenti, schermi, reception con dati visibili, targhe, numeri di camera associati a ospiti.
- Prezzi o promozioni non confermati dalla famiglia.
- Recensioni inventate o attribuite a persone.

## Hashtag
- 5–10 per post, mix di specifici e locali. Proposta di base (da rivedere):
  `#leschambresdor #rome #roma #romeitaly #visitrome #romestay #boutiquestay`
