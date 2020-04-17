<p align="center">
  <img src="http://www.regione.marche.it/Portals/0/Images/LogoSmall.png" alt="Regione Marche"/>
</p>

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
- Lo script `download_pdf.py` permette di scaricare i report in formato PDF. Per scaricare tutti i report di un determinato colore, eseguire:
```bash
$ py download_pdf.py -blu       # download di tutti i report Blu
$ py download_pdf.py -giallo    # download di tutti i report Gialli
$ py download_pdf.py -arancio   # download di tutti i report Arancio
```
Per scaricare invece uno specifico report, eseguire:
```bash
$ py download_pdf.py -blu|-giallo|-arancio MM-DD-YYYY   # MM è il mese, DD il giorno e YYYY l'anno
```
- Lo script `generate_json.py` permette di generare il JSON `covid-19-marche.json` a partire dai file giornalieri presenti nella cartella `./data/JSON`.
```bash
$ py generate_json.py
```

## Informazioni
- I report *gialli* iniziano dal 5 Marzo 2020.
- I report *blu* iniziano dal 12 Marzo 2020.
- I report *arancio* iniziano dall'11 Marzo 2020.

### Errori e refusi
- I report *gialli* del 13, 14 e 15 Aprile 2020, nella tabella "casi e contatti in isolamento domiciliare" sulla colonna "dall'inizio dell'epidemia ad oggi", invertono i valori delle provincie di Pesaro Urbino ed Ancona.
- Il report *blu* del 18 Marzo 2020 riporta erroneamente la data del 17 Marzo 2020.
- Il report *blu* del 15 Marzo 2020 riporta erroneamente la data del 14 Marzo 2020.
- Il report *blu* del 13 Marzo 2020 riporta erroneamente la data del 12 Marzo 2020.

## Crediti
Questo progetto non è ne collegato ne sponsorizzato dalla *Regione Marche* in quanto ente. I dati raccolti provengono dal sito ufficiale http://www.regione.marche.it.

Le informazioni presenti in questo repository sono coperte da licenza MIT. È quindi libero l'uso commerciale e privato, la modifica e la distribuzione con la condizione unica di menzionare la fonte e l'autore.