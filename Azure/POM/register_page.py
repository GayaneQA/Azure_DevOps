from Lib.helper import Helper
from selenium.webdriver.common.by import By


class Register(Helper):
    register_button = ((
        By.XPATH, '//a[@id="nav_register"]'), "register_button")
    name_field = ((By.XPATH, '//input[@id="name"]'), "name_field")
    email_field = ((By.XPATH, '//input[@id="email"]'), "email_field")
    username_field = ((By.XPATH, '//input[@id="username"]'), "username_field")
    password_field = ((By.XPATH, '//input[@id="password"]'), "password_field")
    confirm_password_field = ((
        By.XPATH, '//input[@id="confirm"]'), "confirm_password_field")
    submit_button = ((By.XPATH, '//input[@type="submit"]'), "submit_button")
    flash_wrapper_el = ((
        By.XPATH, '//div[@id="flashwrapper"]'), "successfully registered")

    def register_user(self, name, email, username, password):
        self.find_element_and_click(self.register_button)
        self.find_element_send_keys(self.name_field, name)
        self.find_element_send_keys(self.email_field, email)
        self.find_element_send_keys(self.username_field, username)
        self.find_element_send_keys(self.password_field, password)
        self.find_element_send_keys(self.confirm_password_field, password)
        self.find_element_and_click(self.submit_button)

    def get_successfully_registered_text(self):
        return self.find_element(self.flash_wrapper_el).text
