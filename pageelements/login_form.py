from selenium.webdriver.common.by import By

from pageobjects.base_page import BasePage


class LoginForm(BasePage):
    LOGIN_FIELD = (By.XPATH, '//input[@data-test="username"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@data-test="password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@data-test="login-button"]')

    def enter_username(self, login: str):
        self.browser.find_element(*self.LOGIN_FIELD).send_keys(login)
        return self

    def enter_password(self, password: str):
        self.browser.find_element(*self.PASSWORD_FIELD).send_keys(password)
        return self
