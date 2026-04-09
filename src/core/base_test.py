from src.core.config_loader import load_env_config
from src.core.utils import get_env, load_capabilities
from src.drivers.mobile_driver import create_android_driver
from src.drivers.web_driver import create_web_driver

class BaseTest:

    def setup_method(self):
        # 🔥 Assign here
        self.env_config = load_env_config()

        platform = get_env("PLATFORM", "web")
        profile = get_env("DEVICE_PROFILE", "edge")
        
         # 🔥 Load caps dynamically
        caps = load_capabilities(platform, profile)

        if platform == "web":
            self.driver = create_web_driver(self.env_config, caps)
        elif platform == "android":
            self.driver = create_android_driver(self.env_config, caps)
     
        else:
            raise ValueError("Unsupported platform")

    def teardown_method(self):
        if self.driver:
            self.driver.quit()