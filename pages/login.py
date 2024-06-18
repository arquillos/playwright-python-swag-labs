"""Login page"""
from playwright.sync_api import Page

class LoginPage:
    """Methods and properties for the Login page"""
    def __init__(self, page: Page, page_url: str) -> None:
        self.page = page
        self.page_url = page_url + "/"

        # Locators
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_text("Login")

    def navigate(self) -> None:
        """Browse to the Login page"""
        self.page.goto(self.page_url)

    def title(self) -> str:
        """Page title"""
        return self.page.title()

    def url(self) -> str:
        """Page URL"""
        return self.page.url

    def login(self, username: str, password: str) -> None:
        """Login into the app"""
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
