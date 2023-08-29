import pytest

from pageobjects.product_page import ProductPage
from base.settings import STANDARD_USER, STANDARD_PASSWORD
from pageobjects.product_detail_page import ProductDetailPage


class TestProductDetailPage:
    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_back_to_products_is_loaded(self, browser, product_detail_page):
        assert product_detail_page.browser.is_visible(
            *product_detail_page.BACK_TO_PRODUCTS_BUTTON
        )

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_detail_picture_is_loaded(self, browser, product_detail_page):
        assert product_detail_page.browser.is_visible(
            *product_detail_page.DETAIL_PICTURE
        )

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_detail_title_is_loaded(self, browser, product_detail_page):
        assert product_detail_page.browser.is_visible(*product_detail_page.DETAIL_TITLE)

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_detail_desc_is_loaded(self, browser, product_detail_page):
        assert product_detail_page.browser.is_visible(*product_detail_page.DETAIL_DESC)

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_detail_price_is_loaded(self, browser, product_detail_page):
        assert product_detail_page.browser.is_visible(*product_detail_page.DETAIL_PRICE)

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_add_to_cart_button_is_loaded(self, browser, product_detail_page):
        assert product_detail_page.browser.is_visible(
            *product_detail_page.ADD_TO_CART_BUTTON
        )

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_back_to_products(self, browser, product_detail_page):
        product_detail_page.browser.click(*product_detail_page.BACK_TO_PRODUCTS_BUTTON)
        product_page = ProductPage(browser, browser.current_url)

        assert product_detail_page.browser.is_not_visible(
            *product_detail_page.BACK_TO_PRODUCTS_BUTTON
        )
        assert product_page.browser.is_visible(*product_page.TITLE)

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_add_to_cart(self, browser, product_detail_page):
        product_detail_page.browser.click(*product_detail_page.ADD_TO_CART_BUTTON)

        assert product_detail_page.headers.get_count_items_in_cart() == 1
        assert product_detail_page.browser.expected_text_to_be_present_in_element(
            *product_detail_page.REMOVE_FROM_CART_BUTTON, expected_value="Remove"
        )
        assert product_detail_page.browser.is_not_visible(
            *product_detail_page.ADD_TO_CART_BUTTON
        )

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_remove_from_cart(self, browser, product_detail_page):
        product_detail_page.browser.click(*product_detail_page.ADD_TO_CART_BUTTON)

        assert product_detail_page.headers.get_count_items_in_cart() == 1

        product_detail_page.browser.click(*product_detail_page.REMOVE_FROM_CART_BUTTON)

        assert product_detail_page.browser.is_not_visible(
            *product_detail_page.headers.COUNT_ITEM_IN_CART
        )
        assert product_detail_page.browser.expected_text_to_be_present_in_element(
            *product_detail_page.ADD_TO_CART_BUTTON, expected_value="Add to cart"
        )
        assert product_detail_page.browser.is_not_visible(
            *product_detail_page.REMOVE_FROM_CART_BUTTON
        )

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_check_price(self, browser, login):
        product_page = ProductPage(browser, browser.current_url)
        price_on_product_page = product_page.get_prices_of_products()[0]
        product_page.browser.click(*product_page.INVENTORY_ITEM_PICTURE)
        product_detail_page = ProductDetailPage(browser, browser.current_url)
        price_on_detail_page = product_detail_page.get_price()

        assert price_on_detail_page == price_on_product_page

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_check_title(self, browser, login):
        product_page = ProductPage(browser, browser.current_url)
        title_on_product_page = product_page.get_titles_of_products()[0]
        product_page.browser.click(*product_page.INVENTORY_ITEM_PICTURE)
        product_detail_page = ProductDetailPage(browser, browser.current_url)
        title_on_detail_page = product_detail_page.get_title()

        assert title_on_detail_page == title_on_product_page

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_check_desc(self, browser, login):
        product_page = ProductPage(browser, browser.current_url)
        desc_on_product_page = product_page.get_descs_of_products()[0]
        product_page.browser.click(*product_page.INVENTORY_ITEM_PICTURE)
        product_detail_page = ProductDetailPage(browser, browser.current_url)
        desc_on_detail_page = product_detail_page.get_desc()

        assert desc_on_detail_page == desc_on_product_page
