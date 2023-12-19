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
    Description         : This method is used to cancel dependent scheduled appointment
"""


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class TestCancelDependentScheduleAppointment(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.upass_holder_portal = HolderPortal(self.driver)
        self.bp = SeleniumDriver(self.driver)

    @pytest.mark.run(order=18)
    def test_cancel_schedule_appointment_dependent(self):
        with allure.step("Reading test data"):
            data = ReadData()
            test_data = data.get_test_data()
            excel_data = data.get_excel_data(2, 2)

        with allure.step("Login to U-Pass home Page"):
            self.upass_holder_portal.upass_portal_page()
            LOGGER.info("Entered in login page")

        with allure.step("Clicking on Login to existing account button"):
            self.upass_holder_portal.click_existing_account()

        with allure.step("Entering Username"):
            self.upass_holder_portal.enter_username(excel_data)

        with allure.step("Entering Password"):
            self.upass_holder_portal.enter_login_password(test_data["details"]["password"])

        with allure.step("Clicking Continue button to Signin"):
            self.upass_holder_portal.click_continue_signin()

        with allure.step("Clicking get care button"):
            self.upass_holder_portal.click_get_care()

        with allure.step("Clicking the appointments"):
            self.upass_holder_portal.click_appointments()

        with allure.step("Selecting scheduled appointment to cancel"):
            self.upass_holder_portal.click_scheduled_appointment_dependent()

        with allure.step("Clicking to cancel appointment"):
            self.upass_holder_portal.click_cancel_scheduled_appointment()

        with allure.step("Verifying appointment is cancelled"):
            self.upass_holder_portal.verify_cancel_scheduled_appointment()
