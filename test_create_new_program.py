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
Description    : This class is used to Create New Program
"""


class TestCreateNewProgram(ManagerBaseTest):
    ManagerAppPortal = ManagerPortal(driver)

    LOGGER.info('Creating New Program')

    def test_create_program(self):
        with allure.step("Reading test data"):
            data = ReadData()
            test_data = data.get_test_data()

        with allure.step("Logging to u-pass home page"):
            self.ManagerAppPortal.upass_portal_page()

        with allure.step("Clicking on Login to existing account button"):
            self.ManagerAppPortal.click_existing_account()

        with allure.step("Entering Username"):
            self.ManagerAppPortal.enter_username("saddikut.reddy@unisys.com")

        with allure.step("Entering Login Password"):
            self.ManagerAppPortal.enter_login_password(test_data["Login"]["Password"])

        with allure.step("Clicking on Signin button"):
            self.ManagerAppPortal.click_signin()

        with allure.step("Clicking on New Button"):
            self.ManagerAppPortal.click_new_button()

        with allure.step("Entering Program Name"):
            self.ManagerAppPortal.enter_new_program_name(test_data["Manager_App"]["program_name"])

        with allure.step("Clicking on Save Draft button"):
            self.ManagerAppPortal.click_save_draft_button()

        with allure.step("Verifying New Program"):
            self.ManagerAppPortal.verify_created_program()
