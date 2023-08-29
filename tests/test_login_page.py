import pytest

from base.settings import URL
from base.settings import (
    STANDARD_USER,
    LOCKED_OUT_USER,
    PROBLEM_USER,
    PERFORMANCE_GLITCH_USER,
    STANDARD_PASSWORD,
    WRONG_PASSWORD,
    EMPTY_STRING,
)
from pageobjects.login_page import LoginPage
from pageobjects.product_page import ProductPage


class TestLoginPage:
    def test_login_logo_is_loaded(self, browser):
        login_page = LoginPage(browser, URL)
        login_page.open()

        assert login_page.browser.is_visible(*login_page.LOGIN_LOGO)

    def test_login_form_is_loaded(self, browser):
        login_page = LoginPage(browser, URL)
        login_page.open()

        assert login_page.browser.is_visible(*login_page.LOGIN_FORM)

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, STANDARD_PASSWORD)])
    def test_successful_auth_with_standard_user(self, browser, login):
        assert not login.error_message_exist()

        product_page = ProductPage(browser, browser.current_url)

        assert product_page.browser.are_visible(*product_page.INVENTORY_ITEM_CARD)
        assert product_page.browser.is_visible(*product_page.headers.LOGO)

    @pytest.mark.parametrize(
        "username, password", [(LOCKED_OUT_USER, STANDARD_PASSWORD)]
    )
    def test_auth_with_locked_out_user(self, browser, login):
        assert (
            login.get_error_message_text()
            == "Epic sadface: Sorry, this user has been locked out."
        )

    @pytest.mark.parametrize("username, password", [(PROBLEM_USER, STANDARD_PASSWORD)])
    def test_auth_with_problem_user(self, browser, login):
        assert not login.error_message_exist()

        product_page = ProductPage(browser, browser.current_url)

        assert product_page.browser.are_visible(*product_page.INVENTORY_ITEM_CARD)
        assert product_page.browser.is_visible(*product_page.headers.LOGO)

    @pytest.mark.parametrize(
        "username, password", [(PERFORMANCE_GLITCH_USER, STANDARD_PASSWORD)]
    )
    def test_auth_with_performance_glitch_user(self, browser, login):
        assert not login.error_message_exist()

        product_page = ProductPage(browser, browser.current_url)

        assert product_page.browser.are_visible(*product_page.INVENTORY_ITEM_CARD)
        assert product_page.browser.is_visible(*product_page.headers.LOGO)

    @pytest.mark.parametrize(
        "username, password",
        [(LOCKED_OUT_USER, WRONG_PASSWORD), (WRONG_PASSWORD, LOCKED_OUT_USER)],
    )
    def test_auth_with_invalid_data(self, browser, login):
        assert (
            login.get_error_message_text()
            == "Epic sadface: Username and password do not match any user in this service"
        )

    @pytest.mark.parametrize("username, password", [(EMPTY_STRING, STANDARD_PASSWORD)])
    def test_auth_with_empty_username(self, browser, login):
        assert login.get_error_message_text() == "Epic sadface: Username is required"

    @pytest.mark.parametrize("username, password", [(STANDARD_USER, EMPTY_STRING)])
    def test_auth_with_empty_password(self, browser, login):
        assert login.get_error_message_text() == "Epic sadface: Password is required"
