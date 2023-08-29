import pytest

from pageobjects.cart_page import CartPage
from pageobjects.product_page import ProductPage
from pageobjects.checkout_page import CheckoutPage
from base.settings import STANDARD_USER, STANDARD_PASSWORD
from pageobjects.product_detail_page import ProductDetailPage
from pageobjects.checkout_second_page import CheckoutSecondPage
from pageobjects.checkout_finish_page import CheckoutFinishPage


class TestCheckoutSecondPage:
    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_checkout_second_page_is_loaded(self, browser, checkout_second_page):
        assert checkout_second_page.browser.is_visible(*checkout_second_page.TITLE)
        assert checkout_second_page.browser.is_visible(*checkout_second_page.QTY)
        assert checkout_second_page.browser.is_visible(
            *checkout_second_page.DESCRIPTION
        )
        assert checkout_second_page.browser.is_visible(
            *checkout_second_page.PAYMENT_INFO_TITLE
        )
        assert checkout_second_page.browser.is_visible(
            *checkout_second_page.PAYMENT_INFO_DELIVERY
        )
        assert checkout_second_page.browser.is_visible(*checkout_second_page.ITEM_TOTAL)
        assert checkout_second_page.browser.is_visible(*checkout_second_page.TAX)
        assert checkout_second_page.browser.is_visible(*checkout_second_page.TOTAL)
        assert checkout_second_page.browser.is_visible(
            *checkout_second_page.FINISH_BUTTON
        )
        assert checkout_second_page.browser.is_visible(
            *checkout_second_page.CANCEL_BUTTON
        )

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_go_to_detail_page_via_title(self, browser, login, checkout_data):
        product_page = ProductPage(browser, browser.current_url)
        title_on_product_page = product_page.get_titles_of_products()[0]
        product_page.browser.click(*product_page.ADD_TO_CART_BUTTON)

        assert product_page.headers.get_count_items_in_cart() == 1

        product_page.headers.browser.click(*product_page.headers.SHOPPING_CART)

        cart_page = CartPage(browser, browser.current_url)
        title_on_cart_page = cart_page.get_titles_of_products()[0]
        cart_page.browser.click(*cart_page.CHECKOUT_BUTTON)
        checkout_page = CheckoutPage(browser, browser.current_url)
        checkout_page.enter_first_name(checkout_data["first_name"])
        checkout_page.enter_last_name(checkout_data["last_name"])
        checkout_page.enter_postal_code(checkout_data["postal_code"])
        checkout_page.browser.click(*checkout_page.CONTINUE_BUTTON)
        checkout_second_page = CheckoutSecondPage(browser, browser.current_url)
        title_on_checkout_second_page = checkout_second_page.browser.find_element(
            *checkout_second_page.ITEM_TITLE
        ).text
        checkout_second_page.browser.click(*checkout_second_page.ITEM_TITLE)
        product_detail_page = ProductDetailPage(browser, browser.current_url)
        title_on_detail_page = product_detail_page.get_title()

        assert title_on_checkout_second_page == title_on_detail_page
        assert title_on_checkout_second_page == title_on_cart_page
        assert title_on_checkout_second_page == title_on_product_page

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_cancel_checkout(self, browser, checkout_second_page):
        checkout_second_page.browser.click(*checkout_second_page.CANCEL_BUTTON)
        product_page = ProductPage(browser, browser.current_url)

        assert product_page.browser.are_visible(*product_page.INVENTORY_ITEM_CARD)
        assert product_page.browser.is_visible(*product_page.headers.LOGO)

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_finish_checkout(self, browser, checkout_second_page):
        checkout_second_page.browser.click(*checkout_second_page.FINISH_BUTTON)
        finish_page = CheckoutFinishPage(browser, browser.current_url)

        assert finish_page.browser.is_visible(*finish_page.PONY_EXPRESS_PICTURE)
