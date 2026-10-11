import psycopg2
from psycopg2 import sql
from config import DB_CONFIG

# Lista bianca delle tabelle gestite
TABELLE_VALIDE = [
    "sito",
    "cantiere",
    "quadrante",
    "archeologo",
    "missione",
    "unita_stratigrafica",
    "media",
]


def get_connection():
    """Crea e restituisce una connessione a PostgreSQL."""
    return psycopg2.connect(**DB_CONFIG)


def get_tabella_dati(nome_tabella: str, filtro: str = ""):
    """Recupera le colonne e le righe di una tabella.

    Se viene fornito un filtro, cerca la stringa su tutti i campi
    convertiti in testo tramite CAST(colonna AS TEXT) ILIKE %filtro%.
    """
    if nome_tabella not in TABELLE_VALIDE:
        raise ValueError(f"Tabella non autorizzata: {nome_tabella}")

    conn = None
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            # 1. Recupera i nomi delle colonne della tabella
            query_colonne = sql.SQL(
                """
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name = %s 
                ORDER BY ordinal_position;
            """
            )
            cur.execute(query_colonne, (nome_tabella,))
            colonne = [riga[0] for riga in cur.fetchall()]

            if not colonne:
                return [], []

            # 2. Costruzione della query SELECT
            query_select = sql.SQL("SELECT * FROM {tabella}").format(
                tabella=sql.Identifier(nome_tabella)
            )

            # 3. Applicazione del filtro se presente
            valori_parametri = []
            if filtro and filtro.strip():
                filtro_pattern = f"%{filtro.strip()}%"
                clausole_or = []

                for col in colonne:
                    clausole_or.append(
                        sql.SQL("CAST({colonna} AS TEXT) ILIKE %s").format(
                            colonna=sql.Identifier(col)
                        )
                    )
                    valori_parametri.append(filtro_pattern)

                query_filtro = sql.SQL(" WHERE ") + sql.SQL(" OR ").join(
                    clausole_or
                )
                query_select = query_select + query_filtro

            # 4. Esecuzione query
            cur.execute(query_select, valori_parametri)
            righe = cur.fetchall()

            return colonne, righe

    except Exception as e:
        print(f"Errore durante il recupero dei dati: {e}")
        raise e
    finally:
        if conn:
            conn.close()