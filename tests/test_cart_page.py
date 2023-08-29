import pytest

from pageobjects.cart_page import CartPage
from pageobjects.product_page import ProductPage
from pageobjects.checkout_page import CheckoutPage
from base.settings import STANDARD_USER, STANDARD_PASSWORD
from pageobjects.product_detail_page import ProductDetailPage


class TestCartPage:
    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_cart_page_is_loaded(self, browser, cart_page):
        assert cart_page.browser.is_visible(*cart_page.TITLE)
        assert cart_page.browser.is_visible(*cart_page.QTY)
        assert cart_page.browser.is_visible(*cart_page.DESCRIPTION)
        assert cart_page.browser.is_visible(*cart_page.CONTINUE_SHOPPING_BUTTON)
        assert cart_page.browser.is_visible(*cart_page.CHECKOUT_BUTTON)

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_add_product_to_cart(self, browser, login):
        product_page = ProductPage(browser, browser.current_url)
        product_page.browser.click(*product_page.ADD_TO_CART_BUTTON)

        assert product_page.headers.get_count_items_in_cart() == 1
        assert product_page.browser.expected_text_to_be_present_in_element(
            *product_page.REMOVE_FROM_CART_BUTTON, expected_value="Remove"
        )

        product_page.headers.browser.click(*product_page.headers.SHOPPING_CART)
        cart_page = CartPage(browser, browser.current_url)

        assert cart_page.browser.expected_text_to_be_present_in_element(
            *cart_page.CART_QUANTITY,
            expected_value=str(product_page.headers.get_count_items_in_cart())
        )
        assert (
            cart_page.get_titles_of_products()[0]
            == product_page.get_titles_of_products()[0]
        )
        assert (
            cart_page.get_descs_of_products()[0]
            == product_page.get_descs_of_products()[0]
        )
        assert (
            cart_page.get_prices_of_products()[0]
            == product_page.get_prices_of_products()[0]
        )

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_remove_product_from_cart(self, browser, login):
        product_page = ProductPage(browser, browser.current_url)
        product_page.browser.click(*product_page.ADD_TO_CART_BUTTON)

        assert product_page.headers.get_count_items_in_cart() == 1

        product_page.headers.browser.click(*product_page.headers.SHOPPING_CART)
        cart_page = CartPage(browser, browser.current_url)

        assert cart_page.browser.expected_text_to_be_present_in_element(
            *cart_page.CART_QUANTITY,
            expected_value=str(product_page.headers.get_count_items_in_cart())
        )
        assert (
            cart_page.get_titles_of_products()[0]
            == product_page.get_titles_of_products()[0]
        )
        assert (
            cart_page.get_descs_of_products()[0]
            == product_page.get_descs_of_products()[0]
        )
        assert (
            cart_page.get_prices_of_products()[0]
            == product_page.get_prices_of_products()[0]
        )

        cart_page.browser.click(*cart_page.REMOVE_FROM_CART_BUTTON)

        assert cart_page.headers.get_count_items_in_cart() == 0, "Cart is not empty."
        assert cart_page.browser.is_not_visible(*cart_page.CART_QUANTITY)
        assert cart_page.browser.is_not_visible(*cart_page.ITEM_TITLE)
        assert cart_page.browser.is_not_visible(*cart_page.ITEM_DESC)
        assert cart_page.browser.is_not_visible(*cart_page.ITEM_PRICE)
        assert cart_page.browser.is_not_visible(*cart_page.REMOVE_FROM_CART_BUTTON)

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_continue_shopping(self, browser, cart_page):
        cart_page.browser.click(*cart_page.CONTINUE_SHOPPING_BUTTON)
        product_page = ProductPage(browser, browser.current_url)

        assert product_page.browser.are_visible(*product_page.INVENTORY_ITEM_CARD)
        assert product_page.browser.is_visible(*product_page.headers.LOGO)

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_go_to_checkout(self, browser, cart_page):
        cart_page.browser.click(*cart_page.CHECKOUT_BUTTON)
        checkout_page = CheckoutPage(browser, browser.current_url)

        assert checkout_page.browser.is_visible(*checkout_page.TITLE)

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_go_to_detail_page_via_title_from_cart(self, browser, login):
        product_page = ProductPage(browser, browser.current_url)
        title_on_product_page = product_page.get_titles_of_products()[0]
        product_page.browser.click(*product_page.ADD_TO_CART_BUTTON)

        assert product_page.headers.get_count_items_in_cart() == 1

        product_page.headers.browser.click(*product_page.headers.SHOPPING_CART)
        cart_page = CartPage(browser, browser.current_url)
        title_on_cart_page = cart_page.get_titles_of_products()[0]
        cart_page.browser.click(*cart_page.ITEM_TITLE)

        assert title_on_product_page == title_on_cart_page

        product_detail_page = ProductDetailPage(browser, browser.current_url)
        title_on_detail_page = product_detail_page.get_title()

        assert title_on_cart_page == title_on_detail_page
        assert title_on_product_page == title_on_detail_page
