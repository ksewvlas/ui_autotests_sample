import pytest

from pageobjects.product_page import ProductPage
from base.settings import STANDARD_USER, STANDARD_PASSWORD


class TestCheckoutFinishPage:
    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_checkout_finish_page_is_loaded(self, browser, checkout_finish_page):
        assert checkout_finish_page.browser.is_visible(*checkout_finish_page.TITLE)
        assert checkout_finish_page.browser.is_visible(*checkout_finish_page.HEADER)
        assert checkout_finish_page.browser.is_visible(
            *checkout_finish_page.DESCRIPTION
        )
        assert checkout_finish_page.browser.is_visible(
            *checkout_finish_page.PONY_EXPRESS_PICTURE
        )
        assert checkout_finish_page.browser.is_visible(
            *checkout_finish_page.BACK_HOME_BUTTON
        )

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_go_back_home(self, browser, checkout_finish_page):
        checkout_finish_page.browser.click(*checkout_finish_page.BACK_HOME_BUTTON)
        product_page = ProductPage(browser, browser.current_url)

        assert product_page.browser.are_visible(*product_page.INVENTORY_ITEM_CARD)
        assert product_page.browser.is_visible(*product_page.headers.LOGO)
