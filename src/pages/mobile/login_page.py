from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.core.logger import log


class LoginPage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        # Locators (example IDs - replace with real app locators)
        self.username_field = (AppiumBy.ID, "username")
        self.password_field = (AppiumBy.ID, "password")
        self.login_button = (AppiumBy.ID, "login")
        self.home_screen = (AppiumBy.ID, "home")  # post-login element

    # -------------------------------
    # Actions
    # -------------------------------
    def enter_username(self, username):
        log.info(f"[MOBILE] Entering username: {username}")

        elem = self.wait.until(
            EC.presence_of_element_located(self.username_field)
        )
        elem.clear()
        elem.send_keys(username)

    def enter_password(self, password):
        log.info("[MOBILE] Entering password")

        elem = self.wait.until(
            EC.presence_of_element_located(self.password_field)
        )
        elem.clear()
        elem.send_keys(password)

    def tap_login(self):
        log.info("[MOBILE] Tapping login button")

        self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def login(self, username, password):
        log.info("[MOBILE] Performing login flow")

        self.enter_username(username)
        self.enter_password(password)
        self.tap_login()

    # -------------------------------
    # Validations
    # -------------------------------
    def is_login_successful(self):
        log.info("[MOBILE] Validating login success")

        try:
            self.wait.until(
                EC.presence_of_element_located(self.home_screen)
            )
            return True
        except:
            return False