from selenium.webdriver.common.by import By

from base.browser import Browser
from pageelements.header import Header
from pageobjects.base_page import BasePage


class CheckoutSecondPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    QTY = (By.CLASS_NAME, "cart_quantity_label")
    DESCRIPTION = (By.CLASS_NAME, "cart_desc_label")
    CART_QUANTITY = (By.CLASS_NAME, "cart_quantity")
    ITEM_TITLE = (By.CLASS_NAME, "inventory_item_name")
    ITEM_DESC = (By.CLASS_NAME, "inventory_item_desc")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    PAYMENT_INFO_TITLE = (By.CLASS_NAME, "summary_value_label")
    PAYMENT_INFO_DELIVERY = (By.CLASS_NAME, "summary_info_label")
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.XPATH, '//button[@data-test="finish"]')
    CANCEL_BUTTON = (By.XPATH, '//button[@data-test="cancel"]')

    def __init__(self, browser: Browser, url: str):
        super().__init__(browser, url)
        self.headers = Header(self.browser, self.url)
