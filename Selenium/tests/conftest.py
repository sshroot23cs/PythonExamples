import os
import base64
import pytest
from selenium import webdriver
from src.pageone import PageOne

SCREENSHOT_PATH = os.path.join(os.path.dirname(__file__), "saved_screenshots")

@pytest.fixture
def driver_args():
    return ['--log-level=LEVEL',
            '--start-maximized',
            '--disable-notifications',
            '--disable-extensions',
            '--selenium_capture_debug=always']

@pytest.fixture(scope="function")
def browser():
    # Initialize ChromeDriver
    driver = webdriver.Chrome()
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()

@pytest.fixture(scope="function")
def page_one_object():
    page_one_obj = PageOne()
    return page_one_obj

#
# def pytest_selenium_capture_debug(item, report, extra):
#     for log_type in extra:
#         if log_type["name"] == "Screenshot":
#             content = base64.b64decode(log_type["content"].encode("utf-8"))
#             with open(item.name + ".png", "wb") as f:
#                 f.write(content)
