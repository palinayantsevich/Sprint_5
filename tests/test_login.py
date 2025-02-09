import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helper import Helper
from test_data import TestData
from locators import Locators


class TestLogin:

    def test_login_from_main_page(self, driver):
        goto_account_button = driver.find_element(*Locators.locator_main_goto_acc_button)
        goto_account_button.click()

        email_input = driver.find_element(*Locators.locator_login_email)
        email_input.send_keys(TestData.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.locator_login_password)
        password_input.send_keys(TestData.AUTH_PASSWORD)

        button_login = driver.find_element(*Locators.locator_login_button)
        button_login.click()

        WebDriverWait(driver, TestData.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.locator_main_make_order))

        button_make_order = driver.find_element(*Locators.locator_main_make_order)

        assert button_make_order.is_displayed()

    def test_login_from_my_account(self, driver):
        button_my_account = driver.find_element(*Locators.locator_main_my_account)
        button_my_account.click()

        Helper.perform_login(driver)

        assert Helper.check_loggedin_state(driver)

    def test_login_from_registration_page(self, driver):
        driver.get(TestData.REGISTRATION_PAGE_LINK)

        login_button_reg_page = driver.find_element(*Locators.locator_reg_login_button)
        login_button_reg_page.click()

        Helper.perform_login(driver)

        assert Helper.check_loggedin_state(driver)

    def test_login_from_forgot_password(self, driver):
        driver.get(TestData.FORGOT_PASSWORD_LINK)

        login_button_forgot_pass_page = driver.find_element(*Locators.locator_forgot_password_login_button)
        login_button_forgot_pass_page.click()

        Helper.perform_login(driver)

        assert Helper.check_loggedin_state(driver)
