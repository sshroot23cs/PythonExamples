import os
import allure
import pytest
from selenium import webdriver
from src.pages import Pages
import logging
from src.utilities.customLogger import CustomLogger
import pathlib

SCREENSHOT_PATH = os.path.join(os.path.dirname(__file__), "../screenshots")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser type")
    parser.addoption("--env", action="store", default="qa", help="dev / qa / stage / prod")


@pytest.fixture
def driver_args():
    return ['--log-level=LEVEL',
            '--start-maximized',
            '--disable-notifications',
            '--disable-extensions',
            '--selenium_capture_debug=always']


@pytest.fixture(scope="session")
def browser_type(request):
    logger = CustomLogger(logging.DEBUG).get_logger(request=pytest)
    logger.info("Browser type: " + request.config.getoption("--browser").lower())
    return request.config.getoption("--browser").lower()


@pytest.fixture(scope="session")
def get_base_url():
    env = os.environ.get("TEST_ENV", "qa")
    if env == "qa":
        return "https://bstackdemo.com/"
    elif env == "stage":
        return "https://bstackdemo.com/"
    elif env == "prod":
        return "https://bstackdemo.com/"
    else:
        return "https://bstackdemo.com/"

@pytest.fixture(scope="function")
def browser(request, browser_type):
    logger = CustomLogger(logging.DEBUG).get_logger(request=pytest)
    request.node.name = request.node.name.replace(" ", "_")
    logger.info("******** Test Case: " + request.node.name + " ********")
    # Initialize ChromeDriver
    if browser_type == "chrome":
        driver = webdriver.Chrome()
    elif browser_type == "firefox":
        driver = webdriver.Firefox()

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(os.environ.get("MY_ENV_VARIABLE", "https://bstackdemo.com/"))

    # Return the driver object at the end of setup
    yield driver

    # # Do tear down (this code will be executed after each test):
    # if request.session.testsfailed:
    #     # Make the screenshot if test failed:
    #     try:
    #         browser.execute_script("document.body.bgColor = 'white';")
    #
    #         allure.attach(browser.get_screenshot_as_png(),
    #                       name=request.function.__name__,
    #                       attachment_type=allure.attachment_type.PNG
    #                       )
    #     except Exception as e:
    #         pass  # just ignore


    # For cleanup, quit the driver
    driver.quit()

@pytest.fixture(scope="function")
def get_pages_object():
    pages_obj = Pages()
    return pages_obj


#
# def pytest_selenium_capture_debug(item, report, extra):
#     for log_type in extra:
#         if log_type["name"] == "Screenshot":
#             content = base64.b64decode(log_type["content"].encode("utf-8"))
#             with open(item.name + ".png", "wb") as f:
#                 f.write(content)
