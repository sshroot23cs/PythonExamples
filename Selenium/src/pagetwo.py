from src.common_page_elements import CommonPageElements
from src.helper import Helper

class PageTwo(CommonPageElements):

    LOCATOR_FILE = "page2_locators.yaml"

    def __init__(self):
        pageHelper = Helper()
        self.page_locators = pageHelper.get_locators(self.LOCATOR_FILE)

    def get_page_locator(self, locator_name=None):
        print(self.page_locators)
        if locator_name:
            return self.page_locators[locator_name]
        else:
            return self.page_locators

    def fill_form(self, browser, name, email, password):
        self.enter_keys_to_element(browser, self.page_locators["name"], name)
        self.enter_keys_to_element(browser, self.page_locators["email"], email)
        self.enter_keys_to_element(browser, self.page_locators["password"], password)
        self.click_element(browser, self.page_locators["submit"])
