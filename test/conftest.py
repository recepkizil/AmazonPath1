import pytest
#from constants.homepage_constants import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def setup(request):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    driver.maximize_window()
    driver.get("http://www.amazon.com/")

    request.cls.driver = driver
    yield
    driver.quit()