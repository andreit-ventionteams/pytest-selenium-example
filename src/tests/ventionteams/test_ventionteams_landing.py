from src.pages.ventionteams.landing_page import LandingPage


class TestVentionTeamsLanding:

    def test_verify_landing_page_elements(self, driver):
        page = LandingPage(driver)
        page.open()
        title = driver.title
        assert "Vention" in title, \
            f"Expected title to contain 'Vention', but got '{title}'"
        header = page.get_header()
        expected_header = "AI-enabled software development company"
        assert expected_header in header, \
            f"Expected header to contain '{expected_header}', but got '{header}'"
        assert page.has_logo(), \
            "Expected logo to be present on the landing page"

    def test_verify_cookie_banner_is_closed_with_accept(self, driver):
        page = LandingPage(driver)
        page.open()
        banner = page.get_cookie_banner()
        banner.accept_cookies()

    def test_verify_cookie_banner_is_closed_with_reject(self, driver):
        page = LandingPage(driver)
        page.open()
        banner = page.get_cookie_banner()
        banner.reject_cookies()

    def test_verify_cookie_banner_is_closed_with_close_button(self, driver):
        page = LandingPage(driver)
        page.open()
        banner = page.get_cookie_banner()
        banner.close_banner()