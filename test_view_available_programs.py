import time

import allure
from utils.browser_config import driver
from POM.BaseTest.upass_manager_app import ManagerBaseTest
from POM.Portal.upass_manager import ManagerPortal
import logging
from utils.read_data import ReadData
LOGGER = logging.getLogger(__name__)

"""
@author        : Srinivas Reddy
Description    : This class is used to create New User account 
"""


class TestProgramsDetails(ManagerBaseTest):
    ManagerAppPortal = ManagerPortal(driver)

    LOGGER.info('Creating New User account')

    def test_view_programs(self):
        with allure.step("Reading test data"):
            data = ReadData()
            test_data = data.get_test_data()

        with allure.step("Logging to u-pass home page"):
            self.ManagerAppPortal.upass_portal_page()

        with allure.step("Clicking on Login to existing account button"):
            self.ManagerAppPortal.click_existing_account()
            LOGGER.info("Login to existing button ")

        with allure.step("Entering Username"):
            self.ManagerAppPortal.enter_username("saddikut.reddy@unisys.com")

        with allure.step("Entering Login Password"):
            self.ManagerAppPortal.enter_login_password(test_data["Login"]["Password"])

        with allure.step("Clicking on Signin button"):
            self.ManagerAppPortal.click_signin()

        with allure.step("Clicking on Menu button"):
            self.ManagerAppPortal.click_menu_button()

        with allure.step("Clicking Program dropdown button"):
            self.ManagerAppPortal.select_program_dropdown_btn()

        with allure.step("Selecting Program SHS"):
            self.ManagerAppPortal.click_program_shs()

        with allure.step("Verifying Available Programs"):
            self.ManagerAppPortal.verify_view_programs()