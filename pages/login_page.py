from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.get_by_label("Email or phone").first
        self.password_input = page.get_by_label("Password", exact=True)
        self.login_button = page.get_by_role("button", name="Sign in")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_error_visible(self):
        expect(self.page.get_by_text("Wrong email or password.")).to_be_visible(timeout=5000)

    def assert_error_empty_login_form(self):
        expect(self.page.get_by_text("Please enter an email address or phone number.")).to_be_visible(timeout=5000)