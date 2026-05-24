from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("//input[@autocomplete='username webauthn']")
        self.password_input = page.locator("(//input[@autocomplete='current-password' and @type='password'])[last()]")
        self.login_button = page.locator("(//span/span[contains(.,'Sign in')])[last()]")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_error_visible(self, message: str):
        expect(self.page.get_by_text("Wrong email or password.")).to_be_visible()