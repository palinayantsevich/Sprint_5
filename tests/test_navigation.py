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

        button_my_account = driver.find_element(*Locators.locator_main_my_account)
        button_my_account.click()

        WebDriverWait(driver, TestData.WAIT_TIME).until(EC.url_to_be(TestData.MY_ACCOUNT_LINK))

        current_url = driver.current_url

        assert current_url == TestData.MY_ACCOUNT_LINK

    def test_navigation_to_my_account_for_guest_user(self, driver):
        driver.get(TestData.MAIN_PAGE_LINK)

        button_my_account = driver.find_element(*Locators.locator_main_my_account)
        button_my_account.click()

        WebDriverWait(driver, TestData.WAIT_TIME).until(EC.url_to_be(TestData.LOGIN_PAGE_LINK))

        current_url = driver.current_url

        assert current_url == TestData.LOGIN_PAGE_LINK

    def test_navigation_from_my_acc_to_constructor(self, driver):
        driver.get(TestData.LOGIN_PAGE_LINK)
        Helper.perform_login(driver)

        button_my_account = driver.find_element(*Locators.locator_main_my_account)
        button_my_account.click()

        WebDriverWait(driver, TestData.WAIT_TIME).until(EC.url_to_be(TestData.MY_ACCOUNT_LINK))

        button_constructor = driver.find_element(*Locators.locator_my_acc_constructor_button)
        button_constructor.click()

        WebDriverWait(driver, TestData.WAIT_TIME).until(EC.url_to_be(TestData.MAIN_PAGE_LINK))

        current_url = driver.current_url

        assert current_url == TestData.MAIN_PAGE_LINK

    def test_navigation_from_my_acc_via_logo(self, driver):
        driver.get(TestData.LOGIN_PAGE_LINK)
        Helper.perform_login(driver)

        button_my_account = driver.find_element(*Locators.locator_main_my_account)
        button_my_account.click()

        WebDriverWait(driver, TestData.WAIT_TIME).until(EC.url_to_be(TestData.MY_ACCOUNT_LINK))

        header_logo = driver.find_element(*Locators.locator_my_acc_header_logo)
        header_logo.click()

        WebDriverWait(driver, TestData.WAIT_TIME).until(EC.url_to_be(TestData.MAIN_PAGE_LINK))

        current_url = driver.current_url

        assert current_url == TestData.MAIN_PAGE_LINK

    def test_navigation_to_buns(self, driver):
        driver.get(TestData.MAIN_PAGE_LINK)
        filing_section = driver.find_element(*Locators.locator_main_filings_section)
        filing_section.click()

        buns_section = driver.find_element(*Locators.locator_main_buns_section)
        buns_section.click()

        active_tab = driver.find_element(*Locators.locator_main_buns_check_selected_state)

        assert TestData.SELECTED_TAB_PROPERTY in active_tab.get_attribute('class')

    def test_navigation_to_sauces(self, driver):
        driver.get(TestData.MAIN_PAGE_LINK)

        sauces_section = driver.find_element(*Locators.locator_main_sauces_section)
        sauces_section.click()

        active_tab = driver.find_element(*Locators.locator_main_sauces_check_selected_state)

        assert TestData.SELECTED_TAB_PROPERTY in active_tab.get_attribute('class')

    def test_navigation_to_fillings(self, driver):
        driver.get(TestData.MAIN_PAGE_LINK)

        filing_section = driver.find_element(*Locators.locator_main_filings_section)
        filing_section.click()

        active_tab = driver.find_element(*Locators.locator_main_filings_check_selected_state)
        assert TestData.SELECTED_TAB_PROPERTY in active_tab.get_attribute('class')
