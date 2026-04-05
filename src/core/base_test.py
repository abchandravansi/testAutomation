from src.core.config_loader import ConfigLoader
from src.drivers.web_driver import create_web_driver
import os


class BaseTest:

    def setup_method(self):
        # 🔥 Assign here
        self.env_config = ConfigLoader.load_env_config()

        platform = os.getenv("PLATFORM", "web")

        if platform == "web":
            self.driver = create_web_driver(self.env_config, caps={})
        else:
            raise ValueError("Unsupported platform")

    def teardown_method(self):
        if self.driver:
            self.driver.quit()