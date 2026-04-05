from src.core.config_loader import load_env_config
from core.utils import load_yaml
from selenium import webdriver
from appium import webdriver as appium_webdriver
from selenium.webdriver.chrome.options import Options
import os
from src.core.logger import log


def create_driver():
    platform = os.getenv("PLATFORM", "web").lower()
    browser = os.getenv("BROWSER", "chrome").lower()
    device = os.getenv("DEVICE", "default").lower()
    
    log.info("Creating driver with the following configuration:")
    log.info(f"Platform : {platform}")
    log.info(f"Browser : {browser}")
    log.info(f"Device : {device}")

    env_config = load_env_config()

    if platform == "web":
        log.info("Setting up WebDriver for Selenium Grid")
        caps = load_yaml("config/capabilities/web.yaml")[browser]
        return create_web_driver(env_config, caps)

    elif platform == "android":
        log.info("Setting up Android Driver for Appium")
        caps = load_yaml("config/capabilities/android.yaml")[device]
        return create_android_driver(env_config, caps)

    elif platform == "ios":
        log.info("Setting up iOS Driver for Appium")
        caps = load_yaml("config/capabilities/ios.yaml")[device]
        return create_ios_driver(env_config, caps)

    else:
        raise ValueError(f"Unsupported platform: {platform}")


# -------------------------------
# Web Driver (Selenium Grid)
# -------------------------------
def create_web_driver(env_config, caps):
    selenium_url = os.getenv("SELENIUM_URL") or env_config["selenium_url"]

    return webdriver.Remote(
        command_executor=selenium_url,
        desired_capabilities=caps
    )

# -------------------------------
# Android Driver (Appium)
# -------------------------------
def create_android_driver(env_config, caps):
    appium_url = os.getenv("APPIUM_URL") or env_config["appium_url"]

    return appium_webdriver.Remote(appium_url, caps)
# -------------------------------
# iOS Driver (Future)
# -------------------------------
def create_ios_driver(env_config, caps):
    raise NotImplementedError("iOS setup not added yet")