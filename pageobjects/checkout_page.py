from selenium.webdriver.common.by import By

from base.browser import Browser
from pageelements.header import Header
from pageobjects.base_page import BasePage


class CheckoutPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    INPUT_FIRST_NAME = (By.XPATH, '//input[@data-test="firstName"]')
    INPUT_LAST_NAME = (By.XPATH, '//input[@data-test="lastName"]')
    INPUT_POSTAL_CODE = (By.XPATH, '//input[@data-test="postalCode"]')
    CONTINUE_BUTTON = (By.XPATH, '//input[@data-test="continue"]')
    CANCEL_BUTTON = (By.XPATH, '//button[@data-test="cancel"]')

    def __init__(self, browser: Browser, url: str):
        super().__init__(browser, url)
        self.headers = Header(self.browser, self.url)

    def enter_first_name(self, first_name: str):
        self.browser.find_element(*self.INPUT_FIRST_NAME).send_keys(first_name)
        return self

    def enter_last_name(self, last_name: str):
        self.browser.find_element(*self.INPUT_LAST_NAME).send_keys(last_name)
        return self

    def enter_postal_code(self, postal_code: str):
        self.browser.find_element(*self.INPUT_POSTAL_CODE).send_keys(postal_code)
        return self
