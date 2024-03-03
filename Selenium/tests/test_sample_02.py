from time import sleep
import logging
import allure
from src.utilities.customLogger import CustomLogger

logger = CustomLogger(logging.DEBUG).get_logger()

class TestSample002:
    @allure.title("Second Test Case")
    def test_sample_002(self, browser, get_pages_object):
        urls = ["https://bstackdemo.com/",
                "https://www.google.com/",
                "https://www.facebook.com/",
                "https://www.linkedin.com/",
                "https://www.naukri.com/"]

        for url in urls:
            if urls.index(url) == 0:
                browser.get(url)
            else:
                # open a new tab
                browser.execute_script('window.open("{}","_blank");'.format(url))
            browser.maximize_window()

        cnt = len(browser.window_handles)
        print("Total windows:", cnt)
        for x in range(cnt):
            browser.switch_to.window(browser.window_handles[x])
            print(browser.title)
            logger.info("Open browser title: {}".format(browser.title))

