# archeo-test1

Applicazione Python + Flet + PostgreSQL per la visualizzazione delle Tabelle
di Gestione di un Sito Archeologico.

Le tabelle sono le seguenti: sito, cantiere, quadrante, archeologo, 
  missione, unita_stratigrafica, media.

## Struttura

- `main.py` - interfaccia Flet
- `database.py` - accesso a PostgreSQL
- `config.py` - configurazione della connessione
- 'DDL_01.txt' - creazione delle tabelle
- 'DDL_02_Insert.txt' - popolamento delle tabelle con 7/8 records

## Avvio

1. Creare il database PostgreSQL `Test_Archeo_01`.
    1a. utilizzare DDL_01.txt per creare le tabelle sotto Postgres (PgAdmin4)
    1b. utilizzare DDL_02_Insert.txt per popolare le tabelle con 7/8 records

2. Avviare:
   `python main.py` 
