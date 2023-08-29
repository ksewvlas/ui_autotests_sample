from base.browser import Browser


class BasePage:
    def __init__(self, browser: Browser, url: str):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.open(self.url)
