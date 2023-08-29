from retry import retry
from typing import Optional, Iterable, Type

from selenium.common import (
    StaleElementReferenceException,
    WebDriverException,
    NoSuchElementException,
    ElementClickInterceptedException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class Browser:
    def __init__(self, driver):
        self.driver = driver

    @property
    def current_url(self):
        return self.driver.current_url

    def open(self, url: str):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def wait(
        self, timeout: int, ignored_exceptions: Optional[Iterable[Type[Exception]]]
    ):
        return WebDriverWait(
            driver=self.driver, timeout=timeout, ignored_exceptions=ignored_exceptions
        )

    @retry(
        (
            NoSuchElementException,
            ElementClickInterceptedException,
            WebDriverException,
            StaleElementReferenceException,
        ),
        tries=25,
        delay=0.5,
    )
    def find_element(self, find_by: By, locator: str) -> WebElement:
        return self.driver.find_element(find_by, locator)

    def find_elements(
        self, find_by: By, locator: str
    ) -> list[WebElement] | NoSuchElementException:
        list_of_elements = self.driver.find_elements(find_by, locator)
        if list_of_elements:
            return list_of_elements
        raise NoSuchElementException

    def is_visible(
        self, find_by: By, locator: str, locator_name: str | None = None
    ) -> WebElement:
        return self.wait(
            timeout=5,
            ignored_exceptions=(NoSuchElementException, StaleElementReferenceException),
        ).until(
            ec.visibility_of_element_located((find_by, locator)),
            locator_name,
        )

    def is_not_visible(
        self, find_by: By, locator: str, locator_name: str | None = None
    ) -> WebElement:
        return self.wait(
            timeout=5,
            ignored_exceptions=(NoSuchElementException, StaleElementReferenceException),
        ).until(
            ec.invisibility_of_element_located((find_by, locator)),
            locator_name,
        )

    def is_present(
        self, find_by: By, locator: str, locator_name: str | None = None
    ) -> WebElement:
        return self.wait(
            timeout=5,
            ignored_exceptions=(NoSuchElementException, StaleElementReferenceException),
        ).until(
            ec.presence_of_element_located((find_by, locator)),
            locator_name,
        )

    def is_not_present(
        self, find_by: By, locator: str, locator_name: str | None = None
    ) -> WebElement:
        return self.wait(
            timeout=5,
            ignored_exceptions=(NoSuchElementException, StaleElementReferenceException),
        ).until(
            ec.invisibility_of_element_located((find_by, locator)),
            locator_name,
        )

    def are_visible(
        self, find_by: By, locator: str, locator_name: str | None = None
    ) -> list[WebElement]:
        return self.wait(
            timeout=5,
            ignored_exceptions=(NoSuchElementException, StaleElementReferenceException),
        ).until(
            ec.visibility_of_all_elements_located((find_by, locator)),
            locator_name,
        )

    def are_present(
        self, find_by: By, locator: str, locator_name: str | None = None
    ) -> list[WebElement]:
        return self.wait(
            timeout=5,
            ignored_exceptions=(NoSuchElementException, StaleElementReferenceException),
        ).until(
            ec.presence_of_all_elements_located((find_by, locator)),
            locator_name,
        )

    def expected_text_to_be_present_in_element(
        self,
        find_by: By,
        locator: str,
        expected_value: str,
        locator_name: str | None = None,
    ) -> bool:
        return self.wait(
            timeout=5,
            ignored_exceptions=(NoSuchElementException, StaleElementReferenceException),
        ).until(
            ec.text_to_be_present_in_element((find_by, locator), expected_value),
            locator_name,
        )

    def click(self, find_by: By, locator: str) -> WebElement:
        return (
            self.wait(
                timeout=5,
                ignored_exceptions=(
                    NoSuchElementException,
                    StaleElementReferenceException,
                ),
            )
            .until(ec.visibility_of_element_located((find_by, locator)))
            .click()
        )
