import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helper import Helper
from test_data import TestData
from locators import Locators


class TestNavigation:

    def test_navigation_to_my_account_for_loggedin_user(self, driver):
        driver.get(TestData.LOGIN_PAGE_LINK)
        Helper.perform_login(driver)

        button_my_account = driver.find_element(*Locators.LOCATOR_MAIN_MY_ACCOUNT)
        button_my_account.click()

        WebDriverWait(driver, TestData.WAIT_TIME).until(EC.url_to_be(TestData.MY_ACCOUNT_LINK))

        current_url = driver.current_url

        assert current_url == TestData.MY_ACCOUNT_LINK

    def test_navigation_to_my_account_for_guest_user(self, driver):
        driver.get(TestData.MAIN_PAGE_LINK)

        button_my_account = driver.find_element(*Locators.LOCATOR_MAIN_MY_ACCOUNT)
        button_my_account.click()

        WebDriverWait(driver, TestData.WAIT_TIME).until(EC.url_to_be(TestData.LOGIN_PAGE_LINK))

        current_url = driver.current_url

        assert current_url == TestData.LOGIN_PAGE_LINK

    def test_navigation_from_my_acc_to_constructor(self, driver):
        driver.get(TestData.LOGIN_PAGE_LINK)
        Helper.perform_login(driver)

        button_my_account = driver.find_element(*Locators.LOCATOR_MAIN_MY_ACCOUNT)
        button_my_account.click()

        WebDriverWait(driver, TestData.WAIT_TIME).until(EC.url_to_be(TestData.MY_ACCOUNT_LINK))

        button_constructor = driver.find_element(*Locators.LOCATOR_MY_ACC_CONSTRUCTOR_BUTTON)
        button_constructor.click()

        WebDriverWait(driver, TestData.WAIT_TIME).until(EC.url_to_be(TestData.MAIN_PAGE_LINK))

        current_url = driver.current_url

        assert current_url == TestData.MAIN_PAGE_LINK

    def test_navigation_from_my_acc_via_logo(self, driver):
        driver.get(TestData.LOGIN_PAGE_LINK)
        Helper.perform_login(driver)

        button_my_account = driver.find_element(*Locators.LOCATOR_MAIN_MY_ACCOUNT)
        button_my_account.click()

        WebDriverWait(driver, TestData.WAIT_TIME).until(EC.url_to_be(TestData.MY_ACCOUNT_LINK))

        header_logo = driver.find_element(*Locators.LOCATOR_MY_ACC_HEADER_LOGO)
        header_logo.click()

        WebDriverWait(driver, TestData.WAIT_TIME).until(EC.url_to_be(TestData.MAIN_PAGE_LINK))

        current_url = driver.current_url

        assert current_url == TestData.MAIN_PAGE_LINK

    def test_navigation_to_buns(self, driver):
        driver.get(TestData.MAIN_PAGE_LINK)
        filing_section = driver.find_element(*Locators.LOCATOR_MAIN_FILINGS_SECTION)
        filing_section.click()

        buns_section = driver.find_element(*Locators.LOCATOR_MAIN_BUNS_SECTION)
        buns_section.click()

        active_tab = driver.find_element(*Locators.LOCATOR_MAIN_BUNS_CHECK_SELECTED_STATE)

        assert TestData.SELECTED_TAB_PROPERTY in active_tab.get_attribute('class')

    def test_navigation_to_sauces(self, driver):
        driver.get(TestData.MAIN_PAGE_LINK)

        sauces_section = driver.find_element(*Locators.LOCATOR_MAIN_SAUCES_SECTION)
        sauces_section.click()

        active_tab = driver.find_element(*Locators.LOCATOR_MAIN_SAUCES_CHECK_SELECTED_STATE)

        assert TestData.SELECTED_TAB_PROPERTY in active_tab.get_attribute('class')

    def test_navigation_to_fillings(self, driver):
        driver.get(TestData.MAIN_PAGE_LINK)

        filing_section = driver.find_element(*Locators.LOCATOR_MAIN_FILINGS_SECTION)
        filing_section.click()

        active_tab = driver.find_element(*Locators.LOCATOR_MAIN_FILINGS_CHECK_SELECTED_STATE)
        assert TestData.SELECTED_TAB_PROPERTY in active_tab.get_attribute('class')
