from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException, WebDriverException
from time import sleep
from src.utils.logger import get_logger
import allure


class BasePage:
    TITLE = (By.TAG_NAME, "title")

    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = get_logger()

    @allure.step("Open URL: {url}")
    def open_url(self, url):
        self.logger.debug("open_url: %s", url)
        self.driver.get(url)

    def find(self, locator):
        self.logger.debug("find: %s", locator)
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_visible(self, locator):
        self.logger.debug("wait_for_visible: %s", locator)
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_invisible(self, locator):
        self.logger.debug("wait_for_invisible: %s", locator)
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_not_exist(self, locator):
        self.logger.debug("wait_for_not_exist: %s", locator)
        return self.wait.until(EC.staleness_of(self.find(locator)))

    def get_text(self, locator):
        el = self.find(locator)
        text = el.text
        self.logger.debug("get_text: %s -> %s", locator, text)
        return text

    def is_visible(self, locator):
        is_visible = self.find(locator).is_displayed()
        self.logger.debug("is_visible: %s -> %s", locator, is_visible)
        return is_visible

    @allure.step("Click: {locator}")
    def click(self, locator, retries=3, screenshot_type=None):
        self.logger.debug("click: %s (retries=%s)", locator, retries)
        try:
            el = self.find(locator)
            el = self.wait.until(EC.element_to_be_clickable(el))
            if screenshot_type == "full":
                self.highlight(el)
                self.take_screenshot(name=f"click-{locator}")
            elif screenshot_type == "element":
                self.take_element_screenshot(el, name=f"click-{locator}")
            el.click()
            return el
        except (
            StaleElementReferenceException,
            ElementClickInterceptedException,
        ) as e:
            sleep(0.5)
            if retries > 0:
                return self.click(
                    locator, retries - 1, screenshot_type=screenshot_type
                )
            else:
                self.logger.exception("click failed: %s", locator)
                raise WebDriverException(
                    f"Could not click on element {locator}: {str(e)}"
                ) from e

    @allure.step("Type: {text} into: {locator}")
    def type(self, locator, text, screenshot_type=None):
        self.logger.debug("type: %s -> %s", locator, text)
        el = self.find(locator)
        el.clear()
        el.send_keys(text)
        if screenshot_type == "full":
            self.highlight(el)
            self.take_screenshot(name=f"type-{locator}")
        elif screenshot_type == "element":
            self.take_element_screenshot(el, name=f"type-{locator}")
        return el

    def take_screenshot(self, name):
        try:
            png = self.driver.get_screenshot_as_png()
            allure.attach(
                png, name=name, attachment_type=allure.attachment_type.PNG
            )
        except Exception:
            self.logger.exception("Failed to take screenshot: %s", name)

    @allure.step("Wait for text in element: {locator} contains {text}")
    def wait_for_text(self, locator, text):
        self.logger.debug("wait_for_text: %s contains %s", locator, text)
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))
    
    def highlight(self, element):
        self.driver.execute_script(
            "arguments[0].style.border='3px solid blue'", element)
        self.driver.execute_script(
            "arguments[0].style.backgroundColor='yellow'", element)

    def take_element_screenshot(self, element, name):
        try:
            png = element.screenshot_as_png
            allure.attach(
                png, name=name, attachment_type=allure.attachment_type.PNG
            )
        except Exception:
            self.logger.exception(
                "Failed to take element screenshot: %s", name)
    
    def wait_for_url_contains(self, text):
        self.logger.debug("wait_for_url_contains: %s", text)
        return self.wait.until(EC.url_contains(text))
