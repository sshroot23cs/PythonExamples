import pytest
from time import sleep


# @pytest.fixture
# def browser():
#     # Initialize ChromeDriver
#     driver = webdriver.Chrome()
#     # Wait implicitly for elements to be ready before attempting interactions
#     driver.implicitly_wait(10)
#
#     # Return the driver object at the end of setup
#     yield driver
#
#     # For cleanup, quit the driver
#     driver.quit()

@pytest.skip("Skipping this test")
def test_browserstack(browser):

    browser.get("https://bstackdemo.com/")
    browser.maximize_window()
    sleep(10)

# def test_loop_browser_windows(browser):
#
#     urls = ["https://bstackdemo.com/",
#             "https://www.google.com/",
#             "https://www.facebook.com/",
#             "https://www.linkedin.com/",
#             "https://www.naukri.com/"]
#     for i in range(5):
#         browser.get(urls[i])
#         browser.maximize_window()
#         browser.save_screenshot("screenshot_{}.png".format(i))
#         sleep(10)
#
#     cnt = len(browser.window_handles)
#     print("Total windows:", cnt)
#     for x in range(cnt):
#         browser.switch_to.window(browser.window_handles[x])
#         print(browser.title)
#         sleep(30)  # 30sec
