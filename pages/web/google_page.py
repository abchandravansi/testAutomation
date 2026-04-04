from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.logger import log


class GooglePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        # Locators
        self.search_box = (By.NAME, "q")

    # -------------------------------
    # Actions
    # -------------------------------
    def open(self, base_url):
        log.info("[WEB] Opening Google page")
        self.driver.get(base_url)

    def search(self, text):
        log.info(f"[WEB] Searching for: {text}")

        search_box = self.wait.until(
            EC.presence_of_element_located(self.search_box)
        )
        search_box.clear()
        search_box.send_keys(text)
        search_box.submit()

    # -------------------------------
    # Validations
    # -------------------------------
    def is_results_loaded(self, keyword):
        log.info("[WEB] Validating search results")

        self.wait.until(EC.title_contains(keyword))
        return keyword in self.driver.title