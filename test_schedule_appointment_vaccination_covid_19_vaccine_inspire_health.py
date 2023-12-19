import time
import unittest

import allure

from POM.BaseTest.selenium_driver import SeleniumDriver
from POM.Portal.upass_holder_app import HolderPortal
import logging
from utils.read_data import ReadData
import pytest

LOGGER = logging.getLogger(__name__)

"""
    @author             : Sreenivas Reddy
    Description         : This method is used to schedule an appointment service category vaccination 
"""


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class TestScheduleAppointmentCVIH(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.upass_holder_portal = HolderPortal(self.driver)
        self.bp = SeleniumDriver(self.driver)

    @pytest.mark.run(order=12)
    def test_schedule_appointment_covid_vaccine(self):
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

        with allure.step("Clicking get care button"):
            self.upass_holder_portal.click_get_care()
            LOGGER.info("Clicked get care button successfully")

        with allure.step("Clicking the appointments"):
            self.upass_holder_portal.click_appointments()

            self.upass_holder_portal.click_schedule_appointment()
            LOGGER.info("Click appointments button successfully")

        with allure.step("Select service category"):
            self.upass_holder_portal.select_service_category_vaccination()

        with allure.step("Selecting service type"):
            self.upass_holder_portal.select_service_type_vaccine()

        with allure.step("Selecting Issuer Type CVS Pharmacy"):
            self.upass_holder_portal.select_issuer_inspire_health()

        with allure.step("Clicking Find a Slot button"):
            self.upass_holder_portal.click_find_slot()

        with allure.step("Selecting Appointment slot"):
            self.upass_holder_portal.select_appointment_slot()

        with allure.step("Confirming Appointment slot"):
            self.upass_holder_portal.select_confirm_appointment_slot()

        with allure.step("Clicking Next button"):
            self.upass_holder_portal.click_next()

        with allure.step("Entering Additional Questions"):
            self.upass_holder_portal.enter_additional_questions()

        with allure.step("Entering Allergies"):
            self.upass_holder_portal.enter_allergies(test_data["details"]["enter_allergies"])

        with allure.step("Entering Address"):
            self.upass_holder_portal.enter_address(test_data["details"]["address"])

        with allure.step("Clicking Review All Details Button"):
            self.upass_holder_portal.click_review_all_details()

        with allure.step("Clicking Confirm Appointment button"):
            self.upass_holder_portal.click_confirm_appointment()

        with allure.step("Verifying Scheduled Appointment"):
            self.upass_holder_portal.verify_appointment_scheduled()
