import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from test_data import TestData
from helper import Helper


class TestRegistration:

    def test_registration_success(self, driver):
        driver.get(TestData.REGISTRATION_PAGE_LINK)

        name_reg_input = driver.find_element(*Locators.locator_reg_name)
        name_reg_input.send_keys(TestData.USER_NAME_REGISTRATION)

        email_reg_input = driver.find_element(*Locators.locator_reg_email)
        email_reg_input.send_keys(Helper.generate_email_for_registration())

        password_reg_input = driver.find_element(*Locators.locator_reg_password)
        password_reg_input.send_keys(Helper.generate_password_for_registration())

        button_reg = driver.find_element(*Locators.locator_reg_button)
        button_reg.click()

        WebDriverWait(driver, TestData.WAIT_TIME).until(EC.url_to_be(TestData.LOGIN_PAGE_LINK))

        current_url = driver.current_url

        assert current_url == TestData.LOGIN_PAGE_LINK

    def test_registration_incorrect_password_error(self, driver):
        driver.get(TestData.REGISTRATION_PAGE_LINK)

        name_reg_input = driver.find_element(*Locators.locator_reg_name)
        name_reg_input.send_keys(TestData.USER_NAME_REGISTRATION)

        email_reg_input = driver.find_element(*Locators.locator_reg_email)
        email_reg_input.send_keys(Helper.generate_email_for_registration())

        password_reg_input = driver.find_element(*Locators.locator_reg_password)
        password_reg_input.send_keys(TestData.PASSWORD_REGISTRATION_ERROR)

        button_reg = driver.find_element(*Locators.locator_reg_button)
        button_reg.click()

        WebDriverWait(driver, TestData.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.locator_reg_password_error))

        registration_error = driver.find_element(*Locators.locator_reg_password_error)

        assert registration_error.is_displayed()
