from selenium.webdriver.common.by import By

from base.browser import Browser
from pageelements.header import Header
from pageobjects.base_page import BasePage


class CheckoutFinishPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    HEADER = (By.CLASS_NAME, "complete-header")
    DESCRIPTION = (By.CLASS_NAME, "complete-text")
    PONY_EXPRESS_PICTURE = (By.CSS_SELECTOR, '[alt="Pony Express"]')
    BACK_HOME_BUTTON = (By.XPATH, '//button[@data-test="back-to-products"]')

    def __init__(self, browser: Browser, url: str):
        super().__init__(browser, url)
        self.headers = Header(self.browser, self.url)
