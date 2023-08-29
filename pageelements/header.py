from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

from pageobjects.base_page import BasePage


class Header(BasePage):
    BURGER_MENU_BUTTON = (By.XPATH, '//div[@id="react-burger-menu-btn"]')
    LOGO = (By.CLASS_NAME, "app_logo")
    SHOPPING_CART = (By.XPATH, '//div[@id="shopping_cart_container"]')
    COUNT_ITEM_IN_CART = (By.XPATH, '//span[@class="shopping_cart_badge"]')

    def get_count_items_in_cart(self) -> int:
        try:
            count = self.browser.find_element(*self.COUNT_ITEM_IN_CART).text
        except NoSuchElementException:
            count = 0
        return int(count)
