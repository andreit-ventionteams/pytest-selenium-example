
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class CookieBannerFragement(BasePage):

    ROOT = (By.ID, "CybotCookiebotDialog")
    ACCEPT_BUTTON = (By.ID,
                     "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    REJECT_BUTTON = (By.ID,
                     "CybotCookiebotDialogBodyButtonDecline")
    HEADER = (By.ID, "CybotCookiebotDialogBodyContentTitle")
    CLOSE_BUTTON = (By.ID, "CybotCookiebotBannerCloseButtonE2E")

    def wait_for_banner(self):
        self.wait_for_visible(self.ROOT)

    def accept_cookies(self):
        self.click(self.ACCEPT_BUTTON)
        self.wait_for_invisible(self.ROOT)
    
    def reject_cookies(self):
        self.click(self.REJECT_BUTTON)
        self.wait_for_invisible(self.ROOT)

    def close_banner(self):
        self.click(self.CLOSE_BUTTON)
        self.wait_for_invisible(self.ROOT)
    


