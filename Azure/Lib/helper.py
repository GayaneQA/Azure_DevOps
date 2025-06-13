
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Helper:
    def __init__(self, driver, test_logger):
        self.driver = driver
        self.test_logger = test_logger

    def open_new_page(self, url):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            self.test_logger.info(f"Opened page: {url}")
        except Exception as e:
            self.test_logger.error(f"Could not open {url}: {e}")

    def find_element(self, locator_tuple):
        locator, name = locator_tuple
        try:
            element = self.driver.find_element(*locator)
            self.test_logger.info(f"Found element: {name}")
            return element
        except NoSuchElementException:
            self.test_logger.error(f"Element not found: {name}")
            raise

    def find_elements(self, locator_tuple, timeout=10):
        locator, name = locator_tuple
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator))
            self.test_logger.info(f"Found elements: {name}")
            return elements
        except Exception as e:
            self.test_logger.error(f"{name} are not found: {e}")

    def find_element_and_click(self, locator_tuple, timeout=5):
        locator, name = locator_tuple
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator))
            elem.click()
            self.test_logger.info(f"Clicked on: {name}")
        except Exception as e:
            self.test_logger.error(f"{name} is not clickable: {e}")

    def find_element_send_keys(self, locator_tuple, text, timeout=5):
        locator, name = locator_tuple
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
            elem.send_keys(text)
            self.test_logger.info(f"Sent keys to: {name}")
        except Exception as e:
            self.test_logger.error(f"{name} could not receive keys: {e}")

    def driver_close(self):
        if self.driver:
            self.driver.quit()
            self.test_logger.info("Driver closed successfully.")
