from selenium.webdriver.common.by import By
import pytest


from base.pagebase import *


@pytest.mark.usefixtures("setup")
class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "ap_email_login")
    CONTINUE_BTN = (By.CSS_SELECTOR, "input[type='submit']")
    PASSWORD_INPUT = (By.ID, "ap_password")
    SIGN_IN_BTN = (By.ID, "signInSubmit")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_email(self, email):
        self.wait_element_visibility(self.EMAIL_INPUT).send_keys(email)

    def click_continue(self):
        self.wait_element_visibility(self.CONTINUE_BTN).click()

    def enter_password(self, password):
        self.wait_element_visibility(self.PASSWORD_INPUT).send_keys(password)

    def click_sign_in(self):
        self.wait_element_visibility(self.SIGN_IN_BTN).click()