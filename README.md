<p align="center">
  <img src="https://www.regione.marche.it/Portals/0/Images/LogoSmall.png" alt="Regione Marche"/>
</p>

<p align="center">
📅 <i>Dati aggiornati al 02/06/2020</i> 📅
</p>

# 🧪 Regione Marche - Dati COVID-19 in CSV e JSON
Questo repository nasce con lo scopo di aggregare, in un formato utilizzabile per l'analisi, i dati forniti dal *GORES* (Gruppo Operativo Regionale Emergenza Sanitaria) della *Regione Marche*, riguardanti il diffondersi del COVID-19 nel territtorio marchigiano.

Quotidianamente vengono rilasciati 3 diversi report:
- **Report Blu**: documento nel quale viene rilasciato il numero di tamponi effettuati e il numero di nuovi positivi nelle ultime 24h.
- **Report Giallo**: documento nel quale viene aggiornata la panoramica sulla situazione dei casi risultati positivi al coronavirus (ricoverati, isolamento domiciliare, dimessi e guarti, ecc..).
- **Report Arancio**: documento nel quale sono rilasciati i numeri e i dettagli sui decessi avvenuti nelle ultime 24h.

## Aggiornamento giornaliero ~ Ore 19:00 (circa)
Ogni giorno vengono aggiornati i seguenti file:
- Aggiornamento della cartella `./data/JSON/` con il JSON giornaliero che aggrega i 3 report.
- Update del file `covid-19-marche.json` completo di tutti i report.
- Update del file `covid-19-marche.csv` completo di tutti i report.
- Update del file `./data/CSV/dettagli_decessi.csv` con i dettagli dei decessi di ogni report.
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

- Lo script `generate_csv.py` genera il file CSV `covid-19-marche.csv` e `./data/CSV/dettagli_decessi.csv` a partire dai file giornalieri presenti nella cartella `./data/JSON`.
```bash
$ py generate_csv.py
```

- Lo script `check_error.py` effettua un test statico che controlla tutti i file giornalieri presenti nella cartella `./data/JSON`, verificando se ci sono incongruenze.
```bash
$ py check_error.py
```

## Descrizione JSON e CSV
Per maggiori informazioni, nel file [covid-19-marche.md](covid-19-marche.md) sono descritti in dettaglio tutti i campi che compongono il JSON ed il CSV.

## Analisi dei dati
Nella cartella [notebook](notebook) sono presenti 3 Jupyter Notebook nei quali sono riportate delle analisi dei dati presenti in questo repository.
- `Andamento_Positivi`: analisi dell'andamento dei casi positivi ([articolo su Medium](https://medium.com/p/319edb8d1cda)).
- `Andamento_Ricoveri_Guariti`: situazione dei ricoveri e dei guariti ([articolo su Medium](https://medium.com/p/6fe38c9def00)).
- `Andamento_Decessi`: panoramica sui decessi avvenuti nella Regione Marche ([articolo su Medium](https://medium.com/p/a200299a0a10)).

## Informazioni
- I dati sui tamponi iniziano il 25 Febbraio 2020, il primo decesso risale al 02 Marzo 2020 e le prime informazioni riguardo i malati iniziano il 05 Marzo 2020.
- Dal 15 Aprile 2020 vengono conteggiati anche i "test_effettuati". Questo valore corrisponde al totale dei tamponi eseguiti, compresi anche i test ripetuti più volte sulla stessa persona.
- Dal 08 Aprile 2020 viene conteggiato anche il totale dei casi e contatti in isolamento domiciliare dall'inizio dell'epidemia.
- Dal 04 Aprile 2020 vengono conteggiati insieme i pazienti dimessi dalle strutture ospedaliere ed i pazienti risultati negativi al doppio tampone (per allinearsi ai dati trasmessi dalle altre regioni). Quindi, fino al 03 Aprile 2020 il valore del campo "dimessi_guariti" corrisponde ai soli pazienti risultati negativi al doppio tampone.
- Nel report *arancio* del 29 Maggio 2020 è stato ricalcolato il numero totale di decessi. Infatti, 11 persone precedentemente segnalate, da una prima revisione, non risultano classificabili come COVID-19 positivi. Non avendo però a disposizione i dettagli di tali persone, verranno aggiornati solo i valori associati ai decessi totali e quelli divisi per provincia.
- Nel report *giallo* del 20 Maggio 2020 è stato ricalcolato il numero totale di tamponi effettuati, di conseguenza il dato sui tompani totali odierni effettuati relativo allo stesso report risulta incorretto.
- Dal 13 Maggio 2020 nel report *giallo* è stata aggiunta Macerata LD come degenza post critica. Per non creare confusione, essendo pazienti locati nella provincia di Macerata, il dato verrà sommato a Villa dei Pini.
- Dal 04 Maggio 2020 nel report *giallo* è stata aggiunta Villa Fastiggi come degenza post critica. Per non creare confusione, essendo pazienti locati nella zona Marche Nord, il dato verrà sommato alla RSA Galantara.
- Dal 30 Aprile 2020 nel report *giallo* le degenze post critiche sono state divise tra: degenze post critiche acute o meno. Nel conteggio vengono comunque considerate insieme sotto la categoria post critiche.
- Il report *arancio* del 04 Maggio 2020 riporta 3 decessi ma, nella stessa giornata, ne è stato conteggiato anche 1 avvenuto nelle settimane precedenti. Quindi, il totale inerente a questo report è di 4 decessi.
- Il report *arancio* del 03 Maggio 2020 riporta 3 decessi ma, nella stessa giornata, sono stati conteggiati anche altri 2 avvenuti nelle settimane precedenti. Quindi, il totale inerente a questo report è di 5 decessi.
- Il report *arancio* del 01 Maggio 2020 riporta 3 decessi ma, nella stessa giornata, sono stati conteggiati anche altri 2 avvenuti nelle settimane precedenti. Quindi, il totale inerente a questo report è di 5 decessi.
- Il report *arancio* del 28 Aprile 2020 riporta 4 decessi ma, nella stessa giornata, sono stati conteggiati anche altri 2 avvenuti nelle settimane precedenti. Quindi, il totale inerente a questo report è di 6 decessi.
- Il report *arancio* del 26 Aprile 2020 riporta 2 decessi ma, nella stessa giornata, sono stati conteggiati anche altri 3 avvenuti nelle settimane precedenti. Quindi, il totale inerente a questo report è di 5 decessi.
- Il report *arancio* del 23 Aprile 2020 riporta 5 decessi ma, nella stessa giornata, sono stati conteggiati anche altri 3 avvenuti nelle settimane precedenti. Quindi, il totale inerente a questo report è di 8 decessi.
- Il report *arancio* del 20 Aprile 2020 riporta 9 decessi ma, nella stessa giornata, sono stati conteggiati anche altri 3 avvenuti nelle settimane precedenti. Quindi, il totale inerente a questo report è di 12 decessi.
- Il report *arancio* del 17 Aprile 2020 riporta 7 decessi ma, nella stessa giornata, sono stati conteggiati anche altri 5 avvenuti nelle settimane precedenti. Quindi, il totale inerente a questo report è di 12 decessi.
- Il report *arancio* del 15 Aprile 2020 riporta 13 decessi ma, nella stessa giornata, sono stati conteggiati anche altri 5 avvenuti nelle settimane precedenti. Quindi, il totale inerente a questo report è di 18 decessi.
- Il report *arancio* del 02 Aprile 2020 riporta 31 decessi ma, nella stessa giornata, sono stati conteggiati anche altri 23 avvenuti nelle settimane precedenti di cui 1 residente fuori regione. Quindi, il totale inerente a questo report è di 54 decessi.
- Il report *arancio* del 24 Marzo 2020 riporta 32 decessi ma, nella stessa giornata, sono stati conteggiati anche altri 21 avvenuti nelle settimane precedenti e 4 di residenti fuori regione. Quindi, il totale inerente a questo report è di 57 decessi.
- Il report *arancio* del 17 Marzo 2020 riporta 14 decessi ma, nella stessa giornata, sono stati conteggiati anche altri 8 avvenuti nelle settimane precedenti. Quindi, il totale inerente a questo report è di 22 decessi.
- Il report *giallo* del 23 Marzo 2020 non ha aggiornamenti sui casi e contatti in isolamento domiciliare.
- I report *blu* iniziano dal 12 Marzo 2020.
- I report *arancio* iniziano dall'11 Marzo 2020.
- I report *gialli* iniziano dal 5 Marzo 2020.

### Errori e refusi
- I report *gialli* del 08, 09, 10, 11, 13, 14 e 15 Aprile 2020, nella tabella "casi e contatti in isolamento domiciliare" sulla colonna "dall'inizio dell'epidemia ad oggi", invertono i valori delle provincie di Pesaro Urbino ed Ancona.
- I report *blu* del 13, 14, 15, 16, 17, 18, 19 e 23 Marzo 2020 riportano errori sul numero di casi positivi e di casi diagnosticati che si ripercuotono anche sul calcolo aggregato di questi valori. Effettuando però un controllo incrociato con i report dei giorni successivi sono stati corretti.
- I report *gialli* del 07, 08, 15, 16, 17, 19 e 23 Marzo 2020 riportano incongruenze tra il numero di casi positivi (corretto) ed il numero dei malati. Nel dettaglio i report del 15, 16 e 17 Marzo hanno un malato in meno, quello del 07 Marzo ha 7 malati in meno mentre quello del 08, 19 e 23 Marzo ne considerano rispettivamente 6, 18 e 2 in eccesso.
- Il report *blu* del 18 Marzo 2020 riporta erroneamente la data del 17 Marzo 2020.
- Il report *blu* del 13 Marzo 2020 riporta erroneamente la data del 12 Marzo 2020.
- Il report *blu* del 15 Marzo 2020 riporta erroneamente la data del 14 Marzo 2020. 

## Crediti
Questo progetto non è ne collegato ne sponsorizzato dalla *Regione Marche*. I dati raccolti provengono dal sito ufficiale www.regione.marche.it e le informazioni presenti in questo repository sono coperte da licenza MIT. È libero l'uso commerciale, l'uso privato, la modifica e la distribuzione con la condizione unica di menzionare la fonte e l'autore.

&copy; Gianluca Bonifazi - https://biuni.it

[![BuyMeACoffee](https://i.ibb.co/gynFwS1/rsz-default-orange.png "Make a donation")](https://www.buymeacoffee.com/Biuni)