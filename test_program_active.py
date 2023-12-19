import allure
from utils.browser_config import driver
from POM.BaseTest.upass_manager_app import ManagerBaseTest
from POM.Portal.upass_manager import ManagerPortal
import logging
from utils.read_data import ReadData


LOGGER = logging.getLogger(__name__)

"""
    @author     : Somasekhar
    Description : This class is used to change the program status inactive to active
"""


class TestProgramActive(ManagerBaseTest):
    ManagerAppPortal = ManagerPortal(driver)

    def test_program_active(self):
        with allure.step("Reading test data"):
            data = ReadData()
            test_data = data.get_test_data()

        with allure.step("Logging to u-pass home page"):
            self.ManagerAppPortal.upass_portal_page()

        with allure.step("Clicking on Login to existing account button"):
            self.ManagerAppPortal.click_existing_account()
            LOGGER.info("Login to existing button ")

        with allure.step("Entering Username"):
            self.ManagerAppPortal.enter_username("potturu.naidu@unisys.com")

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

        with allure.step("Click Program settings button"):
            self.ManagerAppPortal.click_program_settings()

        with allure.step("Clicking Edit button"):
            self.ManagerAppPortal.click_edit_button()

        with allure.step("Selecting the program status is Active"):
            self.ManagerAppPortal.select_the_program_status_active()

        with allure.step("Clicking the save button"):
            self.ManagerAppPortal.click_save_button()

        with allure.step("Verifying the program update message"):
            self.ManagerAppPortal.verify_the_program_update()

        with allure.step("Clicking back button in program settings"):
            self.ManagerAppPortal.click_back_button_program_settings()

        with allure.step("Clicking cross mark in program landing page"):
            self.ManagerAppPortal.click_cross_mark()

        with allure.step("Clicking on Menu button"):
            self.ManagerAppPortal.click_menu_button()

        with allure.step("Clicking Program dropdown button"):
            self.ManagerAppPortal.select_program_dropdown_btn()

        with allure.step("Selecting Program SHS"):
            self.ManagerAppPortal.click_program_shs()

        with allure.step("Verifying Active Programs"):
            self.ManagerAppPortal.verify_active_programs()
