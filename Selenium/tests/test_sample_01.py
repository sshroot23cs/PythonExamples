from time import sleep

def test_sample_001(browser, page_one_object):
    browser.get("https://bstackdemo.com/")
    browser.maximize_window()
    page_data = page_one_object.get_page_locator(locator_name="oneplus-category")
    page_ele = page_one_object.get_page_element(browser, page_data)
    page_ele.click()
    print(page_data)
    assert "OnePlus" in browser.title, "Title is not matching"
    sleep(10)

