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
Description    : This class is used to create Add Dependents 
"""


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class TestAddDependent(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.upass_holder_portal = HolderPortal(self.driver)
        self.bp = SeleniumDriver(self.driver)

    LOGGER.info('Add Dependents')

    @pytest.mark.run(order=2)
    def test_add_dependent(self):
        with allure.step("Reading test data"):
            data = ReadData()
            test_data = data.get_test_data()
            excel_data = data.get_excel_data(2, 2)

        with allure.step("Login to U-Pass home Page"):
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

        with allure.step("Clicking Add Dependents button"):
            self.upass_holder_portal.click_dependents_add_btn()

        with allure.step("Entering Dependent name"):
            self.upass_holder_portal.enter_dependent_name(test_data["details"]["dependent_name1"])

        with allure.step("Entering Dependent Date of Birth"):
            self.upass_holder_portal.click_dependent_birthday(test_data["details"]["dependent_dob"])

        with allure.step("Clicking Save button"):
            self.upass_holder_portal.click_save_dependent()

        with allure.step("Clicking Dependents Account Details button"):
            self.upass_holder_portal.click_dependent_account_details()

        with allure.step("Clicking Dependents Basic Info Edit button"):
            self.upass_holder_portal.click_basic_info_edit_dependent()

        with allure.step("Entering Dependent Name"):
            self.upass_holder_portal.enter_name_dependent(test_data["details"]["dependent_name"])

        with allure.step("Entering Dependent Date of Birth"):
            self.upass_holder_portal.enter_dob_dependent(test_data["details"]["dependent_dob1"])

        with allure.step("Clicking Save button"):
            self.upass_holder_portal.click_save_dependent()

        with allure.step("Verifying Dependent "):
            self.upass_holder_portal.Verify_dependent()
