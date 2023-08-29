from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

from base.browser import Browser
from pageobjects.base_page import BasePage
from pageelements.login_form import LoginForm


class LoginPage(BasePage):
    LOGIN_LOGO = (By.CLASS_NAME, "login_logo")
    LOGIN_FORM = (By.ID, "login_button_container")
    ERROR_MESSAGE = (By.XPATH, '//h3[@data-test="error"]')

    def __init__(self, browser: Browser, url: str):
        super().__init__(browser, url)
        self.login_form = LoginForm(self.browser, self.url)

    def error_message_exist(self) -> bool:
        try:
            self.browser.find_element(*self.ERROR_MESSAGE)
        except NoSuchElementException:
            return False
        return True

    def get_error_message_text(self) -> str | None:
        if self.error_message_exist():
            return self.browser.find_elements(*self.ERROR_MESSAGE)[0].text
        return None
