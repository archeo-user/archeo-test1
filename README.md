# archeo-test1

Applicazione Python + Flet + PostgreSQL per la visualizzazione delle Tabelle
di Gestione di un Sito Archeologico.

Le tabelle sono le seguenti: sito, cantiere, quadrante, archeologo, 
  missione, unita_stratigrafica, media.

## Struttura

- `main.py` - interfaccia Flet
- `database.py` - accesso a PostgreSQL
- `config.py` - configurazione della connessione

## Avvio

1. Creare il database PostgreSQL `Test_Archeo_01`.
2. Modificare `config.py` con la propria password PostgreSQL.

3. Avviare:

   `python main.py` 
