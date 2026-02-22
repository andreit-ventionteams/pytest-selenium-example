from selenium.webdriver.common.by import By
from .base_page import BasePage

class SignInPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")
    LOGOUT_BTN = (By.CSS_SELECTOR, "a[href='/logout']")

    def open(self):
        self.open_url(self.URL)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def logout(self):
        self.click(self.LOGOUT_BTN)
    
    def get_flash_message(self):
        return self.get_text(self.FLASH)
