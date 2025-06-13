from Lib.helper import Helper
from selenium.webdriver.common.by import By


class Authorization(Helper):
    email_field = ((By.XPATH, '//input[@id="email"]'), "email_field")
    code_field = ((By.XPATH, '//input[@id="code"]'), "code_field")
    send_button = ((By.XPATH, '//button[@id="Send"]'), "send_button")

    def authorize(self, login, code):
        self.find_element_send_keys(self.email_field, login)
        self.find_element_send_keys(self.code_field, code)
        self.find_element_and_click(self.send_button)
