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
    Description         : This method is used to link record for COVID 19 RT PCR(Issuer type: CDC)
"""


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class TestLinkRecordHealthCovid19RTPCR(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.upass_holder_portal = HolderPortal(self.driver)
        self.bp = SeleniumDriver(self.driver)

    @pytest.mark.run(order=34)
    def test_link_record_health_covid_19_rt_pcr(self):
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

        with allure.step("Clicking the add/get record"):
            self.upass_holder_portal.click_add_or_get_record()

        with allure.step("Clicking the link record"):
            self.upass_holder_portal.click_to_link_record()
            LOGGER.info("Click the link record")

        with allure.step("Selecting holder name"):
            self.upass_holder_portal.select_holder_name()

        with allure.step("Selecting record category type"):
            self.upass_holder_portal.select_record_category_health()

        with allure.step("Selecting record type: covid 19 rt pcr"):
            self.upass_holder_portal.select_record_type_covid_19_rt_pcr()

        with allure.step("Selecting issuer type: Inspire Health"):
            self.upass_holder_portal.select_issuer_type_inspire_health_1()

        with allure.step("Clicking the search records"):
            self.upass_holder_portal.click_search_records()

        with allure.step("Clicking the save button"):
            self.upass_holder_portal.click_save_record()

        with allure.step("Clicking Health tab under Records page"):
            self.upass_holder_portal.click_health_tb()

        with allure.step("Verifying covid 19 rt-pcr test health record"):
            self.upass_holder_portal.verify_covid_19_rt_pcr()
