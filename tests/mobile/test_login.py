from src.core.base_test import BaseTest
from src.pages.mobile.login_page import LoginPage


class TestLogin(BaseTest):

    def test_login(self):
        page = LoginPage(self.driver)

        page.login("testuser", "password123")

        assert page.is_login_successful()