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
Description    : This class is used to edit dependent additional profile information 
"""


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class TestDependentProfileInformation(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.upass_holder_portal = HolderPortal(self.driver)
        self.bp = SeleniumDriver(self.driver)

    @pytest.mark.run(order=56)
    def test_edit_dependent_add_info(self):
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
            self.upass_holder_portal.enter_login_password(test_data["Login"]["Password"])

        with allure.step("Clicking Continue button to Signin"):
            self.upass_holder_portal.click_continue_signin()

        with allure.step("Clicking Profile button"):
            self.upass_holder_portal.click_profile_tab()

        with allure.step("Clicking Dependents Account Details button"):
            self.upass_holder_portal.click_add_info_dependent()

        with allure.step("Clicking Dependents Basic Info Edit button"):
            self.upass_holder_portal.click_add_info_dependent_edit()

        with allure.step("Selecting Gender Male"):
            self.upass_holder_portal.enter_edit_sex()

        with allure.step("Selecting Race White "):
            self.upass_holder_portal.select_race()

        with allure.step("Selecting Ethnicity "):
            self.upass_holder_portal.select_ethnicity()

        with allure.step("Entering Insurance Provider Name"):
            self.upass_holder_portal.enter_insurance_provider_add_info(test_data["details"]["insurance provider"])

        with allure.step("Entering Member Id"):
            self.upass_holder_portal.enter_member_id_add_info(test_data["details"]["member id"])

        with allure.step("Entering Group Member"):
            self.upass_holder_portal.enter_group_number_add_info(test_data["details"]["group id"])

        with allure.step("Clicking Save button"):
            self.upass_holder_portal.click_save_btn()
