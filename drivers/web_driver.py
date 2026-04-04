# selenium wrapper
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from tenacity import retry, stop_after_attempt, wait_fixed

from core.logger import log


# -------------------------------
# Retry Wrapper (Grid startup safe)
# -------------------------------
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def _start_remote_driver(selenium_url, options):
    return webdriver.Remote(
        command_executor=selenium_url,
        options=options
    )


# -------------------------------
# Main Driver Creator
# -------------------------------
def create_web_driver(env_config, caps):
    selenium_url = os.getenv("SELENIUM_URL") or env_config.get("selenium_url")

    browser = caps.get("browserName", "chrome").lower()

    log.info(f"[WEB] Starting browser: {browser}")
    log.info(f"[WEB] Selenium Grid URL: {selenium_url}")

    if browser == "chrome":
        options = ChromeOptions()

        for key, value in caps.items():
            if key == "goog:chromeOptions":
                for arg in value.get("args", []):
                    options.add_argument(arg)
            else:
                options.set_capability(key, value)

    elif browser == "firefox":
        options = FirefoxOptions()

        for key, value in caps.items():
            if key == "moz:firefoxOptions":
                for arg in value.get("args", []):
                    options.add_argument(arg)
            else:
                options.set_capability(key, value)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    try:
        driver = _start_remote_driver(selenium_url, options)

        # -------------------------------
        # Timeouts
        # -------------------------------
        driver.set_page_load_timeout(int(os.getenv("PAGE_LOAD_TIMEOUT", 30)))
        driver.implicitly_wait(int(os.getenv("IMPLICIT_WAIT", 5)))

        # -------------------------------
        # Window handling
        # -------------------------------
        if not any("--headless" in arg for arg in options.arguments):
            try:
                driver.maximize_window()
            except Exception:
                log.warning("[WEB] Could not maximize window")

        # -------------------------------
        # Session Info
        # -------------------------------
        log.info(f"[WEB] Session started: {driver.session_id}")

        return driver

    except Exception as e:
        log.error(f"[WEB] Failed to start driver after retries: {str(e)}")
        raise