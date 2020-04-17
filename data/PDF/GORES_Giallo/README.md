## Download dei report in PDF
I file PDF non sono stati caricati su Github. Nel caso vogliate scaricarli in locale dovete per prima cosa clonare la cartella con il comando:
```bash
$ git clone https://github.com/Biuni/coronavirus-marche.git
```
Successivamente accedere alla cartella `/script`:
```bash
$ cd coronavirus-marche && cd script
```
e poi eseguire il seguente comando per avviare lo script Python che permette di scaricare tutti i report *gialli*:
```bash
$ py download_pdf.py -giallo
```