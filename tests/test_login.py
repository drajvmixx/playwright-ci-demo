import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_invalid_credentials_show_error(login_page: LoginPage):
    login_page.login("bad@email.com", "wrongpass")
    login_page.assert_error_visible("wrong")
