from Lib.helper import Helper
from selenium.webdriver.common.by import By


class Login(Helper):
    login_button = ((By.XPATH, '//a[@id="nav_login"]'), "login_button")
    username_field = ((By.XPATH, '//input[@id="username"]'), "username_field")
    password_field = ((By.XPATH, '//input[@id="password"]'), "password_field")
    log_in_button = ((
        By.XPATH, '//button[@id="submit_login_page"]'), "login_button")
    log_out_button = ((By.XPATH, '//a[@id="logout"]'), "log_out_button")

    def login_user(self, username, password):
        self.find_element_send_keys(self.username_field, username)
        self.find_element_send_keys(self.password_field, password)
        self.find_element_and_click(self.log_in_button)

        return self.find_element(self.log_out_button)
