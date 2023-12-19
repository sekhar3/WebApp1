import unittest

import allure
import pytest

from POM.BaseTest.selenium_driver import SeleniumDriver
from POM.Portal.upass_holder_app import HolderPortal
import logging
from utils.read_data import ReadData

LOGGER = logging.getLogger(__name__)

"""
@author        : Srinivas Reddy
Description    : This class is used to Edit Basic Information
"""


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class TestEditBasicInfo(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.upass_holder_portal = HolderPortal(self.driver)
        self.bp = SeleniumDriver(self.driver)

    @pytest.mark.run(order=52)
    def test_edit_basic_info(self):
        with allure.step("Reading test data"):
            data = ReadData()
            test_data = data.get_test_data()
            excel_data = data.get_excel_data(2, 2)
        with allure.step("Logging to u-pass home page"):
            self.upass_holder_portal.upass_portal_page()

        with allure.step("Clicking on Login to existing account button"):
            self.upass_holder_portal.click_existing_account()

        with allure.step("Entering Username"):
            self.upass_holder_portal.enter_username(excel_data)

        with allure.step("Entering Password"):
            self.upass_holder_portal.enter_login_password(test_data["details"]["password"])

        with allure.step("Clicking Continue button to Signin"):
            self.upass_holder_portal.click_continue_signin()

        with allure.step("Clicking Profile button"):
            self.upass_holder_portal.click_profile_tab()

        with allure.step("Clicking Account Details button"):
            self.upass_holder_portal.click_account_details_tb()

        with allure.step("Clicking Edit button"):
            self.upass_holder_portal.click_basic_info_edit_btn()

        with allure.step("Editing Name "):
            self.upass_holder_portal.enter_basic_info_edit_name(test_data["details"]["edit_name"])

        with allure.step("Editing Date Of Birth "):
            self.upass_holder_portal.enter_basic_info_edit_birthday(test_data["details"]["edit_dob"])

        with allure.step("Clicking Save button"):
            self.upass_holder_portal.click_save_btn()
