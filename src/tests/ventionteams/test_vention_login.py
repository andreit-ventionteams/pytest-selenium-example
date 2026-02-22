import pytest
from src.pages.ventionteams.login_page import LoginPage


class TestVentionLogin:
    """Test suite for Vention login page functionality"""
    USER_NOT_FOUND_ERROR = "User not found"

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Setup method to initialize page object before each test"""
        self.login_page = LoginPage(driver)
        self.login_page.open()
        yield

    def test_login_with_empty_email(self, driver):
        """Test login with empty email field"""
        self.login_page.click_continue()
        error_msg = self.login_page.get_error_message()
        assert error_msg == "Please enter an email or username", "Expected an error message for empty email"
        assert self.login_page.is_email_input_visible(), "Email input should be visible"

    def test_login_with_invalid_email_format(self, driver):
        """Test login with invalid email format"""
        invalid_emails = ["invalid", "invalid@", "@invalid.com", "invalid@@test.com"]
        
        for invalid_email in invalid_emails:
            self.login_page.enter_email(invalid_email)
            self.login_page.click_continue()
            
            expected_error = self.USER_NOT_FOUND_ERROR
            error_msg = self.login_page.get_error_message()
            assert expected_error in error_msg, f"Expected error message: '{expected_error}' but got '{error_msg}' for email: '{invalid_email}'"
            assert self.login_page.is_email_input_visible(), f"Email input should be visible for invalid email: '{invalid_email}'"

    def test_login_with_nonexistent_email(self, driver):
        """Test login with valid format but non-existent email"""
        self.login_page.enter_email("nonexistent@test.com")
        self.login_page.click_continue()

        expected_error = self.USER_NOT_FOUND_ERROR
        error_msg = self.login_page.get_error_message()
        assert expected_error == error_msg, f"Expected error message: '{expected_error}' but got '{error_msg}'"
        assert self.login_page.is_email_input_visible(), "Email input should be visible"

    def test_continue_with_google_redirects_correctly(self, driver):
        """Verify that Continue with Google button redirects to Google accounts"""
        self.login_page.click_google_login()
        self.login_page.wait_for_url_contains("accounts.google.com")

    def test_continue_with_vention_redirects_correctly(self, driver):
        """Verify that Continue with Vention button redirects to Microsoft login"""
        self.login_page.click_microsoft_login()
        self.login_page.wait_for_url_contains("login.microsoftonline.com")

    @pytest.mark.parametrize("invalid_email", [
        " "
        "true",
        "test@",
        "@test.com",
        "test@@test.com"
    ])
    def test_invalid_email_variations(self, driver, invalid_email):
        """Parametrized test for various invalid email formats"""
        self.login_page.enter_email(invalid_email)
        self.login_page.click_continue()
        
        assert self.login_page.is_email_input_visible(), f"Email input should be visible for invalid email: '{invalid_email}'"
        error_msg = self.login_page.get_error_message()
        assert self.USER_NOT_FOUND_ERROR == error_msg, f"Expected error message: '{self.USER_NOT_FOUND_ERROR}' but got '{error_msg}' for email: '{invalid_email}'"
    
    def test_create_account_link_navigates_to_signup(self, driver):
        """Test that clicking the create account link navigates to the signup page"""
        self.login_page.click_create_account_link()
        self.login_page.wait_for_url_contains("auth.ventionteams.com/account/create")