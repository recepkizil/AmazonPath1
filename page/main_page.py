from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import pytest


from base.pagebase import *


@pytest.mark.usefixtures("setup")
class MainPage(BasePage):


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


