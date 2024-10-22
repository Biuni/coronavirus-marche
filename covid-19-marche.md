
## JSON e CSV schema
- `data` : giorno nel quale i tre report sono stati pubblicati. È importante sottolineare però, che i dati si riferiscono alle 24h precedenti.
- **file_pdf**
  - **locale**
    - `blu` : percorso del file PDF blu.
    - `giallo` : percorso del file PDF giallo.
    - `arancio` : percorso del file PDF arancio.
  - **online**
    - `blu` : URL del file PDF blu nel sito della regione.
    - `giallo` : URL del file PDF giallo nel sito della regione.
    - `arancio` : URL del file PDF arancio nel sito della regione.
- **tamponi**
  - **totali**
    - `test_effettuati` : numero totale dei tamponi eseguiti, compresi anche i test ripetuti più volte sulla stessa persona, dall'inizio dell'epidemia.
    - `casi_diagnosticati` : numero totale di persone a cui è stato eseguito un tampone dall'inizio dell'epidemia.
    - `casi_positivi` : numero totale di persone risultate positive al tampone dall'inizio dell'epidemia.
  - **odierni**
    - `test_effettuati` : numero dei tamponi eseguiti, compresi anche i test ripetuti più volte sulla stessa persona, nelle ultime 24h.
    - `casi_diagnosticati` : numero di persone a cui è stato eseguito un tampone nelle ultime 24h.
    - `casi_positivi` : numero di persone risultate positive al tampone nelle ultime 24.
- **malati**:
  - **totali**
    - `persone` : numero totale di persone risultate positive al tampone dall'inizio dell'epidemia.
    - **provincia**
      - `pesaro_urbino` : numero totale di persone risultate positive al tampone, nella provincia di Pesaro Urbino, dall'inizio dell'epidemia.
      - `ancona` : numero totale di persone risultate positive al tampone, nella provincia di Ancona, dall'inizio dell'epidemia.
      - `macerata` : numero totale di persone risultate positive al tampone, nella provincia di Macerata, dall'inizio dell'epidemia.
      - `fermo` : numero totale di persone risultate positive al tampone, nella provincia di Fermo, dall'inizio dell'epidemia.
      - `ascoli_piceno` : numero totale di persone risultate positive al tampone, nella provincia di Ascoli Piceno, dall'inizio dell'epidemia.
      - `extra_regione` : numero totale di persone risultate positive al tampone, non residenti nella regione Marche, dall'inizio dell'epidemia.
  - `dimessi_guariti` : numero totale di persone dimesse e guarite. In questo valore sono considerate: sia le persone risultate negative al doppio tampone di controllo, sia le persone ancora positive ma che sono state dimesse dalle strutture ospedaliere.
  - **attivi**
    - `persone` : numero totale dei pazienti ricoverati o in isolamento domiciliare, attualmente positivi.
    - `isolamento_domiciliare` : numero totale di pazienti attualmente positivi in isolamento domiciliare.
    - **ricoverati**
      - `totali` : numero totale di pazienti ricoverati in strutture ospedaliere.
      - **terapia_intensiva**
        - `totali` : numero totale di pazienti ricoverati in terapia intensiva.
        - **strutture**
          - _numero di ricoveri per ogni struttura_
      - **semi_intensiva**
        - `totali` : numero totale di pazienti ricoverati in aree di semi intensiva.
        - **strutture**
          - _numero di ricoveri per ogni struttura_
      - **post_critica**
        - `totali` : numero totale di pazienti ricoverati in degenze post critiche.
        - **strutture**
          - _numero di ricoveri per ogni struttura_
      - **non_intensiva**
        - `totali` : numero totale di pazienti ricoverati in reparti non intensivi.
        - **strutture**
          - _numero di ricoveri per ogni struttura_
  - **quarantena_domiciliare**
    - `totali` : numero totale, dall'inizio dell'epidemia, di pazienti che sono risultati positivi al tampone o di persone che hanno avuto contatti con casi positivi, che sono attualmente o sono stati in quarantena preventiva.
    - **attivi**
      - `totali` : numero totale di persone positive al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare. (*INFO: Questo valore è calcolato sommando asintomatici e sintomatici, nel cui conteggio sono già considerati gli operatori sanitari*) 
      - `operatori_sanitari` : numero di operatori sanitari che sono positivi al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare. (*INFO: Questo valore è già compreso nel conteggio di sintomatici e asintomatici*)
      - `sintomatici` : numero di persone, con sintomi riconducibili al coronavirus, che sono positive al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare.
      - `asintomatici` : numero di persone, senza alcun sintomo, che sono positive al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare.
    - **provincia**
      - **pesaro_urbino**
        - `totali` : numero totale, dall'inizio dell'epidemia, di pazienti che sono risultati positivi al tampone o di persone che hanno avuto contatti con casi positivi, che sono attualmente o sono stati in quarantena preventiva, nella provincia di Pesaro Urbino.
        - **attivi**
          - `totali` : numero totale di persone positive al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare, nella provincia di Pesaro Urbino. (*INFO: Questo valore è calcolato sommando asintomatici e sintomatici, nel cui conteggio sono già considerati gli operatori sanitari*)
          - `operatori_sanitari` : numero di operatori sanitari che sono positivi al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare, nella provincia di Pesaro Urbino. (*INFO: Questo valore è già compreso nel conteggio di sintomatici e asintomatici*)
          - `sintomatici` : numero di persone, con sintomi riconducibili al coronavirus, che sono positive al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare, nella provincia di Pesaro Urbino.
          - `asintomatici` : numero di persone, senza alcun sintomo, che sono positive al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare, nella provincia di Pesaro Urbino.
      - **ancona**
        - `totali` : numero totale, dall'inizio dell'epidemia, di pazienti che sono risultati positivi al tampone o di persone che hanno avuto contatti con casi positivi, che sono attualmente o sono stati in quarantena preventiva, nella provincia di Ancona.
        - **attivi**
          - `totali` : numero totale di persone positive al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare, nella provincia di Ancona. (*INFO: Questo valore è calcolato sommando asintomatici e sintomatici, nel cui conteggio sono già considerati gli operatori sanitari*)
          - `operatori_sanitari` : numero di operatori sanitari che sono positivi al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare, nella provincia di Ancona. (*INFO: Questo valore è già compreso nel conteggio di sintomatici e asintomatici*)
          - `sintomatici` : numero di persone, con sintomi riconducibili al coronavirus, che sono positive al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare, nella provincia di Ancona.
          - `asintomatici` : numero di persone, senza alcun sintomo, che sono positive al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare, nella provincia di Ancona.
      - **macerata**
        - `totali` : numero totale, dall'inizio dell'epidemia, di pazienti che sono risultati positivi al tampone o di persone che hanno avuto contatti con casi positivi, che sono attualmente o sono stati in quarantena preventiva, nella provincia di Macerata.
        - **attivi**
          - `totali` : numero totale di persone positive al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare, nella provincia di Macerata. (*INFO: Questo valore è calcolato sommando asintomatici e sintomatici, nel cui conteggio sono già considerati gli operatori sanitari*)
          - `operatori_sanitari` : numero di operatori sanitari che sono positivi al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare, nella provincia di Macerata. (*INFO: Questo valore è già compreso nel conteggio di sintomatici e asintomatici*)
          - `sintomatici` : numero di persone, con sintomi riconducibili al coronavirus, che sono positive al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare, nella provincia di Macerata.
          - `asintomatici` : numero di persone, senza alcun sintomo, che sono positive al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare, nella provincia di Macerata.
      - **fermo**
        - `totali` : numero totale, dall'inizio dell'epidemia, di pazienti che sono risultati positivi al tampone o di persone che hanno avuto contatti con casi positivi, che sono attualmente o sono stati in quarantena preventiva, nella provincia di Fermo.
        - **attivi**
          - `totali` : numero totale di persone positive al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare, nella provincia di Fermo. (*INFO: Questo valore è calcolato sommando asintomatici e sintomatici, nel cui conteggio sono già considerati gli operatori sanitari*)
          - `operatori_sanitari` : numero di operatori sanitari che sono positivi al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare, nella provincia di Fermo. (*INFO: Questo valore è già compreso nel conteggio di sintomatici e asintomatici*)
          - `sintomatici` : numero di persone, con sintomi riconducibili al coronavirus, che sono positive al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare, nella provincia di Fermo.
          - `asintomatici` : numero di persone, senza alcun sintomo, che sono positive al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare, nella provincia di Fermo.
      - **ascoli_piceno**
        - `totali` : numero totale, dall'inizio dell'epidemia, di pazienti che sono risultati positivi al tampone o di persone che hanno avuto contatti con casi positivi, che sono attualmente o sono stati in quarantena preventiva, nella provincia di Ascoli Piceno.
        - **attivi**
          - `totali` : numero totale di persone positive al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare, nella provincia di Ascoli Piceno. (*INFO: Questo valore è calcolato sommando asintomatici e sintomatici, nel cui conteggio sono già considerati gli operatori sanitari*)
          - `operatori_sanitari` : numero di operatori sanitari che sono positivi al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare, nella provincia di Ascoli Piceno. (*INFO: Questo valore è già compreso nel conteggio di sintomatici e asintomatici*)
          - `sintomatici` : numero di persone, con sintomi riconducibili al coronavirus, che sono positive al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare, nella provincia di Ascoli Piceno.
          - `asintomatici` : numero di persone, senza alcun sintomo, che sono positive al tampone o che hanno avuto contatti con casi positivi, attualmente in isolamento domiciliare, nella provincia di Ascoli Piceno.
- **decessi**:
  - **totali** :
    - `decessi` : numero totale di decessi di persone risultate positive al coronavirus, dall'inizio dell'epidiemia.
    - **sesso**
      - `maschio` : numero totale maschi deceduti.
      - `femmina` : numero totale di femmine decedute.
    - **provincia**
      - `pesaro_urbino` : numero totale di decessi di persone risultate positive al coronavirus, dall'inizio dell'epidiemia, nella provincia di Pesaro Urbino.
      - `ancona` : numero totale di decessi di persone risultate positive al coronavirus, dall'inizio dell'epidiemia, nella provincia di Ancona.
      - `macerata` : numero totale di decessi di persone risultate positive al coronavirus, dall'inizio dell'epidiemia, nella provincia di Macerata.
      - `fermo` : numero totale di decessi di persone risultate positive al coronavirus, dall'inizio dell'epidiemia, nella provincia di Fermo.
      - `ascoli_piceno` : numero totale di decessi di persone risultate positive al coronavirus, dall'inizio dell'epidiemia, nella provincia di Ascoli Piceno.
  - **odierni**
    - `decessi` : numero di decessi di persone risultate positive al coronavirus, nelle ultime 24h.
    - **dettaglio** (*INFO: Nel formato CSV questi valori sono nel file "dettagli-decessi.csv"*)
      - `id` : numero identificativo incrementale di ogni deceduto.
      - `luogo_decesso` : struttura ospedaliera o comune dove è avvenuto il decesso. (*INFO: Se non disponibile, il valore sarà "ND"*)
      - `sesso` : sesso del deceduto. (*INFO: Se non disponibile, il valore sarà "ND"*)
      - `eta` : età del deceduto. (*INFO: Se non disponibile, il valore sarà "0"*)
      - `comune_domicilio` : comune di domicilio del deceduto. (*INFO: Se non disponibile, il valore sarà "ND"*)
      - `provincia_domicilio` : provincia di domicilio del deceduto. (*INFO: Se non disponibile, il valore sarà "ND"*)
      - `pregresse_patologie` : se il valore è 1 il defunto era affetto da pregresse patologie, se il valore è 0 il defunto non era affetto dal alcuna pregressa patologia. (*INFO: Se non disponibile, il valore sarà "-1"*)