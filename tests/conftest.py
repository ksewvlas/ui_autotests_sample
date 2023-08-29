import os

import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options

from base.settings import URL
from pageobjects.cart_page import CartPage
from base.browser import Browser
from pageobjects.login_page import LoginPage
from pageobjects.product_page import ProductPage
from pageobjects.checkout_page import CheckoutPage
from pageobjects.product_detail_page import ProductDetailPage
from pageobjects.checkout_second_page import CheckoutSecondPage
from pageobjects.checkout_finish_page import CheckoutFinishPage

fake = Faker()


@pytest.fixture
def checkout_data():
    return {
        "first_name": fake.name(),
        "last_name": fake.name(),
        "postal_code": fake.postcode(),
    }


@pytest.fixture
def browser():
    options = chrome_options()
    options.add_argument("chrome")
    options.add_argument("-headless=new")
    options.add_argument("--start-maximized")

    if os.getenv("REMOTE"):
        driver = webdriver.Remote(
            options=options,
            command_executor="http://selenium__standalone-chrome:4444/wd/hub",
        )
    else:
        driver = webdriver.Chrome(options=options)

    browser = Browser(driver)
    yield browser
    browser.quit()


@pytest.fixture
def login(browser, username, password):
    login_page = LoginPage(browser, URL)
    login_page.open()
    login_page.login_form.enter_username(username)
    login_page.login_form.enter_password(password)
    login_page.login_form.browser.click(*login_page.login_form.LOGIN_BUTTON)
    return login_page


@pytest.fixture
def product_detail_page(browser, login):
    product_page = ProductPage(browser, browser.current_url)
    product_page.browser.click(*product_page.INVENTORY_ITEM_PICTURE)
    return ProductDetailPage(browser, browser.current_url)


@pytest.fixture
def cart_page(browser, login):
    product_page = ProductPage(browser, browser.current_url)
    product_page.headers.browser.click(*product_page.headers.SHOPPING_CART)
    return CartPage(browser, browser.current_url)


@pytest.fixture
def checkout_page(browser, cart_page):
    cart_page.browser.click(*cart_page.CHECKOUT_BUTTON)
    return CheckoutPage(browser, browser.current_url)


@pytest.fixture
def fill_checkout_form(browser, checkout_page, checkout_data):
    checkout_page.enter_first_name(checkout_data["first_name"])
    checkout_page.enter_last_name(checkout_data["last_name"])
    checkout_page.enter_postal_code(checkout_data["postal_code"])


@pytest.fixture
def checkout_second_page(browser, checkout_page, fill_checkout_form):
    checkout_page.browser.click(*checkout_page.CONTINUE_BUTTON)
    return CheckoutSecondPage(browser, browser.current_url)


@pytest.fixture
def checkout_finish_page(browser, checkout_second_page):
    checkout_second_page.browser.click(*checkout_second_page.FINISH_BUTTON)
    return CheckoutFinishPage(browser, browser.current_url)
