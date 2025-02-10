import random
import string

from test_data import TestData
from locators import Locators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Helper:
    @staticmethod
    def generate_email_for_registration():
        length = 6
        random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        email_for_registration = 'palina_yant_18_' + random_part + '@' + 'test.com'
        return email_for_registration

    @staticmethod
    def generate_password_for_registration():
        length = 6
        password_for_registration = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        return password_for_registration

    @staticmethod
    def perform_login(driver):
        email_input = driver.find_element(*Locators.LOCATOR_LOGIN_EMAIL)
        email_input.send_keys(TestData.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.LOCATOR_LOGIN_PASSWORD)
        password_input.send_keys(TestData.AUTH_PASSWORD)

        button_login = driver.find_element(*Locators.LOCATOR_LOGIN_BUTTON)
        button_login.click()

    @staticmethod
    def check_loggedin_state(driver):
        WebDriverWait(driver, TestData.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.LOCATOR_MAIN_MAKE_ORDER))

        button_make_order = driver.find_element(*Locators.LOCATOR_MAIN_MAKE_ORDER)

        return button_make_order.is_displayed()
