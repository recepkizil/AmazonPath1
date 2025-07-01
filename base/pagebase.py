from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from constants.homepage_constants import *
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    """Base class to initialize the base page"""

    def __init__(self, driver):
        self.driver = driver  # Initializes the WebDriver instance

    def wait_element_visibility(self, locator):
        # Waits until the element is visible on the page
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))

    def wait_elements_visibility(self, locator):
        # Waits until all elements matching the locator are visible
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(locator))

    def wait_element_text(self, locator, text, timeout=20):
        # Waits until the element contains the specified text
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    def scroll_until_element(self, locator):
        # Scrolls to the element until it is in view
        ActionChains(self.driver).move_to_element(self.wait_element_visibility(locator)).perform()

    def scroll_and_click_to_element(self, locator):
        # Scrolls to the element and performs a click action
        ActionChains(self.driver).move_to_element(self.wait_element_visibility(locator)).click().perform()

    def click_element(self, locator):
        # Waits for the element to be visible and clicks it
        self.wait_element_visibility(locator).click()

    def get_url(self, url):
        # Navigates to the given URL
        self.driver.get(url)

    def find_element(self, locator):
        # Finds a single element using the provided locator
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        # Finds multiple elements using the provided locator
        return self.driver.find_elements(*locator)

    def take_screenshot(self, file_path):
        # Takes a screenshot and saves it to the specified file path
        self.driver.save_screenshot(file_path)

    def scroll_down(self, pixels):
        # Scrolls down the page by the specified number of pixels
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def switch_to_window(self, page):
        # Switches to a different browser window by index
        self.driver.switch_to.window(self.driver.window_handles[page])

    def accept_all_cookies(self):
        # Clicks the 'Accept All Cookies' button
        self.click_element(ACCEPT_ALL_COOKIES)

    def get_element_index(self, locator, index):
        # Returns the element at the specified index from a list of elements
        return self.find_elements(locator)[index]
