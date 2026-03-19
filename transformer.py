import pandas as pd
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def transform(raw_records: list[dict]) -> pd.DataFrame:
    if not raw_records:
            logger.warning("No records to transform")
            return pd.DataFrame()
    df = pd.DataFrame(raw_records)
    logger.info(f"Transforming {len(df)} records")

    for col in ["home_win", "draw", "away_win"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")


    df.dropna(subset=["home_win", "draw", "away_win"], how="all", inplace=True)

    df["prob_home"] = (1 / df["home_win"]).round(4)
    df["prob_draw"] = (1 / df["draw"]).round(4)
    df["prob_away"] = (1 / df["away_win"]).round(4)

    df["overround"] = (df["prob_home"] + df["prob_draw"] + df["prob_away"]).round(4)

    
    df["scraped_at"] = datetime.utcnow().isoformat()


    df.drop_duplicates(subset=["match_id"], inplace=True)

    df.reset_index(drop=True, inplace=True)

    logger.info(f"Transform complete — {len(df)} clean records")
    return df