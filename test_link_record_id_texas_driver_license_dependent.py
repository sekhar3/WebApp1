import unittest

import allure
import pytest

from POM.BaseTest.selenium_driver import SeleniumDriver
from POM.Portal.upass_holder_app import HolderPortal
from utils.read_data import ReadData
import logging

LOGGER = logging.getLogger(__name__)

"""
    @author             : Somasekhar
    Description         : This method is used to Link record for Texas driver license - Dependent
"""


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class TestLinkRecordIdTexasDriverLicenseDependent(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.upass_holder_portal = HolderPortal(self.driver)
        self.bp = SeleniumDriver(self.driver)

    @pytest.mark.run(order=51)
    def test_link_record_id_texas_driver_license_dependent(self):
        with allure.step("Reading test data"):
            data = ReadData()
            test_data = data.get_test_data()
            excel_data = data.get_excel_data(2, 2)

        with allure.step("Logging to u-pass home page"):
            self.upass_holder_portal.upass_portal_page()
            LOGGER.info("Entered in login page")

        with allure.step("Clicking on Login to existing account button"):
            self.upass_holder_portal.click_existing_account()

        with allure.step("Entering Username"):
            self.upass_holder_portal.enter_username(excel_data)

        with allure.step("Entering Password"):
            self.upass_holder_portal.enter_login_password(test_data["Login"]["Password"])

        with allure.step("Clicking Continue button to Signin"):
            self.upass_holder_portal.click_continue_signin()

        with allure.step("Clicking the records"):
            self.upass_holder_portal.click_records()
            LOGGER.info("Click the records button")

        with allure.step("Clicking dropdown from top of records page"):
            self.upass_holder_portal.click_drop_down_from_records()
            LOGGER.info("Clicking dropdown from top of records page")

        with allure.step("Selecting the dependent"):
            self.upass_holder_portal.select_the_dependent()
            LOGGER.info("Dependent selected successfully")

        with allure.step("Clicking the add/get record"):
            self.upass_holder_portal.click_add_or_get_record()
            LOGGER.info("Click add/get record button")

        with allure.step("Clicking the link record"):
            self.upass_holder_portal.click_to_link_record()
            LOGGER.info("Click the link record")

        with allure.step("Selecting dependent holder name"):
            self.upass_holder_portal.select_dependent_holder_name()
            LOGGER.info("Select dependent holder name")

        with allure.step("Selecting record category type: ID"):
            self.upass_holder_portal.select_record_category_id()
            LOGGER.info("Select record category type: ID")

        with allure.step("Selecting record type: Driver license"):
            self.upass_holder_portal.select_record_type_driver_license()
            LOGGER.info("Select record type: Driver license")

        with allure.step("Selecting issuer type: Texas - Driver's License Division"):
            self.upass_holder_portal.select_issuer_type_texas()
            LOGGER.info("Select issuer type: Texas - Driver's License Division")

        with allure.step("Clicking search records"):
            self.upass_holder_portal.click_search_records()
            LOGGER.info("Click search records")

        with allure.step("Clicking the save button"):
            self.upass_holder_portal.click_save_record()
            LOGGER.info("Click the save button")

        with allure.step("Clicking th ID tab"):
            self.upass_holder_portal.click_id_tb()
            LOGGER.info("Click th ID tab")

        with allure.step("Verifying Texas Driver's License record"):
            self.upass_holder_portal.verify_texas_driver_license_record()
            LOGGER.info("Verify Texas Driver's License record")
