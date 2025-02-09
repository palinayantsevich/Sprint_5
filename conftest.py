import pytest
from selenium import webdriver

from test_data import TestData


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(TestData.MAIN_PAGE_LINK)
    yield chrome_driver
    chrome_driver.quit()
