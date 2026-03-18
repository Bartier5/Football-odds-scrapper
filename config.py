BASE_URL = "https://www.oddsportal.com"
PL_URL = f"{BASE_URL}/football/england/premier-league"

SCRAPE_INTERVAL_MINUTES = 30
DB_PATH = "data/odds.db"
TABLE_NAME = "pl_odds"

HEADLESS = False
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.0.0 Safari/537.36"
)
