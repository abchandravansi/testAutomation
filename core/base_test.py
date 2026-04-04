from core.driver_factory import create_driver


class BaseTest:

    def setup_method(self):
        self.driver = create_driver()

    def teardown_method(self):
        if self.driver:
            self.driver.quit()