import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    return APIClient(base_url="https://your-api-base-url.com")

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login = LoginPage(page)
    page.goto("/login")
    return login