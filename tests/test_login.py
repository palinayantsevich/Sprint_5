import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helper import Helper
from test_data import TestData
from locators import Locators


class TestLogin:

    def test_login_from_main_page(self, driver):
        goto_account_button = driver.find_element(*Locators.LOCATOR_MAIN_GOTO_ACC_BUTTON)
        goto_account_button.click()

        email_input = driver.find_element(*Locators.LOCATOR_LOGIN_EMAIL)
        email_input.send_keys(TestData.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.LOCATOR_LOGIN_PASSWORD)
        password_input.send_keys(TestData.AUTH_PASSWORD)

        button_login = driver.find_element(*Locators.LOCATOR_LOGIN_BUTTON)
        button_login.click()

        WebDriverWait(driver, TestData.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.LOCATOR_MAIN_MAKE_ORDER))

        button_make_order = driver.find_element(*Locators.LOCATOR_MAIN_MAKE_ORDER)

        assert button_make_order.is_displayed()

    def test_login_from_my_account(self, driver):
        button_my_account = driver.find_element(*Locators.LOCATOR_MAIN_MY_ACCOUNT)
        button_my_account.click()

        Helper.perform_login(driver)

        assert Helper.check_loggedin_state(driver)

    def test_login_from_registration_page(self, driver):
        driver.get(TestData.REGISTRATION_PAGE_LINK)

        login_button_reg_page = driver.find_element(*Locators.LOCATOR_REG_LOGIN_BUTTON)
        login_button_reg_page.click()

        Helper.perform_login(driver)

        assert Helper.check_loggedin_state(driver)

    def test_login_from_forgot_password(self, driver):
        driver.get(TestData.FORGOT_PASSWORD_LINK)

        login_button_forgot_pass_page = driver.find_element(*Locators.LOCATOR_FORGOT_PASSWORD_LOGIN_BUTTON)
        login_button_forgot_pass_page.click()

        Helper.perform_login(driver)

        assert Helper.check_loggedin_state(driver)
