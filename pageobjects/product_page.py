from selenium.webdriver.common.by import By

from base.browser import Browser
from pageelements.header import Header
from pageobjects.base_page import BasePage


class ProductPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    SORT_PRODUCT = (By.XPATH, '//select[@data-test="product_sort_container"]')
    SORT_PRODUCTS_FROM_A_TO_Z = (
        By.CSS_SELECTOR,
        '[data-test="product_sort_container"] :nth-child(1)',
    )
    SORT_PRODUCTS_FROM_Z_TO_A = (
        By.CSS_SELECTOR,
        '[data-test="product_sort_container"] :nth-child(2)',
    )
    SORT_PRODUCTS_FROM_LOW_TO_HIGH = (
        By.CSS_SELECTOR,
        '[data-test="product_sort_container"] :nth-child(3)',
    )
    SORT_PRODUCTS_FROM_HIGH_TO_LOW = (
        By.CSS_SELECTOR,
        '[data-test="product_sort_container"] :nth-child(4)',
    )
    INVENTORY_ITEM_CARD = (By.CLASS_NAME, "inventory_item")
    INVENTORY_ITEM_PICTURE = (By.CLASS_NAME, "inventory_item_img")
    INVENTORY_ITEM_TITLE = (By.CLASS_NAME, "inventory_item_name")
    INVENTORY_ITEM_DESC = (By.CLASS_NAME, "inventory_item_desc")
    INVENTORY_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTON = (
        By.XPATH,
        '//button[@data-test="add-to-cart-sauce-labs-backpack"]',
    )
    REMOVE_FROM_CART_BUTTON = (
        By.XPATH,
        '//button[@data-test="remove-sauce-labs-backpack"]',
    )

    def __init__(self, browser: Browser, url: str):
        super().__init__(browser, url)
        self.headers = Header(self.browser, self.url)

    def sort_products_from_a_to_z(self):
        self.browser.find_element(*self.SORT_PRODUCTS_FROM_A_TO_Z).click()
        return self

    def sort_products_from_z_to_a(self):
        self.browser.find_element(*self.SORT_PRODUCTS_FROM_Z_TO_A).click()
        return self

    def sort_products_from_low_to_high_price(self):
        self.browser.find_element(*self.SORT_PRODUCTS_FROM_LOW_TO_HIGH).click()
        return self

    def sort_products_from_high_to_low_price(self):
        self.browser.find_element(*self.SORT_PRODUCTS_FROM_HIGH_TO_LOW).click()
        return self

    def get_all_products(self):
        return self.browser.find_elements(*self.INVENTORY_ITEM_CARD)

    def get_titles_of_products(self):
        return [
            product.text
            for product in self.browser.find_elements(*self.INVENTORY_ITEM_TITLE)
        ]

    def get_prices_of_products(self):
        return [
            product.text
            for product in self.browser.find_elements(*self.INVENTORY_ITEM_PRICE)
        ]

    def get_descs_of_products(self):
        return [
            product.text
            for product in self.browser.find_elements(*self.INVENTORY_ITEM_DESC)
        ]
