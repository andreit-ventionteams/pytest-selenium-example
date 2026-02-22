from src.pages.sign_in_page import SignInPage


class TestTheInternetSignIn:

    def test_sign_in_success(self, driver):
        page = SignInPage(driver)
        page.open()
        page.login("tomsmith", "SuperSecretPassword!")
        assert "You logged into a secure area!" in page.get_flash_message(), \
            "Login failed with valid credentials"

    def test_sign_in_invalid_username(self, driver):
        page = SignInPage(driver)
        page.open()
        page.login("wronguser", "SuperSecretPassword!")
        text = page.get_flash_message()
        assert "invalid" in text.lower(), \
            "Login succeeded with invalid username"

    def test_sign_in_invalid_password(self, driver):
        page = SignInPage(driver)
        page.open()
        page.login("tomsmith", "wrongpassword")
        text = page.get_flash_message()
        assert "invalid" in text.lower(), \
            "Login succeeded with invalid password"

    def test_sign_in_empty_fields(self, driver):
        page = SignInPage(driver)
        page.open()
        page.click(page.LOGIN_BTN)
        text = page.get_flash_message()
        assert "invalid" in text.lower(), \
            "Login succeeded with empty fields"

    def test_logout(self, driver):
        page = SignInPage(driver)
        page.open()
        page.login("tomsmith", "SuperSecretPassword!")
        page.logout()
        text = page.get_flash_message()
        assert "logged out" in text.lower(), "Logout failed"
