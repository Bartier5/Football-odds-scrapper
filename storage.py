
import sqlite3
import pandas as pd
import logging
from config import DB_PATH, TABLE_NAME

logger = logging.getLogger(__name__)

def save(df: pd.DataFrame):
    if df.empty:
        logger.warning("Empty DataFrame — nothing to save")
        return

    conn = sqlite3.connect(DB_PATH)
    try:
        df.to_sql(TABLE_NAME, conn, if_exists="append", index=False)
        logger.info(f"Saved {len(df)} rows to {TABLE_NAME}")
        print(f"[storage] Saved {len(df)} rows to '{TABLE_NAME}'")
    except Exception as e:
        logger.error(f"Failed to save to DB: {e}")
    finally:
        conn.close()

def read_all() -> pd.DataFrame:
    conn = sqlite3.connect(DB_PATH)
    try:
        df = pd.read_sql(f"SELECT * FROM {TABLE_NAME}", conn)
        return df
    except Exception as e:
        logger.error(f"Failed to read from DB: {e}")
        return pd.DataFrame()
    finally:
        conn.close()

def read_latest() -> pd.DataFrame:
    conn = sqlite3.connect(DB_PATH)
    try:
        query = f"""
            SELECT * FROM {TABLE_NAME}
            WHERE scraped_at = (
                SELECT MAX(scraped_at) FROM {TABLE_NAME}
            )
        """
        df = pd.read_sql(query, conn)
        return df
    except Exception as e:
        logger.warning(f"Could not read latest: {e}")
        return pd.DataFrame()
    finally:
        conn.close()