import os
import pytest
from src.utils.logger import get_logger
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

SELENIUM_GRID_URL = os.getenv("SELENIUM_GRID_URL", "http://localhost:4444/wd/hub")
BROWSER = os.getenv("BROWSER", "chrome")


@pytest.fixture
def driver():
    logger = get_logger()
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    if os.getenv("HEADLESS", "1") == "1":
        options.add_argument("--headless=new")
    logger.info("Connecting to Selenium at %s", SELENIUM_GRID_URL)
    driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL, options=options)
    driver.set_window_size(1280, 800)
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def attach_screenshot(request, driver):
    yield
    try:
        png = driver.get_screenshot_as_png()
        name = request.node.name
        allure.attach(png, name=f"screenshot-{name}", attachment_type=allure.attachment_type.PNG)
    except Exception:
        get_logger().exception("Failed to attach screenshot for %s", request.node.name)
