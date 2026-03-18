
from driver import get_driver
from scraper import get_page_soup
from parser import parse_matches
from config import PL_URL

driver = get_driver()
try:
    soup = get_page_soup(driver, PL_URL)
    matches = parse_matches(soup)

    print(f"\nFound {len(matches)} matches:\n")
    for m in matches:
        print(f"{m['slug']}")
        print(f"  1: {m['home_win']}  X: {m['draw']}  2: {m['away_win']}")
        print()
finally:
    driver.quit()