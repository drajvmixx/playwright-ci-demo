from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def username_input(self):
        return self.page.locator("#user-name")
    
    @property
    def password_input(self):
        return self.page.locator("#password")

    @property
    def login_button(self):
      return self.page.locator("#login-button")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_error_visible(self):
        expect(self.page.get_by_text("Epic sadface: Username and password do not match any user in this service")).to_be_visible(timeout=5000)

    def assert_error_empty_login_form(self):
        expect(self.page.get_by_text("Epic sadface: Username is required")).to_be_visible(timeout=5000)