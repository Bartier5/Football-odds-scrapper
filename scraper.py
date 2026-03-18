import time   
import random
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from config import PL_URL

logger = logging.getLogger(__name__)

def _delay(min_s=2, max_s=4):
    time.sleep(random.uniform(min_s, max_s))
def get_page_soup(driver, url):
    driver.get(url)
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div[data-testid="game-row"]')
        )
    )
    _delay()
    return BeautifulSoup(driver.page_source, "lxml")
