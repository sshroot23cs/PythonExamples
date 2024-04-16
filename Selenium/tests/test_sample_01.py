import logging
import allure
import pytest
from time import sleep
from src.utilities.assert_json import assert_json
from src.utilities.customLogger import CustomLogger


class TestSample001:

    @allure.title("First Test Case")
    @pytest.mark.smoke
    def test_sample_001(self, request, browser, get_pages_object):
        logger = CustomLogger(logging.DEBUG).get_logger(request)
        logger.info("This is a test log message")

        aa = [
            {'id': '!anything', 'name': 'Main', 'description': 'Main component', 'intentId': '',
             'nodes': [{'id': '!anything', 'name': 'start', 'nodeType': 'START_NODE'},
                       {'id': '!anything', 'name': 'Question & Answer',
                        'nodeType': 'RECOGNITION_NODE'},
                       {'id': '!anything', 'name': 'Message', 'nodeType': 'MESSAGE_NODE'},
                       {'id': '!anything', 'name': 'External Actions',
                        'nodeType': 'EXTERNAL_ACTION_NODE'}], 'numNodes': 4},
            {'id': '!anything', 'name': 'TestA', 'description': '', 'intentId': '', 'nodes': [
                {'id': '!anything', 'name': 'External Actions_02',
                 'nodeType': 'EXTERNAL_ACTION_NODE'},
                {'id': '!anything', 'name': 'Message_02', 'nodeType': 'MESSAGE_NODE'},
                {'id': '!anything', 'name': 'Question & Answer_02',
                 'nodeType': 'RECOGNITION_NODE'},
                {'id': '!anything', 'name': 'start', 'nodeType': 'START_NODE'}], 'numNodes': 4},
            {'id': '!anything', 'name': 'NO_INTENT', 'description': 'intent',
             'intentId': '!anything',
             'nodes': [{'id': '!anything', 'name': 'start', 'nodeType': 'START_NODE'},
                       {'id': '!anything', 'name': 'Question & Answer_01',
                        'nodeType': 'RECOGNITION_NODE'},
                       {'id': '!anything', 'name': 'Message_01', 'nodeType': 'MESSAGE_NODE'},
                       {'id': '!anything', 'name': 'External Actions_01',
                        'nodeType': 'EXTERNAL_ACTION_NODE'}], 'numNodes': 4}
            ]
        bb = [
            {'id': '!anything', 'name': 'Main', 'description': 'Main component', 'intentId': '',
             'nodes': [{'id': '!anything', 'name': 'start', 'nodeType': 'START_NODE'},
                       {'id': '!anything', 'name': 'Question & Answer',
                        'nodeType': 'RECOGNITION_NODE'},
                       {'id': '!anything', 'name': 'Message', 'nodeType': 'MESSAGE_NODE'},
                       {'id': '!anything', 'name': 'External Actions',
                        'nodeType': 'EXTERNAL_ACTION_NODE'}], 'numNodes': 4},
            {'id': '!anything', 'name': 'TestA', 'description': '', 'intentId': '', 'nodes': [
                {'id': '!anything', 'name': 'External Actions_02',
                 'nodeType': 'EXTERNAL_ACTION_NODE'},
                {'id': '!anything', 'name': 'Message_02', 'nodeType': 'MESSAGE_NODE'},
                {'id': '!anything', 'name': 'Question & Answer_02',
                 'nodeType': 'RECOGNITION_NODE'},
                {'id': '!anything', 'name': 'start', 'nodeType': 'START_NODE'}], 'numNodes': 4},
            {'id': '!anything', 'name': 'NO_INTENT', 'description': 'intent',
             'intentId': '!anything',
             'nodes': [{'id': '!anything', 'name': 'start', 'nodeType': 'START_NODE'},
                       {'id': '!anything', 'name': 'Question & Answer_01',
                        'nodeType': 'RECOGNITION_NODE'},
                       {'id': '!anything', 'name': 'Message_01', 'nodeType': 'MESSAGE_NODE'},
                       {'id': '!anything', 'name': 'External Actions_01',
                        'nodeType': 'EXTERNAL_ACTION_NODE'}], 'numNodes': 4}
            ]
        assert_json(aa, bb)
        browser.get("https://bstackdemo.com/")
        browser.maximize_window()
        page_data = get_pages_object.page_one.get_page_locator(locator_name="oneplus-category")
        page_ele = get_pages_object.page_one.get_page_element(browser, page_data)
        page_ele.click()
        print(page_data)
        # allure.attach('screenshot', browser.get_screenshot_as_png())
        assert "OnePlus" in browser.title, "Title is not matching"
        sleep(10)
        logger.info("This is a test log message end")



