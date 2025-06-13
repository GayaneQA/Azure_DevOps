from Lib.helper import Helper
from selenium.webdriver.common.by import By


class Home_page(Helper):
    welcome_guest_el = ((
        By.XPATH, '//div[@id="welcome_text"]'), "welcome_guest")

    def get_welcome_guest_text(self):
        return self.find_element(self.welcome_guest_el).text
