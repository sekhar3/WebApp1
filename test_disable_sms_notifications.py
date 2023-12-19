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
@author        : Srinivas Reddy
Description    : This class is used to Disable SMS Notifications
"""


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class TestNotificationPreferencesDisableSMS(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.upass_holder_portal = HolderPortal(self.driver)
        self.bp = SeleniumDriver(self.driver)

    @pytest.mark.run(order=24)
    def test_disable_sms_notifications(self):
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

        with allure.step("Clicking Notification Preferences button"):
            self.upass_holder_portal.click_notification_preferences()

        with allure.step("Clicking SMS toggle bar for Disable notifications"):
            self.upass_holder_portal.click_disable_sms_notifications()

        with allure.step("Clicking Save button"):
            self.upass_holder_portal.click_save_btn()
        with allure.step("Verifying Success Notification Message"):
            self.upass_holder_portal.verify_success_notification()
