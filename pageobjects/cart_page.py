from selenium.webdriver.common.by import By

from base.browser import Browser
from pageelements.header import Header
from pageobjects.base_page import BasePage


class CartPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    QTY = (By.CLASS_NAME, "cart_quantity_label")
    DESCRIPTION = (By.CLASS_NAME, "cart_desc_label")
    CART_QUANTITY = (By.CLASS_NAME, "cart_quantity")
    ITEM_TITLE = (By.CLASS_NAME, "inventory_item_name")
    ITEM_DESC = (By.CLASS_NAME, "inventory_item_desc")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, '//button[@data-test="continue-shopping"]')
    CHECKOUT_BUTTON = (By.XPATH, '//button[@data-test="checkout"]')
    REMOVE_FROM_CART_BUTTON = (
        By.XPATH,
        '//button[@data-test="remove-sauce-labs-backpack"]',
    )

    def __init__(self, browser: Browser, url: str):
        super().__init__(browser, url)
        self.headers = Header(self.browser, self.url)

    def get_all_products(self):
        return self.browser.find_elements(*self.ITEM_TITLE)

    def get_titles_of_products(self):
        return [
            product.text for product in self.browser.find_elements(*self.ITEM_TITLE)
        ]

    def get_descs_of_products(self):
        return [product.text for product in self.browser.find_elements(*self.ITEM_DESC)]

    def get_prices_of_products(self):
        return [
            product.text for product in self.browser.find_elements(*self.ITEM_PRICE)
        ]
