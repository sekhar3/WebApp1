import allure
from utils.browser_config import driver
from POM.BaseTest.upass_manager_app import ManagerBaseTest
from POM.Portal.upass_manager import ManagerPortal
from POM.BaseTest.upass_holder import RegBaseTest
from POM.Portal.upass_holder_app import HolderPortal
import logging
from utils.read_data import ReadData
LOGGER = logging.getLogger(__name__)

"""
@author        : Srinivas Reddy
Description    : This class is used to create New Program
"""


class TestScanVerify(ManagerBaseTest, RegBaseTest):
    ManagerAppPortal = ManagerPortal(driver)
    upass_holder_portal = HolderPortal(driver)

    LOGGER.info('Creating New Program')

    def test_scan_verify_id(self):
        with allure.step("Reading test data"):
            data = ReadData()
            test_data = data.get_test_data()
            excel_data = data.get_excel_data(2, 2)
            excel_data1 = data.get_excel_data1(2, 2)

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

        with allure.step("Clicking on Save Draft Button"):
            self.ManagerAppPortal.click_save_draft_button()

        with allure.step("Verifying New Program"):
            self.ManagerAppPortal.verify_created_program()

        with allure.step("Click Program settings button"):
            self.ManagerAppPortal.click_program_settings()

        with allure.step("Clicking Edit button"):
            self.ManagerAppPortal.click_edit_button()

        with allure.step("Selecting Program Status Active"):
            self.ManagerAppPortal.select_the_program_status_active()

        with allure.step("Clicking on Save Button"):
            self.ManagerAppPortal.click_save_button()

        with allure.step("Clicking on Back Button"):
            self.ManagerAppPortal.click_back_button_program_settings()

        with allure.step("Clicking the directory page settings"):
            self.ManagerAppPortal.click_directory_page_settings()

        with allure.step("Clicking Edit button"):
            self.ManagerAppPortal.click_edit_button()

        with allure.step("Selecting Program Status Published"):
            self.ManagerAppPortal.select_program_published()

        with allure.step("Clicking on Save Button"):
            self.ManagerAppPortal.click_save_button()

        with allure.step("Clicking on Back Button"):
            self.ManagerAppPortal.click_back_button_directory_page_settings()

        with allure.step("Clicking on Scan Verify Button"):
            self.ManagerAppPortal.click_scan_verify_button()

        with allure.step("Clicking on Use Id Number Button"):
            self.ManagerAppPortal.click_switch_upass_holder()

        with allure.step("Login to U-Pass Page"):
            self.upass_holder_portal.upass_portal_page()

        with allure.step("Clicking on Login to existing account button"):
            self.upass_holder_portal.click_existing_account()

        with allure.step("Entering Username"):
            self.upass_holder_portal.enter_username(excel_data)

        with allure.step("Entering Password"):
            self.upass_holder_portal.enter_login_password(test_data["details"]["password"])

        with allure.step("Clicking create new login button"):
            self.upass_holder_portal.click_continue_signin()

        with allure.step("Getting User Unique Id"):
            self.upass_holder_portal.get_unique_id()

        with allure.step("Clicking on Use Id Number Button"):
            self.ManagerAppPortal.click_use_id_number()

        with allure.step("Entering Id Number"):
            self.ManagerAppPortal.enter_id_number(excel_data1)

        with allure.step("Clicking Verify Button"):
            self.ManagerAppPortal.click_verify_button()

        with allure.step("Clicking Notification Bell Icon"):
            self.upass_holder_portal.click_notification_bell_icon()

        with allure.step("Clicking See Request Button"):
            self.upass_holder_portal.click_see_request()

        with allure.step("Clicking Approve Once Button"):
            self.upass_holder_portal.click_approve_once()

        with allure.step("Verifying the result Pass or Not Pass"):
            self.ManagerAppPortal.verify_upass_result()






