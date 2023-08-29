import pytest

from pageobjects.product_page import ProductPage
from base.settings import STANDARD_USER, STANDARD_PASSWORD
from pageobjects.product_detail_page import ProductDetailPage


class TestProductPage:
    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_title_page_is_loaded(self, browser, login):
        product_page = ProductPage(browser, browser.current_url)

        assert product_page.browser.is_visible(*product_page.TITLE)

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_sort_is_loaded(self, browser, login):
        product_page = ProductPage(browser, browser.current_url)

        assert product_page.browser.is_visible(*product_page.SORT_PRODUCT)

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_get_all_products(self, browser, login):
        product_page = ProductPage(browser, browser.current_url)
        products = product_page.get_all_products()

        assert product_page.browser.are_visible(*product_page.INVENTORY_ITEM_CARD)
        assert product_page.browser.is_visible(*product_page.headers.LOGO)
        assert len(products) > 0, "List of products is empty."

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_sort_products_from_a_to_z(self, browser, login):
        product_page = ProductPage(browser, browser.current_url)
        product_page.sort_products_from_a_to_z()
        product_titles = product_page.get_titles_of_products()

        for idx in range(len(product_titles) - 1):
            assert (
                product_titles[idx] <= product_titles[idx + 1]
            ), "Products are incorrect sort"

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_sort_products_from_z_to_a(self, browser, login):
        product_page = ProductPage(browser, browser.current_url)
        product_page.sort_products_from_z_to_a()
        product_titles = product_page.get_titles_of_products()

        for idx in range(len(product_titles) - 1):
            assert (
                product_titles[idx] >= product_titles[idx + 1]
            ), "Products are incorrect sort"

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_sort_products_from_low_to_high_price(self, browser, login):
        product_page = ProductPage(browser, browser.current_url)
        product_page.sort_products_from_low_to_high_price()
        product_prices = product_page.get_prices_of_products()

        for idx in range(len(product_prices) - 1):
            assert float(product_prices[idx][1:]) <= float(
                product_prices[idx + 1][1:]
            ), "Products are incorrect sort"

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_sort_products_from_high_to_low_price(self, browser, login):
        product_page = ProductPage(browser, browser.current_url)
        product_page.sort_products_from_high_to_low_price()
        product_prices = product_page.get_prices_of_products()

        for idx in range(len(product_prices) - 1):
            assert float(product_prices[idx][1:]) >= float(
                product_prices[idx + 1][1:]
            ), "Products are incorrect sort"

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_add_to_cart(self, browser, login):
        product_page = ProductPage(browser, browser.current_url)

        assert product_page.headers.get_count_items_in_cart() == 0, "Cart is not empty."
        assert product_page.browser.is_not_visible(
            *product_page.REMOVE_FROM_CART_BUTTON
        )
        assert product_page.browser.expected_text_to_be_present_in_element(
            *product_page.ADD_TO_CART_BUTTON, expected_value="Add to cart"
        )

        product_page.browser.click(*product_page.ADD_TO_CART_BUTTON)

        assert product_page.headers.get_count_items_in_cart() == 1
        assert product_page.browser.is_not_visible(*product_page.ADD_TO_CART_BUTTON)
        assert product_page.browser.expected_text_to_be_present_in_element(
            *product_page.REMOVE_FROM_CART_BUTTON, expected_value="Remove"
        )

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_remove_from_cart(self, browser, login):
        product_page = ProductPage(browser, browser.current_url)

        assert product_page.headers.get_count_items_in_cart() == 0, "Cart is not empty."

        product_page.browser.click(*product_page.ADD_TO_CART_BUTTON)

        assert product_page.headers.get_count_items_in_cart() == 1
        assert product_page.browser.is_not_visible(*product_page.ADD_TO_CART_BUTTON)
        assert product_page.browser.expected_text_to_be_present_in_element(
            *product_page.REMOVE_FROM_CART_BUTTON, expected_value="Remove"
        )

        product_page.browser.click(*product_page.REMOVE_FROM_CART_BUTTON)

        assert product_page.headers.get_count_items_in_cart() == 0, "Cart is not empty."
        assert product_page.browser.is_not_visible(
            *product_page.REMOVE_FROM_CART_BUTTON
        )
        assert product_page.browser.expected_text_to_be_present_in_element(
            *product_page.ADD_TO_CART_BUTTON, expected_value="Add to cart"
        )

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_go_to_detail_page_via_picture(self, browser, login):
        product_page = ProductPage(browser, browser.current_url)
        title_on_product_page = product_page.get_titles_of_products()[0]
        product_page.browser.click(*product_page.INVENTORY_ITEM_PICTURE)
        product_detail_page = ProductDetailPage(browser, browser.current_url)
        title_on_detail_page = product_detail_page.get_title()

        assert title_on_detail_page == title_on_product_page

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_go_to_detail_page_via_title(self, browser, login):
        product_page = ProductPage(browser, browser.current_url)
        title_on_product_page = product_page.get_titles_of_products()[0]
        product_page.browser.click(*product_page.INVENTORY_ITEM_TITLE)
        product_detail_page = ProductDetailPage(browser, browser.current_url)
        title_on_detail_page = product_detail_page.get_title()

        assert title_on_detail_page == title_on_product_page
