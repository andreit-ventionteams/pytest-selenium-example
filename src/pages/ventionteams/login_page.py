from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://auth.ventionteams.com/"

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='Login']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    GOOGLE_LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Continue with Google']")
    VENTION_LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Continue with Vention']")
    ERROR_MESSAGE = (By.ID, "Login-helper-text")
    PAGE_TITLE = (By.CSS_SELECTOR, "h1, h2")
    LOGIN_ERROR = (By.ID, "Login-helper-text")
    CREATE_ACCOUNT_LINK = (By.XPATH, "//a//*[normalize-space()='Create account']")

    def open(self):
        """Open the login page"""
        self.open_url(self.URL)

    def enter_email(self, email):
        """Enter email in the email input field"""
        self.type(self.EMAIL_INPUT, email)

    def click_continue(self):
        """Click the continue button"""
        self.click(self.CONTINUE_BUTTON)

    def click_google_login(self):
        """Click Continue with Google button"""
        self.click(self.GOOGLE_LOGIN_BUTTON)

    def click_microsoft_login(self):
        """Click Continue with Microsoft button"""
        self.click(self.VENTION_LOGIN_BUTTON)

    def get_error_message(self):
        """Get error message text"""
        return self.get_text(self.LOGIN_ERROR)

    def is_error_displayed(self):
        """Check if error message is displayed"""
        return self.is_visible(self.LOGIN_ERROR)

    def get_page_title(self):
        """Get the page title text"""
        return self.get_text(self.PAGE_TITLE)

    def is_email_input_visible(self):
        """Check if email input is visible"""
        return self.is_visible(self.EMAIL_INPUT)

    def is_create_account_link_visible(self):
        """Check if create account link is visible"""
        return self.is_visible(self.CREATE_ACCOUNT_LINK)
    
    def click_create_account_link(self):
        """Click the create account link"""
        self.click(self.CREATE_ACCOUNT_LINK)