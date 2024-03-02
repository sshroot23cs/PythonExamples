from selenium.webdriver.common.by import By

class CommonPageElements:
    def __init__(self):
        pass

    def get_page_element(self, driver, locator):
        """
        This function will return the element based on the locator
        :param driver:
        :param locator:
        :return:
        """
        find_by = None
        if locator["type"] == "id":
            find_by = By.ID
        elif locator["type"] == "xpath":
            find_by = By.XPATH

        if find_by:
            return driver.find_element(find_by, locator["value"])
        else:
            print("Invalid locator type {} for locator {}".format(locator['type'], locator['value']))
            return None


    def click_element(self, driver, element):
        driver.find_element_by_id(element).click()

    def enter_keys_to_element(self, driver, element, keys):
        driver.find_element_by_id(element).send_keys(keys)
        return driver.find_element_by_id(element)
