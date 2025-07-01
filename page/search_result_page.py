from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import pytest
from base.pagebase import *


@pytest.mark.usefixtures("setup")
class SearchResultPage(BasePage):
    SECOND_PAGE = (By.CSS_SELECTOR, "a[aria-label='Go to page 2']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_sign_in(self):
        SIGN_IN_BTN = (By.ID, "nav-link-accountList-nav-line-1")
        self.click_element(SIGN_IN_BTN)

    def search_samsung(self):
        SEARCHBAR = (By.ID, "twotabsearchtextbox")
        SEARCH_BTN = (By.ID, "nav-search-submit-button")
        self.click_element(SEARCHBAR)
        self.wait_element_visibility(SEARCHBAR).send_keys("samsung")
        self.click_element(SEARCH_BTN)

    def verify_title_contains_samsung(self):
        title = self.driver.title.lower()
        assert "samsung" in title, f"'samsung' not found in title: {title}"

    def go_to_second_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        second_page = self.wait_element_visibility(self.SECOND_PAGE)
        self.scroll_until_element(self.SECOND_PAGE)
        second_page.click()
        assert "page=2" in self.driver.current_url.lower(), f"'page=2' not found in URL: {self.driver.current_url}"




