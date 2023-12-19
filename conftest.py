import json
import allure
import pytest
from selenium import webdriver
from POM.BaseTest.selenium_driver import SeleniumDriver
from POM.BaseTest.DriverClass import WebDriverClass
import time
import logging

LOGGER = logging.getLogger(__name__)

"""
@author        : Sreenivas Reddy
Description    : This class is used as setup and tear down for browser and u-pass application
"""


@pytest.fixture(scope="class")
def beforeClass(request):
    with allure.step("Opening the Browser"):
        LOGGER.info('Entered Browser')
        driver1 = WebDriverClass()
        driver = driver1.getWebDriver("chrome")
        bp = SeleniumDriver(driver)
        f = open(r'..\..\Resources\Testdata.json')
        data = json.load(f)
        bp.launchWebPage(data["url"]["portal_url"])
        driver.implicitly_wait(20)
        driver.maximize_window()
        if request.cls is not None:
            request.cls.driver = driver
        yield driver
        time.sleep(2)
        driver.quit()


@pytest.yield_fixture()
def beforeMethod():
    print("Before Method")
    yield
    print("After Method")
