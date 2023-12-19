import unittest

import allure
import pytest

from POM.BaseTest.selenium_driver import SeleniumDriver
from POM.Portal.upass_holder_app import HolderPortal
import logging
from utils.read_data import ReadData

LOGGER = logging.getLogger(__name__)

"""
    @author             : Sreenivas Reddy
    Description         : This method is used to Order Home Kit
"""


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class TestHomeOrderKitAntigen1(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.upass_holder_portal = HolderPortal(self.driver)
        self.bp = SeleniumDriver(self.driver)

    @pytest.mark.run(order=14)
    def test_home_kit_order_antigen(self):
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

        with allure.step("Clicking Get Care button"):
            self.upass_holder_portal.click_get_care()

        with allure.step("Clicking At Home Kit Order button"):
            self.upass_holder_portal.click_home_kit_order()

        with allure.step("Clicking Start Order button"):
            self.upass_holder_portal.click_start_order()

        with allure.step("Selecting Order Quantity of Antigen Test Kit"):
            self.upass_holder_portal.select_antigen_test1()

        with allure.step("Clicking Check Out button"):
            self.upass_holder_portal.click_check_out()

        with allure.step("Entering Fullname"):
            self.upass_holder_portal.enter_shipping_fullname(test_data["details"]["fullname"])

        with allure.step("Entering Phone Number"):
            self.upass_holder_portal.enter_shipping_phone_number(test_data["details"]["phone number"])

        with allure.step("Entering Address"):
            self.upass_holder_portal.enter_shipping_address(test_data["details"]["shipping address"])

        with allure.step("clicking Next Button"):
            self.upass_holder_portal.click_order_next()

        with allure.step("clicking Next Button"):
            self.upass_holder_portal.click_place_order()

        with allure.step("Verifying Order"):
            self.upass_holder_portal.verify_order_()
