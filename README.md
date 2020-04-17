# Dati JSON | Coronavirus - COVID-19 | Marche (Italia)
Questo repository nasce con lo scopo di aggregare, in un formato utilizzabile per l'analisi, i dati forniti dalla regione Marche, in particolare dal GORES (Gruppo Operativo Regionale Emergenza Sanitaria), riguardanti il diffondersi del COVID-19 nel territtorio marchigiano.
Di fatti, quotidianamente vengono rilasciati 3 diversi report:
- **Report Blu**: documento nel quale viene rilasciato il numero di tamponi effettuati e il numero di nuovi positivi nelle ultime 24h.
- **Report Giallo**: documento nel quale viene aggiornata la panoramica sulla situazione dei casi risultati positivi al coronavirus (ricoverati, isolamento domiciliare, dimessi e guarti, ecc..).
- **Report Arancio**: documento nel quale sono rilasciati i numeri e i dettagli sui decessi avvenuti nelle ultime 24h.

## Aggiornamento giornaliero
Ogni giorno vengono aggiornati i seguenti file:
- Aggiornamento della cartella `./data/JSON/` con il JSON giornaliere che aggrega i 3 report.
- Update del file `covid-19-marche.json` completo di tutti i report.
- Aggiornamento delle liste "gores_blu", "gores_giallo" e "gores_arancio" in `download_pdf.py`.

## Script Python
- Lo script `download_pdf.py` permette di scaricare la lista di tutti i report. Esempi di utilizzo:
```bash
$ py download_pdf.py -blu       # download di tutti i report BLU
$ py download_pdf.py -giallo    # download di tutti i report GIALLI
$ py download_pdf.py -arancio   # download di tutti i report ARANCIO
```
- Lo script `generate_json.py` permette di generare il JSON `covid-19-marche.json` a partire dai file giornalieri presenti nella cartella `./data/JSON`.
```bash
$ py generate_json.py
```

## Informazioni
- I report BLU iniziano dal 12 Marzo 2020, i report ARANCIO iniziano dall'11 Marzo 2020 mentre i report GIALLI iniziano dal 5 Marzo 2020.
- Il report BLU del 18 Marzo 2020 riporta erroneamente la data del 17 Marzo 2020.
- Il report BLU del 15 Marzo 2020 riporta erroneamente la data del 14 Marzo 2020.
- Il report BLU del 13 Marzo 2020 riporta erroneamente la data del 12 Marzo 2020.