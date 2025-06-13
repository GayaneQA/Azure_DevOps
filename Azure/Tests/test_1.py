import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import url
from config import login_url
from config import home_page_url
from Lib.helper import Helper
from POM.enter_qwallity_page import Authorization
from POM.home_page import Home_page
from POM.register_page import Register
from POM.login_page import Login
from Test_Data import test_data


def test_1(test_driver, test_logger):

    author_obj = Authorization(test_driver, test_logger)
    home_page_obj = Home_page(test_driver, test_logger)
    helper = Helper(test_driver, test_logger)
    register_obj = Register(test_driver, test_logger)
    login_obj = Login(test_driver, test_logger)
    helper.open_new_page(url)
    test_logger.info("Started authorization test")
    author_obj.authorize(test_data.login, test_data.code)
    text = home_page_obj.get_welcome_guest_text()
    assert "Welcome Guest!" in text
    test_logger.info("Finished authorization test")
    test_logger.info('Test passed.')
    helper.open_new_page(home_page_url)
    test_logger.info("Started registration test")
    register_obj.register_user(
        test_data.name, test_data.email,
        test_data.username, test_data.password)
    text = register_obj.get_successfully_registered_text()
    assert "Your account has been successfully registered." in text
    test_logger.info("Finished registration test")
    test_logger.info("Test passed.")
    helper.open_new_page(login_url)
    test_logger.info("Started login test")
    logout_element = login_obj.login_user(
        test_data.username, test_data.password)
    assert logout_element is not None, (
        "Logout button not found, login may have failed")
    test_logger.info("Login successful")
    test_logger.info("Finished login test")
