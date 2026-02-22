from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.pages.ventionteams.cookie_banner_fragement import CookieBannerFragement


class LandingPage(BasePage):
    URL = "https://ventionteams.com/"

    HEADER = (By.TAG_NAME, "h1")
    LOGO_LINK = (By.CSS_SELECTOR, "[aria-label='Vention']")
    LOGO_IMG = (By.CSS_SELECTOR, "a img[alt*='Vention']")
    FOOTER = (By.TAG_NAME, "footer")
    JSONLD = (By.XPATH, "//script[@type='application/ld+json']")

    def open(self):
        self.open_url(self.URL)

    def get_header(self):
        return self.get_text(self.HEADER)

    def has_logo(self):
        return bool(self.wait_for_visible(self.LOGO_IMG))

    def get_title(self):
        return self.get_text(self.TITLE)
    
    def get_cookie_banner(self):
        banner = CookieBannerFragement(self.driver, self.wait._timeout)
        banner.wait_for_banner()
        return banner