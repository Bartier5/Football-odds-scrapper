import os
import logging
from driver import get_driver
from scraper import get_page_soup
from parser import parse_matches
from transformer import transform
from storage import save
from config import PL_URL

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/scraper.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

def run_pipeline():
    logger.info("Pipeline Started")
    print("\n[Pipeline] starting...")
    driver = get_driver()
    try:
        print("[pipeline] Loading OddsPortal...")
        soup = get_page_soup(driver, PL_URL)

        print("[pipeline] Parsing matches...")
        raw = parse_matches(soup)
        print(f"[pipeline] Found {len(raw)} matches")

        print("[pipeline] Transforming data...")
        df = transform(raw)

        print("[pipeline] Saving to database...")
        save(df)
        print(f"[pipeline] Done — {len(df)} records saved\n")
        logger.info(f"Pipeline complete — {len(df)} records saved")
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        print(f"[pipeline] ERROR: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_pipeline()