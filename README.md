# archeo-test1

Applicazione Python + Flet + PostgreSQL per la visualizzazione delle Tabelle
di Gestione di un Sito Archeologico.

Le tabelle sono le seguenti: sito, cantiere, quadrante, archeologo, 
  missione, unita_stratigrafica, media.

## Struttura

- `main.py` - interfaccia Flet
- `database.py` - accesso a PostgreSQL
- `config.py` - configurazione della connessione
- `config_bak.py` - template configurazione della connessione
- 'requirements.txt' - per installazione dipendenze
- 'DDL_01.txt' - creazione delle tabelle
- 'DDL_02_Insert.txt' - popolamento delle tabelle con 7/8 records

## Dipendenze

Il software richiede Python 3.10 o superiore e le seguenti librerie:
- **Flet**: framework per l'interfaccia grafica
- **psycopg2-binary**: driver per la connessione al database PostgreSQL

### Installazione delle dipendenze
Installa tutti i pacchetti necessari tramite il file `requirements.txt`:
  pip install -r requirements.txt

## Avvio
1. Copiare il file config_bak.py in config.py
2. Personalizzare il file config.py (dbname,user,password)
3. Creare il database PostgreSQL `Test_Archeo_01`.
    3a. utilizzare DDL_01.txt per creare le tabelle sotto Postgres (PgAdmin4)
    3b. utilizzare DDL_02_Insert.txt per popolare le tabelle con 7/8 records

4. Avviare:
   `python main.py` 
