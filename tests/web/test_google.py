from core.base_test import BaseTest
from pages.web.google_page import GooglePage
import pytest

@pytest.mark.smoke
class TestGoogle(BaseTest):

    def test_google_search(self):
        page = GooglePage(self.driver)

        page.open("https://www.google.com")
        page.search("Selenium Python")

        assert page.is_results_loaded("Selenium")