"""
config_bak.py
Parametri di collegamento a PostgreSQL.
  N.B. copiare config_bak in config.py e personalizzare config.py (dbname, user, password)
"""
import os

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),           
    "dbname": os.getenv("DB_NAME", "Test_Archeo_01"),            # <-- inserire il nome dello Schema Db
    "user": os.getenv("DB_USER", "mio-utente-postgres"),         # <-- inserire nome utente postgres
    "password": os.getenv("DB_PASSWORD", "mia-password"),        # <-- inserire password postgres
    "port": int(os.getenv("DB_PORT", 5432)),
}
