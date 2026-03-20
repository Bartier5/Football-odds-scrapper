# Premier League Odds Scraper

An automated ETL pipeline that scrapes live Premier League betting odds 
from OddsPortal, transforms the data, and stores it in SQLite on a schedule.

## Features
- Stealth browser automation (undetected-chromedriver)
- JavaScript-rendered content handled via Selenium WebDriverWait
- Pandas transform layer with implied probability and overround calculations
- SQLite storage with full historical timestamped snapshots
- APScheduler automation — runs every 30 minutes
- Structured file logging for headless monitoring

## Stack
- Python 3.12
- Selenium + undetected-chromedriver
- BeautifulSoup4 + lxml
- Pandas
- SQLite
- APScheduler

## Architecture
```
scheduler.py        # runs pipeline every 30 minutes
    └── main.py     # orchestrator
        ├── driver.py       # stealth Chrome browser
        ├── scraper.py      # Selenium navigation + page render
        ├── parser.py       # BeautifulSoup data extraction
        ├── transformer.py  # Pandas cleaning + probability calc
        └── storage.py      # SQLite persistence
```

## Setup
```bash
git clone https://github.com/Bartier5/Football-odds-scrapper
cd Football-odds-scrapper
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Usage
Run once:
```bash
python main.py
```

Run on schedule (every 30 minutes):
```bash
python scheduler.py
```

## Output
Each run appends 18 rows to `data/odds.db` with columns:
- `slug` — match identifier
- `home_win`, `draw`, `away_win` — decimal odds
- `prob_home`, `prob_draw`, `prob_away` — implied probabilities
- `overround` — bookmaker margin
- `scraped_at` — UTC timestamp