import json
import os
import allure
import pytest
from utils.browser_config import driver
from time import sleep
import logging

LOGGER = logging.getLogger(__name__)

"""
@author        : Sreenivas reddy
Description    : This class is used as setup and tear down for browser
"""


class ManagerBaseTest:

    @pytest.fixture(autouse=True, scope="session")
    def open_browser(self, request):
        with allure.step("Opening the Browser"):
            LOGGER.info('Entered Browser')
            driver.delete_all_cookies()
            driver.maximize_window()
            f = open(r'..\..\Resources\Testdata.json')
            data = json.load(f)
            driver.get(data["url"]["manager_url"])
            driver.implicitly_wait(20)

        def close_browser():
            with allure.step("Closing the Browser"):
                sleep(1)
                driver.quit()
                os.system("allure generate..\..\Reports")

        request.addfinalizer(close_browser)
