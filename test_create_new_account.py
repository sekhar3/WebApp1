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


class TestCreateAccount(ManagerBaseTest):
    ManagerAppPortal = ManagerPortal(driver)

    LOGGER.info('Creating New User account')

    def test_create_account(self):
        with allure.step("Reading test data"):
            data = ReadData()
            test_data = data.get_test_data()

        with allure.step("Logging to u-pass home page"):
            self.ManagerAppPortal.upass_portal_page()

        with allure.step("Clicking create new login button"):
            self.ManagerAppPortal.click_create_new_login_btn()

        with allure.step("Entering Full name"):
            self.ManagerAppPortal.enter_full_legal_name()

        with allure.step("Entering Email"):
            self.ManagerAppPortal.enter_Email()

        with allure.step("Entering date of birth"):
            self.ManagerAppPortal.enter_birthdate(test_data["details"]["dob"])

        with allure.step("Entering Phone Number"):
            self.ManagerAppPortal.enter_phone_number(test_data["details"]["phone"])

        with allure.step("Entering Password"):
            self.ManagerAppPortal.enter_password(test_data["details"]["password"])

        with allure.step("Entering confirm password"):
            self.ManagerAppPortal.enter_Confirm_password(test_data["details"]["password"])

        with allure.step("Clicking Continue button"):
            self.ManagerAppPortal.click_continue()

        with allure.step("Clicking Continue button"):
            self.ManagerAppPortal.click_continue_button()

        with allure.step("Clicking Go To U-pass button"):
            self.ManagerAppPortal.click_go_to_upass()

        with allure.step("Clicking Go To U-pass button"):
            self.ManagerAppPortal.verify_created_account()
