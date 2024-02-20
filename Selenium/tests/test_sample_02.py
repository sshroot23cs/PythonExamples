from time import sleep

class TestSample002:
    def test_sample_002(self, browser, page_one_object):
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

