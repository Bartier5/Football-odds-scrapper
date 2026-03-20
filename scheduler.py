from apscheduler.schedulers.blocking import BlockingScheduler
from main import run_pipeline
from config import SCRAPE_INTERVAL_MINUTES
import logging

logger = logging.getLogger(__name__)
scheduler = BlockingScheduler()
scheduler.add_job(
    run_pipeline,
    "interval",
    minutes = SCRAPE_INTERVAL_MINUTES,
    id = "pl_odds_scraper"
)
if __name__ == "__main__":
    print(f"[scheduler] Starting — running every {SCRAPE_INTERVAL_MINUTES} minutes")
    print("[scheduler] Press Ctrl+C to stop\n")
    run_pipeline()        
    scheduler.start()