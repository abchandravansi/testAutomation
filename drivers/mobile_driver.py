# appium wrapper
import os
from appium import webdriver as appium_webdriver

from tenacity import retry, stop_after_attempt, wait_fixed

from core.logger import log


# -------------------------------
# Retry Wrapper (Appium readiness)
# -------------------------------
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def _start_appium_driver(appium_url, caps):
    return appium_webdriver.Remote(appium_url, caps)


# -------------------------------
# Android Driver
# -------------------------------
def create_android_driver(env_config, caps):
    appium_url = os.getenv("APPIUM_URL") or env_config.get("appium_url")

    log.info("[MOBILE] Starting Android session")
    log.info(f"[MOBILE] Appium URL: {appium_url}")
    log.debug(f"[MOBILE] Capabilities: {caps}")

    try:
        driver = _start_appium_driver(appium_url, caps)

        # -------------------------------
        # Timeouts
        # -------------------------------
        driver.implicitly_wait(int(os.getenv("IMPLICIT_WAIT", 5)))

        # -------------------------------
        # Session Info
        # -------------------------------
        log.info(f"[MOBILE] Android Session ID: {driver.session_id}")

        return driver

    except Exception as e:
        log.error(f"[MOBILE] Android driver init failed: {str(e)}")
        raise


# -------------------------------
# iOS Driver
# -------------------------------
def create_ios_driver(env_config, caps):
    appium_url = os.getenv("APPIUM_URL") or env_config.get("appium_url")

    log.info("[MOBILE] Starting iOS session")
    log.info(f"[MOBILE] Appium URL: {appium_url}")
    log.debug(f"[MOBILE] Capabilities: {caps}")

    try:
        driver = _start_appium_driver(appium_url, caps)

        driver.implicitly_wait(int(os.getenv("IMPLICIT_WAIT", 5)))

        log.info(f"[MOBILE] iOS Session ID: {driver.session_id}")

        return driver

    except Exception as e:
        log.error(f"[MOBILE] iOS driver init failed: {str(e)}")
        raise