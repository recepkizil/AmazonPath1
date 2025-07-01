import pytest
from time import sleep

from base.pagebase import BasePage
from page import*
from page.login_page import LoginPage
from page.main_page import *
from page.search_result_page import SearchResultPage


@pytest.mark.usefixtures("setup")
class TestAmazonPage():

    current_url = "https://www.amazon.com/"
    SEARCH_RESULT = (By.CSS_SELECTOR, ".a-color-state.a-text-bold")

    def test_amazon_page(self):
        pagebase = BasePage(self.driver)
        mainpage = MainPage(self.driver)
        loginpage = LoginPage(self.driver)
        searchresultpage = SearchResultPage(self.driver)

        #Anasayfanın açıldığını doğrula
        assert self.driver.current_url == "https://www.amazon.com/", f"Expected 'https://www.amazon.com/', but found '{self.driver.current_url}'"

        #login kısmına tıkla
        mainpage.click_sign_in()

        #email gir
        loginpage.enter_email("testerhesabim@gmail.com")

        #continue butonuna tıkla
        loginpage.click_continue()

        #şifre gir
        loginpage.enter_password("Receprecep123.")

        #signin tıkla
        loginpage.click_sign_in()

        #searchbar'a tıkla ve samsung yaz
        mainpage.search_samsung()

        #samsug sonuçlarının gösterildiğini doğrula
        searchresultpage.verify_title_contains_samsung()

        #ikinci sayfaya geç
        searchresultpage.go_to_second_page()






