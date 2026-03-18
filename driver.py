import undetected_chromedriver as uc
from config import HEADLESS, USER_AGENT

def get_driver():
    options = uc.ChromeOptions()
    options.add_argument(f"--user-agent={USER_AGENT}")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    if HEADLESS:
        options.add_argument("--headless=new")
    driver = uc.Chrome(options=options,
                       version_main=145)
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )
    return driver
        