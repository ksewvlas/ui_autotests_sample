import pytest

from pageobjects.cart_page import CartPage
from base.settings import STANDARD_USER, STANDARD_PASSWORD
from pageobjects.checkout_second_page import CheckoutSecondPage


class TestCheckoutPage:
    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_checkout_page_is_loaded(self, browser, checkout_page):
        assert checkout_page.browser.is_visible(*checkout_page.TITLE)
        assert checkout_page.browser.is_visible(*checkout_page.INPUT_FIRST_NAME)
        assert checkout_page.browser.is_visible(*checkout_page.INPUT_LAST_NAME)
        assert checkout_page.browser.is_visible(*checkout_page.INPUT_POSTAL_CODE)
        assert checkout_page.browser.is_visible(*checkout_page.CONTINUE_BUTTON)
        assert checkout_page.browser.is_visible(*checkout_page.CANCEL_BUTTON)

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_successful_filled(self, browser, checkout_page, fill_checkout_form):
        checkout_page.browser.click(*checkout_page.CONTINUE_BUTTON)
        checkout_second_page = CheckoutSecondPage(browser, browser.current_url)

        assert checkout_second_page.browser.is_visible(*checkout_second_page.TITLE)
        assert checkout_second_page.browser.is_visible(
            *checkout_second_page.FINISH_BUTTON
        )
        assert checkout_second_page.browser.is_visible(
            *checkout_second_page.CANCEL_BUTTON
        )

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_cancel_checkout(self, browser, checkout_page):
        checkout_page.browser.click(*checkout_page.CANCEL_BUTTON)
        cart_page = CartPage(browser, browser.current_url)

        assert cart_page.browser.is_visible(*cart_page.TITLE)
        assert cart_page.browser.is_visible(*cart_page.QTY)
        assert cart_page.browser.is_visible(*cart_page.DESCRIPTION)
        assert cart_page.browser.is_visible(*cart_page.CONTINUE_SHOPPING_BUTTON)
        assert cart_page.browser.is_visible(*cart_page.CHECKOUT_BUTTON)
