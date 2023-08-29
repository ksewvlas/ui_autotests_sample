from selenium.webdriver.common.by import By

from base.browser import Browser
from pageelements.header import Header
from pageobjects.base_page import BasePage


class ProductDetailPage(BasePage):
    BACK_TO_PRODUCTS_BUTTON = (By.XPATH, '//button[@data-test="back-to-products"]')
    DETAIL_PICTURE = (By.CLASS_NAME, "inventory_details_img_container")
    DETAIL_TITLE = (By.CLASS_NAME, "inventory_details_name")
    DETAIL_DESC = (By.CLASS_NAME, "inventory_details_desc")
    DETAIL_PRICE = (By.CLASS_NAME, "inventory_details_price")
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

    def get_price(self):
        return self.browser.find_element(*self.DETAIL_PRICE).text

    def get_title(self):
        return self.browser.find_element(*self.DETAIL_TITLE).text

    def get_desc(self):
        return self.browser.find_element(*self.DETAIL_DESC).text
