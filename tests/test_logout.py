import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helper import Helper
from test_data import TestData
from locators import Locators


class TestLogout:

    def test_logout_from_my_account(self, driver):
        driver.get(TestData.LOGIN_PAGE_LINK)

        Helper.perform_login(driver)

        button_my_account = driver.find_element(*Locators.LOCATOR_MAIN_MY_ACCOUNT)
        button_my_account.click()

        WebDriverWait(driver, TestData.WAIT_TIME).until(
            EC.visibility_of_element_located(Locators.LOCATOR_MY_ACC_LOGOUT_BUTTON))

        button_logout = driver.find_element(*Locators.LOCATOR_MY_ACC_LOGOUT_BUTTON)
        button_logout.click()

        WebDriverWait(driver, TestData.WAIT_TIME).until(EC.url_to_be(TestData.LOGIN_PAGE_LINK))

        current_url = driver.current_url

        assert current_url == TestData.LOGIN_PAGE_LINK
