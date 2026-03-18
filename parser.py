import logging

logger = logging.getLogger(__name__)
def parse_matches(soup) -> list[dict]:
    matches = []
    rows = soup.find_all("div",  attrs={"data-testid": "game-row"})
    for row in rows:
        try:
            link = row.find("a", class_=lambda c: c and "next-m:flex" in c)
            if not link:
                continue
            href = link.get("href", "")
            slug = href.strip("/").split("/")[-1]
            match_id = slug.split("-")[-1]
            
            odds_divs = row.find_all(
                "div", attrs={"data-testid": "odd-container-default"}
            )
            odds_values = [d.get_text(strip=True) for d in odds_divs]

            matches.append({
                "slug": slug,
                "match_id": match_id,
                "home_win": odds_values[0] if len(odds_values) > 0 else None,
                "draw":     odds_values[1] if len(odds_values) > 1 else None,
                "away_win": odds_values[2] if len(odds_values) > 2 else None,
                "url": f"https://www.oddsportal.com{href}"
            })

        except Exception as e:
            logger.warning(f"Failed to parse row: {e}")
            continue

    return matches
            