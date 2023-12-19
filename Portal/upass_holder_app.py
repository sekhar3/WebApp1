import time
import random
import imaplib
import email
import logging
from selenium.webdriver import ActionChains
from time import sleep

import pyautogui

from POM.Locators.locators import CreateNewLoginElements
from POM.Locators.locators import LoginExistingAccount
from utils.read_data import ReadData
from selenium.webdriver.common.keys import Keys
from POM.Locators.locators import UpassPortalElements
from POM.BaseTest.selenium_driver import SeleniumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
LOGGER = logging.getLogger(__name__)


class HolderPortal(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    data = ReadData()
    test_data = data.get_test_data()

    continue_btn = UpassPortalElements.continue_btn
    continue_btn_2 = UpassPortalElements.continue_btn_2
    continue_btn_3 = CreateNewLoginElements.continue_btn
    continue_btn_4 = UpassPortalElements.continue_btn_4
    get_started_btn = UpassPortalElements.get_started_btn
    create_new_login_btn = CreateNewLoginElements.create_new_login_btn
    full_name = CreateNewLoginElements.full_name
    enter_email = CreateNewLoginElements.enter_email
    birthdate = CreateNewLoginElements.birthdate
    phone_number = CreateNewLoginElements.phone_number
    password = CreateNewLoginElements.password
    confirm_password = CreateNewLoginElements.confirm_password
    verify_authentication_page = CreateNewLoginElements.verify_authentication_page
    go_to_upass_btn = CreateNewLoginElements.go_to_upass_btn
    verify_registration_logo = CreateNewLoginElements.verify_registration_logo
    verify_email = CreateNewLoginElements.verify_email
    insurance_provider_ = CreateNewLoginElements.insurance_provider
    member_id_ = CreateNewLoginElements.member_id
    group_number_ = CreateNewLoginElements.group_number
    insurance_provider_1 = CreateNewLoginElements.insurance_provider_1
    member_id_1 = CreateNewLoginElements.member_id_1
    group_number_1 = CreateNewLoginElements.group_number_1
    sex_ = CreateNewLoginElements.sex
    gender_m_ = CreateNewLoginElements.gender_m
    race_ = CreateNewLoginElements.race
    race_w_ = CreateNewLoginElements.race_w
    ethnicity_ = CreateNewLoginElements.ethnicity
    ethnicity_h_ = CreateNewLoginElements.ethnicity_h
    push_notifications_ = CreateNewLoginElements.push_notifications
    sms_notifications_ = CreateNewLoginElements.sms_notifications
    i_agree_ = CreateNewLoginElements.i_agree

    profile_btn = LoginExistingAccount.profile_button
    dismiss_button = LoginExistingAccount.dismiss_button
    resend_code = LoginExistingAccount.resend_code
    account_details_tb = LoginExistingAccount.account_details_tb
    basic_info_edit_btn = LoginExistingAccount.basic_info_edit_btn
    contact_info_edit_btn = LoginExistingAccount.contact_info_edit_btn
    edit_name = LoginExistingAccount.edit_name
    edit_display_name = LoginExistingAccount.edit_display_name
    edit_birthday = LoginExistingAccount.edit_birthday
    save_btn = LoginExistingAccount.save_btn
    save_dependent = LoginExistingAccount.save_btn
    cancel_btn = LoginExistingAccount.cancel_btn
    secondary_email_edit = LoginExistingAccount.secondary_email_edit
    edit_phone_number = LoginExistingAccount.edit_phone_number
    additional_profile_information_tb = LoginExistingAccount.additional_profile_information_tb
    additional_info_edit_btn = LoginExistingAccount.additional_info_edit_btn
    edit_gender = LoginExistingAccount.edit_gender
    gender_male = LoginExistingAccount.gender_male
    gender_female = LoginExistingAccount.gender_female
    edit_age = LoginExistingAccount.edit_age
    edit_sex = LoginExistingAccount.edit_sex
    edit_race = LoginExistingAccount.edit_race
    race_white = LoginExistingAccount.race_white
    race_asian = LoginExistingAccount.race_asian
    race_african_american_black = LoginExistingAccount.race_african_american_black
    race_native_american_alaskan = LoginExistingAccount.race_native_american_alaskan
    race_pacific_islander_hawaiian = LoginExistingAccount.race_pacific_islander_hawaiian
    race_other = LoginExistingAccount.race_other
    edit_ethnicity = LoginExistingAccount.edit_ethnicity
    ethnicity_hispanic = LoginExistingAccount.ethnicity_hispanic
    ethnicity_non_hispanic = LoginExistingAccount.ethnicity_non_hispanic
    ethnicity_unknown = LoginExistingAccount.ethnicity_unknown
    ethnicity_not_specified = LoginExistingAccount.ethnicity_not_specified
    add_insurance_provider1 = LoginExistingAccount.add_insurance_provider1
    add_member_id = LoginExistingAccount.add_member_id
    add_group_number = LoginExistingAccount.add_group_number

    name_edit_add_info = LoginExistingAccount.name_edit_add_info
    edit_birthday_add_info = LoginExistingAccount.edit_birthday_add_info
    notification_preferences_tb = LoginExistingAccount.notification_preferences_tb
    email_toggle_bar = LoginExistingAccount.email_toggle_bar
    sms_toggle_bar = LoginExistingAccount.sms_toggle_bar
    push_notifications_toggle_bar = LoginExistingAccount.push_notifications_toggle_bar
    success_message = LoginExistingAccount.success_message
    auto_approvals_btn = LoginExistingAccount.auto_approvals_btn
    dependents_add_btn = LoginExistingAccount.dependents_add_btn
    dependent_name = LoginExistingAccount.dependent_name
    dependent_birthday = LoginExistingAccount.dependent_birthday
    account_details_dependent = LoginExistingAccount.account_details_dependent
    basic_info_edit_dependent = LoginExistingAccount.basic_info_edit_dependent
    name_dependent = LoginExistingAccount.name_dependent
    dob_dependent = LoginExistingAccount.dob_dependent
    verify_dependent_text = LoginExistingAccount.verify_dependent_text
    verify_dependent = LoginExistingAccount.verify_dependent
    verify_dependent_name = LoginExistingAccount.verify_dependent_name
    add_info_dependent = LoginExistingAccount.add_info_dependent
    add_info_dependent_edit = LoginExistingAccount.basic_info_edit_dependent
    add_info_dependent_gender = LoginExistingAccount.add_info_dependent_gender
    add_info_dependent_age = LoginExistingAccount.add_info_dependent_age
    add_info_dependent_name = LoginExistingAccount.add_info_dependent_name
    auto_approvals_dependent = LoginExistingAccount.auto_approvals_dependent
    sign_out_btn = LoginExistingAccount.sign_out_btn
    sign_out_confirm_btn = LoginExistingAccount.sign_out_confirm_btn
    reset_password_btn = LoginExistingAccount.reset_password_btn
    reset_success = LoginExistingAccount.reset_success
    confirm_reset_password_btn = LoginExistingAccount.reset_password_done
    delete_account_btn = LoginExistingAccount.delete_account_btn
    confirm_delete_btn = LoginExistingAccount.confirm_delete_btn
    request_my_data_btn = LoginExistingAccount.request_my_data_btn
    call_btn = LoginExistingAccount.call_btn
    verify_delete = LoginExistingAccount.verify_delete
    delete_dependent_button = LoginExistingAccount.delete_dependent_button
    confirm_delete_dependent_button = LoginExistingAccount.confirm_delete_dependent_button
    verify_delete_dependent = LoginExistingAccount.verify_delete_dependent

    existing_account = LoginExistingAccount.existing_account
    username_textbox = LoginExistingAccount.username_tb
    password_textbox = LoginExistingAccount.password_tb
    signin_button = LoginExistingAccount.sign_in_btn
    hamburger_icon = LoginExistingAccount.hamburger_icon
    reset_id = LoginExistingAccount.reset_id
    view_scan_history = LoginExistingAccount.view_scan_history
    download_qr_code = LoginExistingAccount.download_code
    get_care_btn = LoginExistingAccount.get_care_btn
    get_care = LoginExistingAccount.get_care
    appointments_btn = LoginExistingAccount.appointments_btn
    schedule_appointment_btn = LoginExistingAccount.schedule_appointment
    schedule_new_appointment = LoginExistingAccount.schedule_new_appointment
    service_category = LoginExistingAccount.service_category

    service_category_covid_testing = LoginExistingAccount.service_category_covid_testing
    service_type_virtual = LoginExistingAccount.service_type_virtual

    service_category_medical = LoginExistingAccount.service_category_medical
    service_category_vaccination = LoginExistingAccount.service_category_vaccination
    service_type = LoginExistingAccount.service_type
    service_type_covid_vaccine = LoginExistingAccount.service_type_covid_vaccine
    service_type_antibody_test = LoginExistingAccount.service_type_antibody_test
    service_type_antibody_test_2 = LoginExistingAccount.service_type_antibody_test_2
    service_type_antigen_test = LoginExistingAccount.service_type_antigen_test
    service_type_antigen_test_2 = LoginExistingAccount.service_type_antigen_test_2
    service_type_pcr_test = LoginExistingAccount.service_type_pcr_test
    service_type_pcr_test_2 = LoginExistingAccount.service_type_pcr_test_2
    issuer_btn = LoginExistingAccount.issuer_btn
    choose_appointment_date_btn = LoginExistingAccount.choose_appointment_btn
    your_info_btn = LoginExistingAccount.your_info_btn
    next_btn = LoginExistingAccount.next_btn
    schedule_btn = LoginExistingAccount.schedule_btn
    appointment_scheduled_message = LoginExistingAccount.appointment_scheduled_message
    view_appointment = LoginExistingAccount.view_appointment
    view_dependent_appointment = LoginExistingAccount.view_dependent_appointment
    edit_appointment = LoginExistingAccount.edit_appointment
    issuer_type_any = LoginExistingAccount.issuer_type_any
    issuer_type_cvs = LoginExistingAccount.issuer_type_cvs
    issuer_type_inspire = LoginExistingAccount.issuer_type_inspire
    virtual_issuer_type_inspire = LoginExistingAccount.virtual_issuer_type_inspire
    virtual_appointment = LoginExistingAccount.virtual_appointment
    service_type_virtual_appointment = LoginExistingAccount.service_type_virtual_appointment
    find_a_slot = LoginExistingAccount.find_a_slot
    book_slot = LoginExistingAccount.book_slot
    reschedule_slot = LoginExistingAccount.reschedule_slot
    confirm_slot = LoginExistingAccount.confirm_slot
    confirm_reschedule_slot = LoginExistingAccount.confirm_reschedule_slot
    cancel_appointment = LoginExistingAccount.cancel_appointment
    confirm_cancel_appointment = LoginExistingAccount.confirm_cancel_appointment
    verify_cancel_appointment_message = LoginExistingAccount.confirm_cancel_appointment_message
    error_message_cancel_appointment = LoginExistingAccount.error_message_cancel_appointment
    dependent_schedule_appointment = LoginExistingAccount.dependent_schedule_appointment
    dependent_schedule_appointment_1 = LoginExistingAccount.dependent_schedule_appointment_1
    no_appointments = LoginExistingAccount.no_appointments
    schedule_date_next = LoginExistingAccount.schedule_date_next
    covid_test_yes = LoginExistingAccount.covid_test_yes
    covid_test_no = LoginExistingAccount.covid_test_no
    fever_chills = LoginExistingAccount.fever_chills
    nausea = LoginExistingAccount.nausea
    headache = LoginExistingAccount.headache
    dizziness = LoginExistingAccount.dizziness
    fatigue = LoginExistingAccount.fatigue
    difficulty_breathing = LoginExistingAccount.difficulty_breathing
    allergies = LoginExistingAccount.allergies
    gender = LoginExistingAccount.gender
    gender_m = LoginExistingAccount.gender_m
    gender_f = LoginExistingAccount.gender_f
    gender_others = LoginExistingAccount.gender_others
    prefer_not_to_say = LoginExistingAccount.prefer_not_to_say
    i_am_over_18 = LoginExistingAccount.i_am_over_18
    skip = LoginExistingAccount.skip
    review_all_details = LoginExistingAccount.review_all_details
    confirm_appointment = LoginExistingAccount.confirm_appointment
    address_field = LoginExistingAccount.address_field

    at_homekit_btn = LoginExistingAccount.at_homekit_btn
    start_order = LoginExistingAccount.start_order
    order_antigen_kit = LoginExistingAccount.order_antigen_kit
    order_antibody_kit = LoginExistingAccount.order_antibody_kit
    order_Antigen_Self_Test = LoginExistingAccount.order_Antigen_Self_Test
    order_antigen_kit1 = LoginExistingAccount.order_antigen_kit1
    order_pcr_kit = LoginExistingAccount.order_pcr_kit
    order_test_product = LoginExistingAccount.order_test_product
    order_non_zero_product = LoginExistingAccount.order_non_zero_product
    place_order = LoginExistingAccount.place_order
    check_out = LoginExistingAccount.check_out
    shipping_fullname = LoginExistingAccount.shipping_fullname
    shipping_phone_number = LoginExistingAccount.shipping_phone_number
    shipping_address = LoginExistingAccount.shipping_address
    shipping_address_input = LoginExistingAccount.shipping_address_input
    order_next = LoginExistingAccount.shipping_next
    card_number = LoginExistingAccount.card_number
    expiry_date = LoginExistingAccount.expiry_date
    cvc = LoginExistingAccount.cvc
    iframe = LoginExistingAccount.iframe
    submit = LoginExistingAccount.submit
    verify_order = LoginExistingAccount.verify_order

    place_btn = LoginExistingAccount.place_tab
    search_tb = LoginExistingAccount.search_tb
    shs_students_program = LoginExistingAccount.shs_students_program
    shs_athletics_program = LoginExistingAccount.shs_athletics_program
    shs_employees_vaccinated_program = LoginExistingAccount.shs_employees_vaccinated_program
    favourite_program = LoginExistingAccount.favourite_program
    un_favourite_program = LoginExistingAccount.un_favourite_program
    requirements_btn = LoginExistingAccount.requirements_btn
    verify_health = LoginExistingAccount.verify_health

    records_btn = LoginExistingAccount.record_btn
    click_dependent = LoginExistingAccount.click_dependent
    first_dependent = LoginExistingAccount.first_dependent
    select_dependent = LoginExistingAccount.select_dependent
    add_or_record_btn = LoginExistingAccount.add_or_record_btn
    link_to_record = LoginExistingAccount.link_record_btn
    scan_document_btn = LoginExistingAccount.scan_document_btn
    name_tb = LoginExistingAccount.name_tb
    first_name = LoginExistingAccount.first_name

    record_category = LoginExistingAccount.record_category
    record_category_health = LoginExistingAccount.record_category_health
    record_category_id = LoginExistingAccount.record_category_id
    record_type = LoginExistingAccount.record_type
    record_type_covid_pcr_test = LoginExistingAccount.record_type_covid_pcr_test
    record_type_covid_vaccination = LoginExistingAccount.record_type_covid_vaccination
    record_type_covid_19_test_antigen = LoginExistingAccount.record_type_covid_19_test_antigen
    record_type_immunization = LoginExistingAccount.record_type_immunization
    record_type_covid_19_test_antibody = LoginExistingAccount.record_type_covid_19_test_antibody
    record_type_covid_19_rt_pcr = LoginExistingAccount.record_type_covid_19_rt_pcr
    record_type_driver_license = LoginExistingAccount.record_type_driving_license
    record_type_employee_id_card = LoginExistingAccount.record_type_employee_id_card
    record_type_passport = LoginExistingAccount.record_type_passport
    record_type_student_id_card = LoginExistingAccount.record_type_student_id_card
    issuer_type = LoginExistingAccount.issuer_tb
    issuer_type_cdc = LoginExistingAccount.issuer_type_cdc
    issuer_type_inspire_health = LoginExistingAccount.issuer_type_inspire_health
    issuer_type_inspire_health_1 = LoginExistingAccount.issuer_type_inspire_health_1
    issuer_type_texas = LoginExistingAccount.issuer_type_texas
    issuer_type_alabama = LoginExistingAccount.issuer_type_alabama
    issuer_type_alaska = LoginExistingAccount.issuer_type_alaska
    issuer_type_employee_card = LoginExistingAccount.issuer_type_employee_card
    issuer_type_passport = LoginExistingAccount.issuer_type_passport
    issuer_type_student_card = LoginExistingAccount.issuer_type_student_card
    search_records = LoginExistingAccount.search_records
    search_records_btn = LoginExistingAccount.search_records_btn
    use_existing_btn = LoginExistingAccount.use_existing_btn
    scan_code_button = LoginExistingAccount.scan_code_button
    click_scan = LoginExistingAccount.click_scan
    confirm_btn = LoginExistingAccount.confirm_existing_document
    click_save = LoginExistingAccount.save_existing_document
    scan_code_btn = LoginExistingAccount.scan_code_btn
    save_record_btn = LoginExistingAccount.records_save_btn
    health_record = LoginExistingAccount.health_record
    id_record = LoginExistingAccount.id_record
    delete_from_record = LoginExistingAccount.delete_from_u_pass
    delete_record = LoginExistingAccount.delete_record
    verify_delete_record = LoginExistingAccount.verify_delete_record
    scan = LoginExistingAccount.scan
    verify_record_type_covid_pcr_test = LoginExistingAccount.verify_record_type_covid_pcr_test
    verify_record_type_covid_vaccination = LoginExistingAccount.verify_record_type_covid_vaccination
    verify_record_type_covid_19_antigen = LoginExistingAccount.verify_record_type_covid_19_antigen
    verify_record_type_immunization = LoginExistingAccount.verify_record_type_immunization
    verify_record_type_covid_19_antibody = LoginExistingAccount.verify_record_type_covid_19_antibody
    verify_record_type_covid_19_rt_pcr = LoginExistingAccount.verify_record_type_covid_19_rt_pcr
    verify_record_type_passport = LoginExistingAccount.verify_record_type_passport
    verify_record_type_texas_driver_license = LoginExistingAccount.verify_record_type_texas_driver_license
    verify_record_type_alabama_driver_license = LoginExistingAccount.verify_record_type_alabama_driver_license
    verify_record_type_alaska_driver_license = LoginExistingAccount.verify_record_type_alaska_driver_license
    verify_record_type_student_id_card = LoginExistingAccount.verify_record_type_student_id_card
    select_record = LoginExistingAccount.select_record_button
    delete_from_u_pass = LoginExistingAccount.delete_from_u_pass

    unique_id = LoginExistingAccount.unique_id
    notification_bell_icon = LoginExistingAccount.notification_bell_icon
    see_request = LoginExistingAccount.see_request
    approve_once = LoginExistingAccount.approve_once

    """
        @author : Sreenivas Reddy
        Description: This method used to launch U-Pass login page
    """

    def upass_portal_page(self):
        try:
            title = self.driver.title
            assert 'UPass-Holder' in title
            print("Title of the page:", title)
            self.element_Is_Visible("xpath", self.continue_btn)
            self.element_clickable("xpath", self.continue_btn)
            self.clickElement("xpath", self.continue_btn)

            self.element_Is_Visible("xpath", self.continue_btn_2)
            self.element_clickable("xpath", self.continue_btn_2)
            self.clickElement("xpath", self.continue_btn_2)

            self.element_Is_Visible("xpath", self.continue_btn_4)
            self.element_clickable("xpath", self.continue_btn_4)
            self.clickElement("xpath", self.continue_btn_4)
            print("Continue Button is Clicked")

        except Exception:
            print("Exception in Clicking Continue Button")
            self.takeScreenshot("Clicking Continue Button")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Click Create New Login
    """

    def click_create_new_login_btn(self):
        try:
            self.element_Is_Visible("xpath", self.create_new_login_btn)
            self.element_clickable("xpath", self.create_new_login_btn)
            self.clickElement("xpath", self.create_new_login_btn)
            sleep(1)
            print("Create New login Button is Clicked")
        except Exception:
            print("Exception in clicking Create New login Button")
            self.takeScreenshot("Clicking Create New login Button")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Enter Fullname
    """

    def enter_full_legal_name(self):
        try:
            global legal_fullname
            data = ReadData()
            test_data = data.get_test_data()
            title = self.driver.title
            assert 'Create Account' in title
            print("Title of the page:", title)
            self.element_Is_Visible("xpath", self.full_name)
            full_name = self.driver.find_element_by_xpath(self.full_name)
            full_name.send_keys(test_data["details"]["name"])
            time.sleep(2)
            legal_fullname = full_name.get_attribute('value')
            sleep(1)
            print("Full Legal Name is entered :", legal_fullname)
            return legal_fullname
        except Exception:
            print("Exception in Entering Full Legal Name")
            self.takeScreenshot("Entering Full Legal Name")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Enter Email
    """

    def enter_Email(self):
        try:
            global email_entered
            self.element_Is_Visible("xpath", self.enter_email)
            self.clickElement("xpath", self.enter_email)
            enter_email = self.driver.find_element_by_xpath(self.enter_email)
            enter_email.send_keys("sreenivasreddyunisys+" + str(random.randint(1, 99999)) + "@gmail.com")
            time.sleep(2)
            email_entered = enter_email.get_attribute('value')
            print("Entered email id is:", email_entered)
            return email_entered
        except Exception:
            print("Exception in Entering Email Method")
            self.takeScreenshot("Entering Email Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Enter Date of Birth
    """

    def enter_birthdate(self, DOB):
        try:
            self.element_Is_Visible("xpath", self.birthdate)
            self.clickElement("xpath", self.birthdate)
            self.enterText("xpath", self.birthdate, DOB)
            sleep(1)
            print("Date of Birth is entered")
        except Exception:
            print("Exception in Entering Date of Birth Method")
            self.takeScreenshot("Entering Date of Birth Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Enter Phone Number
    """

    def enter_phone_number(self, phone):
        try:
            self.element_Is_Visible("xpath", self.phone_number)
            self.clickElement("xpath", self.phone_number)
            self.enterText("xpath", self.phone_number, phone)
            sleep(1)
            print("Phone Number is entered")
        except Exception:
            print("Exception in Entering Phone Number Method")
            self.takeScreenshot("Entering Phone Number Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Enter Password
    """

    def enter_password(self, password):
        try:
            self.driver.find_element_by_xpath(self.confirm_password).send_keys(Keys.END)
            self.element_Is_Visible("xpath", self.password)
            self.clickElement("xpath", self.password)
            self.enterText("xpath", self.password, password)
            sleep(1)
            print("Password is entered")
        except Exception:
            print("Exception in Entering Password Method")
            self.takeScreenshot("Entering Password Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Enter Confirm Password
    """

    def enter_Confirm_password(self, password):
        try:
            self.element_Is_Visible("xpath", self.confirm_password)
            self.enterText("xpath", self.confirm_password, password)
            sleep(2)
            print("Confirm Password is entered")
        except Exception:
            print("Exception in Entering Confirm Password Method")
            self.takeScreenshot("Entering Confirm Password Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Enter Insurance Provider Name
    """

    def enter_insurance_provider(self, text):
        try:
            self.element_Is_Visible("xpath", self.insurance_provider_1)
            self.clickElement("xpath", self.insurance_provider_1)
            sleep(1)
            self.enterText("xpath", self.insurance_provider_, text)
            print("Insurance Provider name is entered")
        except Exception:
            print("Exception in Entering Insurance Provider name Method")
            self.takeScreenshot("Entering Insurance Provider name Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Enter Member Id
    """

    def enter_member_id(self, text):
        try:
            self.element_Is_Visible("xpath", self.member_id_1)
            self.clickElement("xpath", self.member_id_1)
            sleep(1)
            self.enterText("xpath", self.member_id_, text)
            sleep(10)
            print("Member Id is entered")
        except Exception:
            print("Exception in Entering Member Id Method")
            self.takeScreenshot("Entering Member Id name Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Enter Group Number
    """

    def enter_group_number(self, text):
        try:
            self.element_Is_Visible("xpath", self.group_number_1)
            self.clickElement("xpath", self.group_number_1)
            sleep(1)
            self.enterText("xpath", self.group_number_, text)
            print("Group Number is entered")
        except Exception:
            print("Exception in Entering IGroup Number Method")
            self.takeScreenshot("Entering Group Number Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Selecting Gender
    """
    def select_sex_male(self):
        try:
            self.element_Is_Visible("xpath", self.sex_)
            self.clickElement("xpath", self.sex_)
            sleep(2)
            self.element_Is_Visible("xpath", self.gender_m_)
            self.clickElement("xpath", self.gender_m_)
            print("Gender is Selected")
        except Exception:
            print("Exception in Selecting Gender Method")
            self.takeScreenshot("Selecting Gender Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Selecting Race
    """
    def select_race_white(self):
        try:
            self.element_Is_Visible("xpath", self.race_)
            self.clickElement("xpath", self.race_)
            sleep(2)
            self.element_Is_Visible("xpath", self.race_w_)
            self.clickElement("xpath", self.race_w_)
            print("Race is Selected")
        except Exception:
            print("Exception in Selecting Race Method")
            self.takeScreenshot("Selecting Race Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Selecting Ethnicity
    """

    def select_ethnicity_h(self):
        try:
            self.element_Is_Visible("xpath", self.ethnicity_)
            self.clickElement("xpath", self.ethnicity_)
            sleep(2)
            self.element_Is_Visible("xpath", self.ethnicity_h_)
            self.clickElement("xpath", self.ethnicity_h_)
            print("Ethnicity is Selected")
        except Exception:
            print("Exception in Selecting Ethnicity Method")
            self.takeScreenshot("Selecting Ethnicity Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Enable Push Notifications
    """

    def enable_push_notifications(self):
        try:
            self.element_Is_Visible("xpath", self.push_notifications_)
            self.clickElement("xpath", self.push_notifications_)
            print("Enabled Push Notifications")
        except Exception:
            print("Exception in Enabling Push Notifications Method")
            self.takeScreenshot("Enabling Push Notifications Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Enable Sms Notifications
    """

    def enable_sms_notifications(self):
        try:
            self.element_Is_Visible("xpath", self.sms_notifications_)
            self.clickElement("xpath", self.sms_notifications_)
            print("Enabled Sms Notifications")
        except Exception:
            print("Exception in Enabling Sms Notifications Method")
            self.takeScreenshot("Enabling Sms Notifications Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Clicking I Agree Button
    """

    def click_i_agree(self):
        try:
            self.element_Is_Visible("xpath", self.i_agree_)
            self.clickElement("xpath", self.i_agree_)
            print("I Agree Button is clicked")
        except Exception:
            print("Exception in Clicking I Agree Method")
            self.takeScreenshot("Clicking I Agree Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Verify Email Address
    """

    def verify_email_upass(self):
        global new_otp
        username = 'sreenivasreddyunisys@gmail.com'
        password = 'sree.123'
        link = []
        st = " "
        # create an IMAP4 class with SSL
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        # authenticate
        imap.login(username, password)
        status, messages = imap.select("Inbox")
        # number of top emails to fetch
        N = 1
        # total number of emails
        messages = int(messages[0])
        for i in range(messages, messages - N, -1):
            # fetch the email message by ID
            res, msg = imap.fetch(str(i), "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    # parse a bytes email into a message object
                    msg = email.message_from_bytes(response[1])
                    if msg.as_string():
                        # iterate over email parts
                        for part in msg.walk():
                            # extract content type of email
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:
                                # get the email body
                                body = part.get_payload(decode=True).decode()
                                import re
                                a = (re.search("(?P<url>https?://[^\\s]+)", body).group("url"))
                                b = a.partition('http://www.w3.org/1999/xhtml"')
                                c = (b[0])
                                link.append(c)
                                new_otp = st.join(link)
                            except:
                                pass
        imap.close()
        imap.logout()
        return new_otp

    """
        @author : Sreenivas Reddy
        Description: This method used to Click Continue Button
    """

    def click_continue_button(self):
        try:
            self.element_Is_Visible("xpath", self.verify_authentication_page)
            self.element_Is_Visible("xpath", self.continue_btn_3)
            self.clickElement("xpath", self.continue_btn_3)
            sleep(1)
            print("Continue Button is clicked")
        except Exception:
            print("Exception in Clicking Continue Button Method")
            self.takeScreenshot("Clicking Continue Button Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Click Continue Button
    """

    def click_continue(self):
        try:
            self.element_Is_Visible("xpath", self.continue_btn_3)
            self.clickElement("xpath", self.continue_btn_3)
            sleep(1)
            print("Continue Button is clicked")
        except Exception:
            print("Exception in Clicking Continue Button Method")
            self.takeScreenshot("Clicking Continue Button Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Click Go To U-Pass Button
    """

    def click_go_to_upass(self):
        try:
            self.element_Is_Visible("xpath", self.go_to_upass_btn)
            self.clickElement("xpath", self.go_to_upass_btn)
            print("Go To U-Pass button is clicked")
            sleep(3)
            self.data.write_data_into_excel(2, 2, email_entered)
        except Exception:
            print("Exception in Clicking Go To U-Pass Button Method")
            self.takeScreenshot("Clicking Go To U-Pass Button Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Verify New Account
    """

    def verify_new_account(self):
        try:
            self.element_Is_Visible("xpath", self.get_care_btn)
            print("New User Account is Successfully created")
        except Exception:
            print("Exception in Verifying New Account Method")
            self.takeScreenshot("Verifying New Account Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to click Profile button 
    """

    def click_profile_tab(self):
        try:
            self.element_Is_Visible("xpath", self.profile_btn)
            element = self.driver.find_element_by_xpath(self.profile_btn)
            self.driver.execute_script("arguments[0].click();", element)
            title = self.driver.title
            assert 'Profile' in title
            print("Title of the page:", title)
            print("Profile Button is clicked")
        except Exception:
            print("Exception in Clicking Profile Button Method ")
            self.takeScreenshot("Clicking Profile Button Method")
            raise Exception

        """
            @author        : Sreenivas reddy
            Description    : This method is used to click Account Details button under Profile Section
        """

    def click_account_details_tb(self):
        try:
            self.element_Is_Visible("xpath", self.account_details_tb)
            element = self.driver.find_element_by_xpath(self.account_details_tb)
            self.driver.execute_script("arguments[0].click();", element)
            print("Account Details Button is clicked")
        except Exception:
            print("Exception in Clicking Account Details Method")
            self.takeScreenshot("Clicking Account Details Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to click Edit button under Basic Information Under Account Details section
    """

    def click_basic_info_edit_btn(self):
        try:
            self.element_Is_Visible("xpath", self.basic_info_edit_btn)
            self.clickElement("xpath", self.basic_info_edit_btn)
            print("Edit Button is clicked")
        except Exception:
            print("Exception in Clicking Edit Button Method")
            self.takeScreenshot("Clicking Edit Button Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to click Edit Name under Basic Information
    """

    def enter_basic_info_edit_name(self, name):
        try:
            self.element_Is_Visible("xpath", self.edit_name)
            self.clickElement("xpath", self.edit_name)
            self.driver.find_element_by_xpath(self.edit_name).send_keys(Keys.CONTROL + "a", Keys.DELETE)
            self.enterText("xpath", self.edit_name, name)
            print("Name is Entered")
        except Exception:
            print("Exception in Entering Name Method")
            self.takeScreenshot("Entering Name Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Edit Birthday under Basic Information
    """

    def enter_basic_info_edit_birthday(self, birthday):
        try:
            self.element_Is_Visible("xpath", self.edit_birthday)
            self.clickElement("xpath", self.edit_birthday)
            self.driver.find_element_by_xpath(self.edit_birthday).send_keys(Keys.CONTROL + "a", Keys.DELETE)
            self.enterText("xpath", self.edit_birthday, birthday)
            print("Birthday is Entered")
        except Exception:
            print("Exception in Entering Birthday Method")
            self.takeScreenshot("Entering Birthday Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to click Save button
    """

    def click_save_btn(self):
        try:
            sleep(1)
            self.scrollTo("xpath", self.save_btn)
            self.element_Is_Visible("xpath", self.save_btn)
            self.clickElement("xpath", self.save_btn)
            print("Save Button is Clicked")
        except Exception:
            print("Exception in Clicking the Save Button Method")
            self.takeScreenshot("Clicking the Save Button Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Save Dependent
    """

    def click_save_dependent(self):
        try:
            self.element_Is_Visible("xpath", self.save_dependent)
            self.driver.find_element_by_xpath(self.save_dependent).click()
            print("Save Button is Clicked")
            sleep(2)
        except Exception:
            print("Exception in Clicking the Save Button Method")
            self.takeScreenshot("Clicking the Save Button Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to click Edit button under Contact Information Under Account Details section
    """

    def click_contact_info_edit_btn(self):
        try:
            self.element_Is_Visible("xpath", self.contact_info_edit_btn)
            self.clickElement("xpath", self.contact_info_edit_btn)
            print("Edit Button is clicked")
        except Exception:
            print("Exception in Clicking Edit Button Method")
            self.takeScreenshot("Clicking Edit Button Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Enter Secondary Email address under contact Information
    """

    def enter_secondary_email(self, email_id):
        try:
            self.element_Is_Visible("xpath", self.secondary_email_edit)
            self.clickElement("xpath", self.secondary_email_edit)
            self.driver.find_element_by_xpath(self.secondary_email_edit).send_keys(Keys.CONTROL + "a", Keys.DELETE)
            time.sleep(2)
            self.enterText("xpath", self.secondary_email_edit, email_id)
            print("Secondary Email Address is entered")
        except Exception:
            print("Exception in Entering Secondary Email Address Method")
            self.takeScreenshot("Entering Secondary Email Address Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Enter Phone Number
    """

    def enter_edit_phone_number(self, phone):
        try:
            self.element_Is_Visible("xpath", self.edit_phone_number)
            self.clickElement("xpath", self.edit_phone_number)
            self.driver.find_element_by_xpath(self.edit_phone_number).send_keys(Keys.CONTROL + "a", Keys.DELETE)
            time.sleep(2)
            self.enterText("xpath", self.edit_phone_number, phone)
            print("Phone Number is entered")
        except Exception:
            print("Exception in Entering Phone Number Method")
            self.takeScreenshot("Entering Phone Number Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to click Additional Profile Information button under Profile Section
    """

    def click_additional_profile_information(self):
        try:
            self.element_Is_Visible("xpath", self.additional_profile_information_tb)
            element = self.driver.find_element_by_xpath(self.additional_profile_information_tb)
            self.driver.execute_script("arguments[0].click();", element)
            print("Additional Profile Information is clicked")
        except Exception:
            print("Exception in Clicking Additional Profile Information Method")
            self.takeScreenshot("Clicking Additional Profile Information Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to click Edit Button under Additional Info
    """

    def click_additional_info_edit_btn(self):
        try:
            self.element_Is_Visible("xpath", self.additional_info_edit_btn)
            self.clickElement("xpath", self.additional_info_edit_btn)
            print("Edit Button is clicked")
        except Exception:
            print("Exception in Clicking Edit Button Method")
            self.takeScreenshot("Clicking Edit Button Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Select Gender under Additional Info
    """

    def enter_edit_sex(self):
        try:
            self.element_Is_Visible("xpath", self.edit_sex)
            self.clickElement("xpath", self.edit_sex)
            sleep(1)
            self.clickElement("xpath", self.gender_male)
            print("Gender Male is selected")
        except Exception:
            print("Exception in  Selecting Gender Method")
            self.takeScreenshot("Selecting Gender Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Select Race under Additional Info
    """

    def select_race(self):
        try:
            self.element_Is_Visible("xpath", self.edit_race)
            self.clickElement("xpath", self.edit_race)
            sleep(1)
            self.clickElement("xpath", self.race_white)
            print("Race is selected")
        except Exception:
            print("Exception in  Selecting Race Method")
            self.takeScreenshot("Selecting Race Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Select Ethnicity under Additional Info
    """

    def select_ethnicity(self):
        try:
            self.element_Is_Visible("xpath", self.edit_ethnicity)
            self.clickElement("xpath", self.edit_ethnicity)
            sleep(1)
            self.clickElement("xpath", self.ethnicity_hispanic)
            print("Ethnicity is selected")
        except Exception:
            print("Exception in  Selecting Ethnicity Method")
            self.takeScreenshot("Selecting Ethnicity Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to enter Age under Additional Info
    """

    def enter_edit_age(self, gen):
        try:
            self.element_Is_Visible("xpath", self.edit_age)
            self.clickElement("xpath", self.edit_age)
            self.driver.find_element_by_xpath(self.edit_age).send_keys(Keys.CONTROL + "a", Keys.DELETE)
            self.enterText("xpath", self.edit_age, gen)
            print("Age is entered")
        except Exception:
            print("Exception in Entering Age Method")
            self.takeScreenshot("Entering Age Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to enter Name under Additional Info
    """

    def enter_edit_name_add_info(self, name):
        try:
            self.element_Is_Visible("xpath", self.name_edit_add_info)
            self.clickElement("xpath", self.name_edit_add_info)
            self.driver.find_element_by_xpath(self.name_edit_add_info).send_keys(Keys.CONTROL + "a", Keys.DELETE)
            self.enterText("xpath", self.name_edit_add_info, name)
            print("Name is entered")
        except Exception:
            print("Exception in Entering Name Method")
            self.takeScreenshot("Entering Name Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to enter Date of Birth under Additional Info
    """

    def enter_edit_birthday_add_info(self, dob):
        try:
            self.element_Is_Visible("xpath", self.edit_birthday_add_info)
            self.clickElement("xpath", self.edit_birthday_add_info)
            self.driver.find_element_by_xpath(self.edit_birthday_add_info).send_keys(Keys.CONTROL + "a", Keys.DELETE)
            self.enterText("xpath", self.edit_birthday_add_info, dob)
            print("Date of Birth is entered")
        except Exception:
            print("Exception in Entering Date of Birth Method")
            self.takeScreenshot("Entering Date of Birth Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to enter Insurance Provider under Additional Info
    """

    def enter_insurance_provider_add_info(self, gen):
        try:
            self.element_Is_Visible("xpath", self.add_insurance_provider1)
            self.clickElement("xpath", self.add_insurance_provider1)
            self.driver.find_element_by_xpath(self.add_insurance_provider1).send_keys(Keys.CONTROL + "a", Keys.DELETE)
            self.enterText("xpath", self.add_insurance_provider1, gen)
            print("Insurance Provider is entered")
        except Exception:
            print("Exception in Entering Insurance Provider Method")
            self.takeScreenshot("Entering Insurance Provider Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to enter Member Id under Additional Info
    """

    def enter_member_id_add_info(self, gen):
        try:
            self.element_Is_Visible("xpath", self.add_member_id)
            self.clickElement("xpath", self.add_member_id)
            self.driver.find_element_by_xpath(self.add_member_id).send_keys(Keys.CONTROL + "a", Keys.DELETE)
            self.enterText("xpath", self.add_member_id, gen)
            print("Member Id is entered")
        except Exception:
            print("Exception in Entering Member Id Method")
            self.takeScreenshot("Entering Member Id Method")
            raise Exception

    """
            @author        : Sreenivas reddy
            Description    : This method is used to enter Member Id under Additional Info
        """

    def enter_group_number_add_info(self, gen):
        try:
            # self.driver.find_element_by_xpath(self.save_btn).send_keys(Keys.END)
            sleep(2)
            self.scrollTo("xpath", self.add_group_number)
            self.element_Is_Visible("xpath", self.add_group_number)
            print("visible")
            self.clickElement("xpath", self.add_group_number)
            self.driver.find_element_by_xpath(self.add_group_number).send_keys(Keys.CONTROL + "a", Keys.DELETE)
            self.enterText("xpath", self.add_group_number, gen)
            print("Group Number is entered")
        except Exception:
            print("Exception in Entering Group Number Method")
            self.takeScreenshot("Entering Group Number Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Click Notification Preferences button under Profile Section
    """

    def click_notification_preferences(self):
        try:
            self.driver.set_window_size(800, 1080)
            time.sleep(2)
            self.element_Is_Visible("xpath", self.notification_preferences_tb)
            self.clickElement("xpath", self.notification_preferences_tb)
            print("Notification Preferences button is clicked")
            sleep(2)
            title = self.driver.title
            assert 'Notification Preferences' in title
            print("Title of the page:", title)
        except Exception:
            print("Exception in Clicking Notification Preferences Button Method")
            self.takeScreenshot("Clicking Notification Preferences Button Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Enable Email Notifications
    """

    def click_enable_email_notifications(self):
        try:
            enable = self.getElement(self.email_toggle_bar, "xpath")
            if enable.is_selected():
                print("Enabled Email Notifications")
            else:
                enable.click()
                print("Enabled Email Notifications")
            print("Email Toggle Bar is clicked")
        except Exception:
            print("Exception in Clicking Email Toggle Bar Method")
            self.takeScreenshot("Clicking Email Toggle Bar Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Disable Email Notifications
    """

    def click_disable_email_notifications(self):
        try:
            disable = self.getElement(self.email_toggle_bar, "xpath")
            if disable.get_attribute("checked") != "true":
                print("Disable Email Notifications")
            else:
                disable.click()
                print("Disable Email Notifications")
            print("Email Toggle Bar is clicked")
        except Exception:
            print("Exception in Clicking Email Toggle Bar Method")
            self.takeScreenshot("Clicking Email Toggle Bar Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Verify Success Notification Message
    """

    def verify_success_notification(self):
        self.element_Is_Visible("xpath", self.success_message)
        print("Changes to Your Notifications have been saved")

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Enable SMS Notifications
    """

    def click_enable_sms_notifications(self):
        try:
            enable = self.getElement(self.sms_toggle_bar, "xpath")
            if enable.is_selected():
                print("Enabled SMS Notifications")
            else:
                enable.click()
                print("Enabled SMS Notifications")
            print("SMS Toggle Bar is clicked")
        except Exception:
            print("Exception in Clicking SMS Toggle Bar Method")
            self.takeScreenshot("Clicking SMS Toggle Bar Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Disable Sms Notifications
    """

    def click_disable_sms_notifications(self):
        try:
            disable = self.getElement(self.sms_toggle_bar, "xpath")
            if disable.get_attribute("checked") != "true":
                print("Disable SMS Notifications")
            else:
                disable.click()
                print("Disable SMS Notifications")
            print("SMS Toggle Bar is clicked")
        except Exception:
            print("Exception in Clicking SMS Toggle Bar Method")
            self.takeScreenshot("Clicking SMS Toggle Bar Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Enable Push Notifications
    """

    def click_enable_push_notifications(self):
        try:
            enable = self.getElement(self.push_notifications_toggle_bar, "xpath")
            if enable.is_selected():
                print("Enabled Push notifications")
            else:
                enable.click()
                print("Enabled Push Notifications")
            print("Push Notifications Toggle Bar Method is clicked")
        except Exception:
            print("Exception in Clicking Push Notifications Toggle Bar Method")
            self.takeScreenshot("Clicking Push Notifications Toggle Bar Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Disable Push Notifications
    """

    def click_disable_push_notifications(self):
        try:
            disable = self.getElement(self.push_notifications_toggle_bar, "xpath")
            if disable.get_attribute("checked") != "true":
                print("Disable Push Notifications")
            else:
                disable.click()
                print("Disable Push Notifications")
            print("Push Notifications Toggle Bar is clicked")
        except Exception:
            print("Exception in Clicking Push Notifications Toggle Bar Method")
            self.takeScreenshot("Clicking Push Notifications Toggle Bar Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Click Auto Approvals Button 
    """

    def click_auto_approvals_btn(self):
        try:
            self.element_Is_Visible("xpath", self.auto_approvals_btn)
            self.clickElement("xpath", self.auto_approvals_btn)
            print("Auto Approvals Button is clicked")
        except Exception:
            print("Exception in Clicking Auto Approvals Button Method")
            self.takeScreenshot("Clicking Auto Approvals Button Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Click Add Dependents Button 
    """

    def click_dependents_add_btn(self):
        try:
            self.element_Is_Visible("xpath", self.dependents_add_btn)
            self.clickElement("xpath", self.dependents_add_btn)
            print("Add Dependents Button  is clicked")
        except Exception:
            print("Exception in Clicking Add Dependents Button Method")
            self.takeScreenshot("Clicking Add Dependents Button Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Enter Dependents Name 
    """

    def enter_dependent_name(self, name):
        try:
            title = self.driver.title
            assert 'Dependent' in title
            print("Title of the page:", title)
            self.clickElement("xpath", self.dependent_name)
            dependent = self.driver.find_element_by_xpath(self.dependent_name)
            dependent.send_keys(name)
            time.sleep(2)
        except Exception:
            print("Exception in Entering Dependent Name Method")
            self.takeScreenshot("Entering Dependent Name Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Enter Dependents Date of Birth 
    """

    def click_dependent_birthday(self, dob):
        try:
            self.element_Is_Visible("xpath", self.dependent_birthday)
            self.clickElement("xpath", self.dependent_birthday)
            self.enterText("xpath", self.dependent_birthday, dob)
            sleep(1)
        except Exception:
            print("Exception in Entering Dependent Date of Birth Method")
            self.takeScreenshot("Entering Dependent Date of Birth Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Verify Dependent is added or not
    """

    def Verify_dependent(self):
        self.element_Is_Visible("xpath", self.verify_dependent)
        verify_d = self.driver.find_element_by_xpath(self.verify_dependent).text
        print(verify_d)
        if verify_d == dependent_fullname:
            assert True
            print("Dependent has been successfully added")
        else:
            assert False

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Click Dependent Account Details Button
    """

    def click_dependent_account_details(self):
        try:
            self.element_Is_Visible("xpath", self.account_details_dependent)
            self.clickElement("xpath", self.account_details_dependent)
            print("Dependent Account Details Button clicked ")
        except Exception:
            print("Exception in Clicking Dependent Account Details Button Method")
            self.takeScreenshot("Clicking Dependent Account Details Button Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Delete Dependent Account
    """

    def click_delete_dependent(self):
        try:
            self.element_Is_Visible("xpath", self.delete_dependent_button)
            self.clickElement("xpath", self.delete_dependent_button)
            print("Delete Dependent Account Button is clicked ")

            self.element_Is_Visible("xpath", self.confirm_delete_dependent_button)
            self.clickElement("xpath", self.confirm_delete_dependent_button)
            print("Confirm Delete Dependent Account Button is clicked ")

        except Exception:
            print("Exception in Clicking Delete Dependent Account Button Method")
            self.takeScreenshot("Clicking Delete Dependent Account Button Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Verify Delete Dependent Account
    """

    def verify_dependent_delete(self):
        try:
            self.element_Is_Visible("xpath", self.verify_delete_dependent)
            verify_d = self.getElement(self.verify_delete_dependent, "xpath")
            print(verify_d)
        except Exception:
            print("Exception in Verifying Delete Dependent Account Method")
            self.takeScreenshot("Verifying Delete Dependent Account Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Click Dependent Basic Info Edit button
    """

    def click_basic_info_edit_dependent(self):
        try:
            self.element_Is_Visible("xpath", self.basic_info_edit_dependent)
            self.clickElement("xpath", self.basic_info_edit_dependent)
            print("Dependent Basic Info Edit Button is clicked ")
        except Exception:
            print("Exception in Clicking Dependent Basic Info Edit Button Method")
            self.takeScreenshot("Clicking Dependent Basic Info Edit Button Method")
            raise Exception

    """
            @author        : Sreenivas reddy
            Description    : This method is used to Edit and Enter Dependent Name
        """

    def enter_name_dependent(self, name):
        try:
            # self.element_Is_Visible("xpath", self.name_dependent)
            # self.clickElement("xpath", self.name_dependent)
            # # self.driver.find_element_by_xpath(self.name_dependent).send_keys(Keys.CONTROL + "a", Keys.DELETE)
            # self.enterText("xpath", self.name_dependent, name)
            # print("Dependent Name is edited")
            global dependent_fullname
            self.clickElement("xpath", self.name_dependent)
            self.driver.find_element_by_xpath(self.name_dependent).send_keys(Keys.CONTROL + "a", Keys.DELETE)
            dependent = self.driver.find_element_by_xpath(self.name_dependent)
            dependent.send_keys(name)
            time.sleep(2)
            dependent_fullname = dependent.get_attribute('value')
            sleep(1)
            print("Full Legal Name is entered :", dependent_fullname)
            print("Dependent Name  is entered")
            return dependent_fullname

        except Exception:
            print("Exception in Entering Dependent Name Method")
            self.takeScreenshot("Entering Dependent Name Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Enter DOB of Dependent 
    """

    def enter_dob_dependent(self, dob):
        try:
            self.element_Is_Visible("xpath", self.dob_dependent)
            self.clickElement("xpath", self.dob_dependent)
            self.driver.find_element_by_xpath(self.dob_dependent).send_keys(Keys.CONTROL + "a", Keys.DELETE)
            self.enterText("xpath", self.dob_dependent, dob)
            print("Dependent Date of Birth is entered")
        except Exception:
            print("Exception in Entering Dependent Date of Birth Method")
            self.takeScreenshot("Entering Dependent Date of Birth Method")
            raise Exception

    """
            @author        : Sreenivas reddy
            Description    : This method is used to Click Dependent Additional Profile Information button
        """

    def click_add_info_dependent(self):
        try:
            self.element_Is_Visible("xpath", self.add_info_dependent)
            self.clickElement("xpath", self.add_info_dependent)
            print("Dependent Additional Profile Information Button is clicked ")
        except Exception:
            print("Exception in Clicking Additional Profile Information Button Method")
            self.takeScreenshot("Clicking Additional Profile Information Button Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Click Dependent Additional Info Edit button
    """

    def click_add_info_dependent_edit(self):
        try:
            self.element_Is_Visible("xpath", self.add_info_dependent_edit)
            self.clickElement("xpath", self.add_info_dependent_edit)
            print("Dependent Additional Info Edit Button is clicked ")
        except Exception:
            print("Exception in Clicking Dependent Additional Info Edit Button Method")
            self.takeScreenshot("Clicking Dependent Additional Info Edit Button Method")
            raise Exception

    """
            @author        : Sreenivas reddy
            Description    : This method is used to Edit and Enter Dependent Gender
        """

    def enter_add_info_dependent_gender(self):
        try:
            self.element_Is_Visible("xpath", self.add_info_dependent_gender)
            self.clickElement("xpath", self.add_info_dependent_gender)
            self.clickElement("xpath", self.gender_female)
            print("Dependent Gender is entered")
        except Exception:
            print("Exception in Entering Dependent Gender Method")
            self.takeScreenshot("Entering Dependent Gender Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Enter Age of Dependent 
    """

    def enter_add_info_dependent_age(self, age):
        try:
            self.element_Is_Visible("xpath", self.add_info_dependent_age)
            self.clickElement("xpath", self.add_info_dependent_age)
            self.driver.find_element_by_xpath(self.add_info_dependent_age).send_keys(Keys.CONTROL + "a", Keys.DELETE)
            self.enterText("xpath", self.add_info_dependent_age, age)
            print("Dependent Age is entered")
        except Exception:
            print("Exception in Entering Dependent Age Method")
            self.takeScreenshot("Entering Dependent Age Method")
            raise Exception

    """
            @author        : Sreenivas reddy
            Description    : This method is used to Enter Age of Dependent 
        """

    def enter_add_info_dependent_name(self, name):
        try:
            self.element_Is_Visible("xpath", self.add_info_dependent_name)
            self.clickElement("xpath", self.add_info_dependent_name)
            self.driver.find_element_by_xpath(self.add_info_dependent_name).send_keys(Keys.CONTROL + "a", Keys.DELETE)
            self.enterText("xpath", self.add_info_dependent_name, name)
            print("Dependent Name is entered")
        except Exception:
            print("Exception in Entering Dependent Name Method")
            self.takeScreenshot("Entering Dependent Name Method")
            raise Exception

    """
            @author        : Sreenivas reddy
            Description    : This method is used to Click Auto Approvals Button 
        """

    def click_auto_approvals_dependent(self):
        try:
            self.element_Is_Visible("xpath", self.auto_approvals_dependent)
            self.clickElement("xpath", self.auto_approvals_dependent)
            print("Auto Approvals Button is clicked")
        except Exception:
            print("Exception in Clicking Auto Approvals Button Method")
            self.takeScreenshot("Clicking Auto Approvals Button Method")
            raise Exception

    """
            @author        : Sreenivas reddy
            Description    : This method is used to Click Sign Out button
    """

    def click_sign_out_btn(self):
        try:
            self.element_Is_Visible("xpath", self.sign_out_btn)
            self.clickElement("xpath", self.sign_out_btn)
            print("Sign Out Button is clicked")
        except Exception:
            print("Exception in Clicking Sign Out Button Method")
            self.takeScreenshot("Clicking Sign Out Button Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Click Sign Out Confirmation button 
    """

    def click_sign_out_confirm_btn(self):
        try:
            self.element_Is_Visible("xpath", self.sign_out_confirm_btn)
            self.clickElement("xpath", self.sign_out_confirm_btn)
            print("Sign Out Confirmation Button is clicked")
            print("User Sign Out Successfully")
            time.sleep(2)
        except Exception:
            print("Exception in Clicking Sign Out Confirmation Button Method")
            self.takeScreenshot("Clicking Sign Out Confirmation Button Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Click Reset Password button 
    """

    def click_reset_password_btn(self):
        try:
            self.element_Is_Visible("xpath", self.reset_password_btn)
            self.clickElement("xpath", self.reset_password_btn)
            print("Reset Password  Button is clicked")
        except Exception:
            print("Exception in Clicking Reset Password Button Method")
            self.takeScreenshot("Clicking Reset Password Button Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Click Reset Password Confirmation button 
    """

    def click_confirm_reset_password_btn(self):
        try:
            self.element_Is_Visible("xpath", self.confirm_reset_password_btn)
            self.element_Is_Visible("xpath", self.reset_success)
            self.clickElement("xpath", self.confirm_reset_password_btn)
            print("Reset Password Confirmation button is clicked")
            print("Password Reset Email Sent")
            time.sleep(2)
        except Exception:
            print("Exception in Clicking Reset Password Confirmation Method")
            self.takeScreenshot("Clicking Reset Password Confirmation Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Click Delete Account button 
    """

    def click_delete_account_btn(self):
        try:
            self.element_Is_Visible("xpath", self.delete_account_btn)
            self.clickElement("xpath", self.delete_account_btn)
            print("Delete Account Button is clicked")
        except Exception:
            print("Exception in Clicking Delete Account Button Method")
            self.takeScreenshot("Clicking Delete Account Button Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Click Delete Account Confirmation button 
    """

    def click_confirm_delete_btn(self):
        try:
            self.element_Is_Visible("xpath", self.confirm_delete_btn)
            self.clickElement("xpath", self.confirm_delete_btn)
            print("Delete Account Confirmation Button is clicked")
            sleep(1)
            self.element_Is_Visible("xpath", self.verify_delete)
            print("Account Successfully Deleted")
        except Exception:
            print("Exception in Clicking Delete Account Confirmation Button Method")
            self.takeScreenshot("Delete Account Confirmation Button Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Click Request My Data button 
    """

    def click_request_my_data_btn(self):
        try:
            self.element_Is_Visible("xpath", self.request_my_data_btn)
            self.clickElement("xpath", self.request_my_data_btn)
            print("Request My Data Button is clicked")
        except Exception:
            print("Exception in Clicking Request My Data Button Method")
            self.takeScreenshot("Clicking Request My Data Button Method")
            raise Exception

    """
            @author        : Sreenivas reddy
            Description    : This method is used to Click Call button 
    """

    def click_call_btn(self):
        try:
            self.element_Is_Visible("xpath", self.call_btn)
            self.clickElement("xpath", self.call_btn)
            print("Call Button is clicked")
        except Exception:
            print("Exception in Clicking Call Button Method")
            self.takeScreenshot("Clicking Call Button Method")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to login to an existing account
    """

    def click_existing_account(self):
        try:
            login = self.driver.find_element_by_xpath(self.existing_account)
            self.driver.execute_script("arguments[0].click();", login)
            handles = self.driver.window_handles
            for handle in handles:
                self.driver.switch_to.window(handle)
            print("Existing Account Button is clicked")
        except Exception:
            self.takeScreenshot("Clicking Existing Account Button")
            raise Exception

    """
    @author             : Somasekhar
    Description         : This method is used to enter username
    """

    def enter_username(self, username):
        try:
            wait = WebDriverWait(self.driver, 30)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.username_textbox)))
            wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.username_textbox)))
            self.driver.find_element_by_xpath(self.username_textbox).send_keys(username)
            print("Username is Entered")
        except Exception:
            print("Exception in Entering Username Method")
            self.takeScreenshot("Entering Username Method")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to enter password
    """

    def enter_login_password(self, password):
        try:
            wait = WebDriverWait(self.driver, 30)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.password_textbox)))
            wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.password_textbox)))
            self.driver.find_element_by_xpath(self.password_textbox).send_keys(password)
            print("Password is entered")
        except Exception:
            print("Exception in Entering Password Method")
            self.takeScreenshot("Entering Password Method")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to sign in to U-Pass holder application
    """

    def click_continue_signin(self):
        try:
            self.element_Is_Visible("xpath", self.signin_button)
            self.clickElement("xpath", self.signin_button)
            time.sleep(5)
            handles = self.driver.window_handles
            for handle in handles:
                self.driver.switch_to.window(handle)
            print("Signin Button is clicked")
        except Exception:
            print("Exception in Clicking Signin Method")
            self.takeScreenshot("Clicking Signin Method")
            raise Exception

    """
        @author             : Sreenivas reddy
        Description         : This method is used to select the service category type Virtual Appointment
    """

    def select_service_category_virtual_appointment(self):
        try:
            # title = self.driver.title
            # assert 'ScheduleAppointmentDetails' in title
            # print("Title of the page:", title)
            self.element_Is_Visible("xpath", self.service_category)
            self.clickElement("xpath", self.service_category)
            self.element_Is_Visible("xpath", self.virtual_appointment)
            element = self.getElement(self.virtual_appointment, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
            print("Selected Service Category is Virtual Appointment")
        except Exception:
            LOGGER.info("Exception in Selecting Service Category Virtual Appointment Method")
            self.takeScreenshot("Selecting Service Category Virtual Appointment Method")
            raise Exception

    """
            @author             : Sreenivas reddy
            Description         : This method is used to select the service category type Covid Testing
        """

    def select_service_category_covid_testing(self):
        try:
            # title = self.driver.title
            # assert 'ScheduleAppointmentDetails' in title
            # print("Title of the page:", title)
            self.element_Is_Visible("xpath", self.service_category)
            self.clickElement("xpath", self.service_category)
            self.element_Is_Visible("xpath", self.service_category_covid_testing)
            element = self.getElement(self.service_category_covid_testing, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
            print("Selected Service Category is Covid Testing")
        except Exception:
            LOGGER.info("Exception in Selecting Service Category Covid Testing Method")
            self.takeScreenshot("Selecting Service Category Covid Testing Method")
            raise Exception

    """
        @author             : Sreenivas reddy
        Description         : This method is used to select the service type Virtual Appointment
    """

    def select_service_type_virtual_appointment(self):
        try:
            self.element_Is_Visible("xpath", self.service_type)
            self.clickElement("xpath", self.service_type)
            self.element_Is_Visible("xpath", self.service_type_virtual_appointment)
            element = self.getElement(self.service_type_virtual_appointment, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
            print("Selected Service Type is Virtual Appointment")
        except Exception:
            LOGGER.info("Exception in Selecting Service Type Virtual Appointment Method")
            self.takeScreenshot("Selecting Service Type Virtual Appointment Method")
            raise Exception

    """
        @author             : Sreenivas reddy
        Description         : This method is used to select the service category type medical type
    """

    def select_service_category_medical(self):
        try:
            # title = self.driver.title
            # assert 'ScheduleAppointmentDetails' in title
            # print("Title of the page:", title)
            self.element_Is_Visible("xpath", self.service_category)
            self.clickElement("xpath", self.service_category)
            self.element_Is_Visible("xpath", self.service_category_medical)
            self.clickElement("xpath", self.service_category_medical)
            print("Selected Service Category is Medical")
        except Exception:
            LOGGER.info("Exception in Selecting Service Category Medical Method")
            self.takeScreenshot("Selecting Service Category Medical Method")
            raise Exception

    """
            @author             : Sreenivas reddy
            Description         : This method is used to select the service category type Vaccination
    """

    def select_service_category_vaccination(self):
        try:
            self.element_Is_Visible("xpath", self.service_category)
            self.clickElement("xpath", self.service_category)
            self.element_Is_Visible("xpath", self.service_category_vaccination)
            self.clickElement("xpath", self.service_category_vaccination)
            print("Selected Service Category is Vaccination ")
        except Exception:
            LOGGER.info("Exception in Selecting Service Category Vaccination Method")
            self.takeScreenshot("Selecting Service Category Vaccination Method")
            raise Exception

    """
        @author             : Sreenivas reddy
        Description         : This method is used to select the service type Antibody test
    """

    def select_service_type_antibody(self):
        try:
            self.element_Is_Visible("xpath", self.service_type)
            self.clickElement("xpath", self.service_type)
            self.element_Is_Visible("xpath", self.service_type_antibody_test)
            self.clickElement("xpath", self.service_type_antibody_test)
            print("Selected Service Type is Antibody")
        except Exception:
            LOGGER.info("Exception in Selecting Service Type Antibody Method")
            self.takeScreenshot("Selecting Service Type Antibody Method")
            raise Exception

    """
        @author             : Sreenivas reddy
        Description         : This method is used to select the service type Antigen test
    """

    def select_service_type_antigen(self):
        try:
            self.element_Is_Visible("xpath", self.service_type)
            self.clickElement("xpath", self.service_type)
            self.element_Is_Visible("xpath", self.service_type_antigen_test)
            self.clickElement("xpath", self.service_type_antigen_test)
            print("Selected service type is Antigen")
        except Exception:
            LOGGER.info("Exception in Selecting Service Type Antigen Method")
            self.takeScreenshot("Selecting Service Type Antigen Method")
            raise Exception

    """
        @author             : Sreenivas reddy
        Description         : This method is used to select the service type PCR test
    """

    def select_service_type_pcr(self):
        try:
            self.element_Is_Visible("xpath", self.service_type)
            self.clickElement("xpath", self.service_type)
            self.element_Is_Visible("xpath", self.service_type_pcr_test)
            self.clickElement("xpath", self.service_type_pcr_test)
            print("Selected Service Type is PCR")
        except Exception:
            LOGGER.info("Exception in Selecting Service Type PCR Method")
            self.takeScreenshot("Selecting Service Type PCR Method")
            raise Exception

    """
        @author             : Sreenivas reddy
        Description         : This method is used to select the service type vaccine
    """

    def select_service_type_vaccine(self):
        try:
            self.element_Is_Visible("xpath", self.service_type)
            self.clickElement("xpath", self.service_type)
            self.element_Is_Visible("xpath", self.service_type_covid_vaccine)
            self.clickElement("xpath", self.service_type_covid_vaccine)
            sleep(2)
            print("Selected Service Type is Covid-19 Vaccine")
        except Exception:
            LOGGER.info("Exception in Selecting Service Type Vaccine Method")
            self.takeScreenshot("Selecting Service Type Vaccine Method")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to Select Issuer Type
    """

    def click_issuer_btn(self):
        try:
            self.element_Is_Visible("xpath", self.issuer_btn)
            self.clickElement("xpath", self.issuer_btn)
            print("Selected default issuer")

        except Exception:
            LOGGER.info("Exception in Selecting Issuer")
            self.takeScreenshot("Selecting Issuer")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to Select Issuer Type Any
    """

    def select_issuer_any(self):
        try:
            self.element_Is_Visible("xpath", self.issuer_type_any)
            self.clickElement("xpath", self.issuer_type_any)
            print("Issuer type Any is selected")

        except Exception:
            LOGGER.info("Exception in Selecting Issuer type Any Method")
            self.takeScreenshot("Selecting Issuer type Any Method")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to Select Issuer Type CVS Pharmacy
    """

    def select_issuer_cvs_pharmacy(self):
        try:
            element = self.getElement(self.issuer_type_cvs, "xpath")
            self.element_Is_Visible("xpath", self.issuer_type_cvs)
            self.clickElement("xpath", self.issuer_type_cvs)
            print("Issuer type CVC Pharmacy is Selected")
        except Exception:
            print("Issuers are not available")
            LOGGER.info("Exception in Selecting Issuer type CVC Pharmacy Method")
            self.takeScreenshot("Selecting Issuer type CVC Pharmacy Method")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to Select Issuer Type Inspire Health
    """

    def select_issuer_inspire_health(self):
        try:
            self.element_Is_Visible("xpath", self.issuer_type_inspire)
            self.clickElement("xpath", self.issuer_type_inspire)
            print("Issuer type Inspire Health is Selected")
        except Exception:
            print("Issuers are not available")
            LOGGER.info("Exception in Selecting Issuer type Inspire Health method")
            self.takeScreenshot("Selecting Issuer type Inspire Health")
            raise Exception

    """
            @author             : Sreenivas
            Description         : This method is used to Select Issuer Type Inspire Health
        """

    def select_issuer_virtual_inspire_health(self):
        try:
            self.element_Is_Visible("xpath", self.virtual_issuer_type_inspire)
            self.clickElement("xpath", self.virtual_issuer_type_inspire)
            print("Issuer type Inspire Health is selected")
        except Exception:
            print("Issuers are not available")
            LOGGER.info("Exception in Select Issuer type Inspire Health method")
            self.takeScreenshot("Select Issuer type Inspire Health Method")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to Select Appointment Date
    """

    def select_choose_appointment_date_btn(self):
        try:
            self.element_Is_Visible("xpath", self.choose_appointment_date_btn)
            self.clickElement("xpath", self.choose_appointment_date_btn)
            sleep(1)
            print("Appointment Date is selected")
        except Exception:
            LOGGER.info("Exception in Selecting Appointment Date Method")
            self.takeScreenshot("Selecting Appointment Date Method")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to Clicking Find a Slot
    """

    def click_find_slot(self):
        try:
            element = self.driver.find_element_by_xpath(self.find_a_slot)
            self.driver.execute_script("arguments[0].click();", element)
            sleep(1)
            print("Find a Slot button is clicked")
        except Exception:
            LOGGER.info("Exception in Clicking Find a Slot Method")
            self.takeScreenshot("Clicking Find a Slot Method")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to Select Appointment slot
    """

    def select_appointment_slot(self):
        try:
            gettext = self.driver.find_element_by_xpath(self.book_slot).text
            if gettext == "No appointments available":
                self.clickElement("xpath", self.schedule_date_next)
                sleep(30)
                self.clickElement("xpath", self.book_slot)
                print("Appointment Slot is Selected")
            else:
                self.clickElement("xpath", self.book_slot)
                print("Appointment Slot is Selected")
        except Exception:
            print("Appointment Dates are not Available")
            LOGGER.info("Exception in Select Appointment Slot Method")
            self.takeScreenshot("Select Appointment Slot Method")
            raise Exception

    def select_reschedule_appointment_slot(self):
        try:
            gettext = self.driver.find_element_by_xpath(self.book_slot)
            if gettext == "No appointments available":
                self.clickElement("xpath", self.schedule_date_next)
                sleep(2)
                self.clickElement("xpath", self.reschedule_slot)
            else:
                self.clickElement("xpath", self.reschedule_slot)

            print("Selected Appointment slot")
        except Exception:
            LOGGER.info("Exception in Selecting Appointment Slot Method")
            self.takeScreenshot("Selecting Appointment Slot Method")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to Confirm Appointment slot
    """

    def select_confirm_appointment_slot(self):
        try:
            self.element_Is_Visible("xpath", self.confirm_slot)
            self.clickElement("xpath", self.confirm_slot)
            sleep(1)
            print("Selected Appointment slot is confirmed")
        except Exception:
            LOGGER.info("Exception in Confirm Appointment slot Method")
            self.takeScreenshot("confirm Appointment slot")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to Click Review All Details
    """

    def click_review_all_details(self):
        try:
            self.element_Is_Visible("xpath", self.review_all_details)
            element = self.getElement(self.review_all_details, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
            sleep(1)
            print("Review All Details button is Clicked")
        except Exception:
            LOGGER.info("Exception in Clicking Review All Details Method")
            self.takeScreenshot("Clicking Review All Details Method")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to Click Confirm Appointment
    """

    def click_confirm_appointment(self):
        try:
            title = self.driver.title
            assert 'ScheduleAppointmentDetails' in title
            print("Title of the page:", title)
            self.element_Is_Visible("xpath", self.confirm_appointment)
            element = self.getElement(self.confirm_appointment, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
            sleep(1)
            print("Confirm Appointment button is Clicked")
        except Exception:
            LOGGER.info("Exception in Clicking Confirm Appointment Method")
            self.takeScreenshot("Clicking Confirm Appointment Method")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to Confirm Appointment slot
    """

    def select_confirm_reschedule_appointment_slot(self):
        try:
            sleep(1)
            self.clickElement("xpath", self.reschedule_slot)
            print("Selected Appointment slot is confirmed")
        except Exception:
            LOGGER.info("Exception in Confirm Appointment slot Method")
            self.takeScreenshot("confirm Appointment slot")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to Verify Appointment
    """

    def verify_appointment_scheduled(self):
        try:
            data = ReadData()
            test_data = data.get_test_data()
            self.element_Is_Visible("xpath", self.appointment_scheduled_message)
            actual = self.driver.find_element_by_xpath(self.appointment_scheduled_message).text
            expected = test_data["validation"]["verify appointment"]
            if actual == expected:
                assert True
                print(actual)
            else:
                assert False
        except Exception:
            LOGGER.info("Exception in Verifying Appointment Method")
            self.takeScreenshot("Verifying Appointment Method")
            raise Exception

    """
            @author             : Sreenivas
            Description         : This method is used to Verify Appointment
        """

    def verify_dependent_appointment_scheduled(self):
        try:
            data = ReadData()
            test_data = data.get_test_data()
            self.element_Is_Visible("xpath", self.appointment_scheduled_message)
            actual = self.driver.find_element_by_xpath(self.appointment_scheduled_message).text
            print(actual)
            expected = test_data["validation"]["appointment dependent"]
            if actual == expected:
                assert True
            else:
                assert False
        except Exception:
            LOGGER.info("Exception in Verify Appointment Method")
            self.takeScreenshot("Verify Appointment Method")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to see your information 
    """

    def click_your_info_btn(self):
        try:
            sleep(3)
            page_down = self.driver.find_element_by_tag_name('html')
            page_down.send_keys(Keys.END)
            self.element_Is_Visible("xpath", self.your_info_btn)
            self.clickElement("xpath", self.your_info_btn)
            sleep(2)
            print("your information button is clicked")
        except Exception:
            LOGGER.info("Exception in Clicking your information button method")
            self.takeScreenshot("Clicking your information button")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to click next button in schedule appointment page
    """

    def click_next(self):
        try:
            self.element_Is_Visible("xpath", self.next_btn)
            element = self.driver.find_element_by_xpath(self.next_btn)
            self.driver.execute_script("arguments[0].click();", element)
            sleep(1)
            print("Next button is clicked")
        except Exception:
            LOGGER.info("Exception in Click Next method")
            self.takeScreenshot("click next")
            raise Exception

    """
        @author             : Sreenivas 
        Description         : This method is used to schedule an appointment
    """

    def click_schedule_appointment(self):
        try:
            title = self.driver.title
            assert 'MyAppointments' in title
            print("Title of the page:", title)
            if self.getElement(self.schedule_appointment_btn, "xpath").is_displayed():
                self.clickElement("xpath", self.schedule_appointment_btn)
            else:
                self.clickElement("xpath", self.schedule_new_appointment)
            print("Schedule Appointment button is clicked")
        except Exception:
            LOGGER.info("Exception in clicking schedule appointment")
            self.takeScreenshot("clicking schedule an new appointment")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to Click Schedule button
    """

    def click_schedule(self):
        try:
            self.element_Is_Visible("xpath", self.schedule_btn)
            element = self.driver.find_element_by_xpath(self.schedule_btn)
            self.driver.execute_script("arguments[0].click();", element)
            print("Schedule button is clicked")
        except Exception:
            LOGGER.info("Exception in Click schedule method")
            self.takeScreenshot("click schedule")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to Click Scheduled Appointments
    """

    def click_scheduled_appointment(self):
        try:
            if self.getElement(self.view_appointment, "xpath").is_displayed():
                self.clickElement("xpath", self.view_appointment)
                print("Scheduled Appointment is Selected")
            else:
                print("No Scheduled Appointments")
        except Exception:
            print("No Scheduled Appointments")
            LOGGER.info("Exception in Click Scheduled Appointment method")
            self.takeScreenshot("click scheduled Appointment")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to Reschedule Appointments
    """

    def click_edit_scheduled_appointment(self):
        try:
            self.element_Is_Visible("xpath", self.edit_appointment)
            self.clickElement("xpath", self.edit_appointment)
            print("Edit button is clicked")
        except Exception:
            LOGGER.info("Exception in Clicking Edit button method")
            self.takeScreenshot("Clicking Edit button method")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to Click Scheduled Appointments
    """

    def click_scheduled_appointment_dependent(self):
        try:
            view = self.driver.find_element_by_xpath(self.view_dependent_appointment)
            if view.is_displayed():
                self.driver.execute_script("arguments[0].click();", view)
                print("Scheduled Appointment is clicked")
            else:
                print("You have not scheduled any appointments yet")
        except Exception:
            print("No Scheduled Appointments")
            LOGGER.info("Exception in Click Scheduled Appointment method")
            self.takeScreenshot("click scheduled Appointment")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to Click Cancel Scheduled Appointments
    """

    def click_cancel_scheduled_appointment(self):
        try:
            sleep(2)
            title = self.driver.title
            # assert 'Profile' in title
            print("Title of the page:", title)
            element = self.driver.find_element_by_xpath(self.cancel_appointment)
            self.driver.execute_script("arguments[0].click();", element)
            print("Cancel Appointment button is clicked")
            self.element_Is_Visible("xpath", self.confirm_cancel_appointment)
            self.clickElement("xpath", self.confirm_cancel_appointment)
        except Exception:
            LOGGER.info("Exception in Clicking Cancel Appointment method")
            self.takeScreenshot("click cancel Appointment")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to Verify Cancel Scheduled Appointments
    """

    def verify_cancel_scheduled_appointment(self):
        try:
            data = ReadData()
            test_data = data.get_test_data()
            self.element_Is_Visible("xpath", self.verify_cancel_appointment_message)
            actual = self.driver.find_element_by_xpath(self.verify_cancel_appointment_message).text
            print(actual)
            expected = test_data["validation"]["cancel appointment"]
            if actual == expected:
                assert True
                print("Appointment is Cancelled")
            else:
                assert False
        except Exception:
            LOGGER.info("Exception in Verifying Cancel Appointment method")
            self.takeScreenshot("Verifying cancel Appointment")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to Click Scheduled Appointments
    """

    def click_dependent_scheduled_appointment(self):
        try:
            sleep(5)
            gettext = self.driver.find_element_by_xpath(self.dependent_schedule_appointment).text
            if gettext == "You have not scheduled any appointments yet":
                element = self.driver.find_element_by_xpath(self.dependent_schedule_appointment_1)
                self.driver.execute_script("arguments[0].click();", element)
            else:
                element = self.driver.find_element_by_xpath(self.dependent_schedule_appointment_1)
                self.driver.execute_script("arguments[0].click();", element)
        except Exception:
            LOGGER.info("Exception in Click Scheduled Appointment method")
            self.takeScreenshot("click scheduled Appointment")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to Enter Additional Questions
    """

    def enter_additional_questions(self):
        try:
            data = ReadData()
            test_data = data.get_test_data()
            sleep(2)
            self.element_Is_Visible("xpath", self.covid_test_yes)
            element = self.getElement(self.covid_test_yes, "xpath")
            self.driver.execute_script("arguments[0].click();", element)

            self.element_Is_Visible("xpath", self.fever_chills)
            element = self.getElement(self.fever_chills, "xpath")
            self.driver.execute_script("arguments[0].click();", element)

            self.element_Is_Visible("xpath", self.nausea)
            element = self.getElement(self.nausea, "xpath")
            self.driver.execute_script("arguments[0].click();", element)

            self.element_Is_Visible("xpath", self.headache)
            element = self.getElement(self.headache, "xpath")
            self.driver.execute_script("arguments[0].click();", element)

            self.element_Is_Visible("xpath", self.dizziness)
            element = self.getElement(self.dizziness, "xpath")
            self.driver.execute_script("arguments[0].click();", element)

            self.element_Is_Visible("xpath", self.fatigue)
            element = self.getElement(self.fatigue, "xpath")
            self.driver.execute_script("arguments[0].click();", element)

            self.element_Is_Visible("xpath", self.difficulty_breathing)
            element = self.getElement(self.difficulty_breathing, "xpath")
            self.driver.execute_script("arguments[0].click();", element)

        except Exception:
            LOGGER.info("Exception in Entering Additional Details Method")
            self.takeScreenshot("Entering Additional Details Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Enter Allergies
    """

    def enter_allergies(self, name):
        try:
            sleep(2)
            self.element_Is_Visible("xpath", self.allergies)
            element = self.getElement(self.allergies, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
            sleep(2)
            self.enterText("xpath", self.allergies, name)
            print("Allergies entered")

            self.element_Is_Visible("xpath", self.gender)
            element = self.getElement(self.gender, "xpath")
            self.driver.execute_script("arguments[0].click();", element)

            self.element_Is_Visible("xpath", self.gender_m)
            element = self.getElement(self.gender_m, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
        except Exception:
            print("Exception in Enter Allergies Method")
            self.takeScreenshot("Enter Allergies Method")
            raise Exception

    """
        @author        : Sreenivas reddy
        Description    : This method is used to Enter Address
    """

    def enter_address(self, name):
        try:
            self.element_Is_Visible("xpath", self.address_field)
            element = self.getElement(self.address_field, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
            sleep(2)
            self.enterText("xpath", self.address_field, name)
            print("Address is entered")

            self.element_Is_Visible("xpath", self.i_am_over_18)
            element = self.getElement(self.i_am_over_18, "xpath")
            self.driver.execute_script("arguments[0].click();", element)

            self.element_Is_Visible("xpath", self.i_am_over_18)
            element = self.getElement(self.i_am_over_18, "xpath")
            self.driver.execute_script("arguments[0].click();", element)

            self.element_Is_Visible("xpath", self.i_am_over_18)
            element = self.getElement(self.i_am_over_18, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
        except Exception:
            print("Exception in Entering Address Method")
            self.takeScreenshot("Entering Address Method")
            raise Exception

    """
        @author             : Sreenivas
        Description         : This method is used to click the appointments under get care
    """

    def click_appointments(self):
        try:
            self.element_Is_Visible("xpath", self.appointments_btn)
            self.clickElement("xpath", self.appointments_btn)
            print("Appointment button is clicked")
            sleep(2)
        except Exception:
            LOGGER.info("Exception in click appointment method")
            self.takeScreenshot("click appointments")
            raise Exception

    """
        @author             : sreenivas
        Description         : This method is used to order a home kit
    """

    def click_home_kit_order(self):
        try:
            self.element_Is_Visible("xpath", self.at_homekit_btn)
            self.clickElement("xpath", self.at_homekit_btn)
            print("At Home Kit Order Button is clicked")
        except Exception:
            LOGGER.info("Exception in Clicking Home Kit Order Method")
            self.takeScreenshot("Clicking Home Kit Order Method")
            raise Exception

    """
        @author             : sreenivas
        Description         : This method is used to Click Start Order Button
    """

    def click_start_order(self):
        try:
            title = self.driver.title
            assert 'Orders' in title
            print("Title of the page:", title)
            self.element_Is_Visible("xpath", self.start_order)
            element = self.getElement(self.start_order, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
            print("Start Order Button is clicked")
        except Exception:
            LOGGER.info("Exception in Clicking Start Order Button method")
            self.takeScreenshot("Clicking Start Order Button")
            raise Exception

    """
        @author             : sreenivas
        Description         : This method is used to Select Quantity of Antigen Test Kits
    """

    def select_antigen_test(self):
        try:
            # title = self.driver.title
            # assert 'Products' in title
            # print("Title of the page:", title)
            self.element_Is_Visible("xpath", self.order_antigen_kit)
            element = self.getElement(self.order_antigen_kit, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
            print("Selected Antigen Test Kit")
        except Exception:
            LOGGER.info("Exception in Selecting Antigen Test method")
            self.takeScreenshot("Selecting Antigen Test method")
            raise Exception

    """
        @author             : sreenivas
        Description         : This method is used to Select Quantity of Non Zero Product Test Kits
    """

    def select_non_zero_product(self):
        try:
            # title = self.driver.title
            # assert 'Products' in title
            # print("Title of the page:", title)
            self.element_Is_Visible("xpath", self.order_non_zero_product)
            element = self.getElement(self.order_non_zero_product, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
            print("Selected Antigen Test Kit")
        except Exception:
            LOGGER.info("Exception in Selecting Antigen Test method")
            self.takeScreenshot("Selecting Antigen Test method")
            raise Exception

    """
        @author             : sreenivas
        Description         : This method is used to Select Quantity of Antigen Test Kits
    """

    def select_antigen_test1(self):
        try:
            # title = self.driver.title
            # assert 'Products' in title
            # print("Title of the page:", title)
            self.element_Is_Visible("xpath", self.order_antigen_kit1)
            element = self.getElement(self.order_antigen_kit1, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
            print("Selected Antigen Test Kit")
        except Exception:
            LOGGER.info("Exception in Selecting Antigen Test method")
            self.takeScreenshot("Selecting Antigen Test method")
            raise Exception

    """
        @author             : sreenivas
        Description         : This method is used to Select Quantity of PCR Test Kits
    """

    def select_pcr_test(self):
        try:
            # title = self.driver.title
            # assert 'Products' in title
            # print("Title of the page:", title)
            self.element_Is_Visible("xpath", self.order_pcr_kit)
            element = self.getElement(self.order_pcr_kit, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
            print("Selected PCR Test Kit")
        except Exception:
            LOGGER.info("Exception in Selecting PCR Test method")
            self.takeScreenshot("Selecting PCR Test method")
            raise Exception

    """
        @author             : sreenivas
        Description         : This method is used to Select Quantity of Antibody Test Kits
    """

    def select_antibody_test(self):
        try:
            title = self.driver.title
            assert 'Products' in title
            print("Title of the page:", title)
            self.element_Is_Visible("xpath", self.order_antibody_kit)
            element = self.getElement(self.order_antibody_kit, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
            print("Selected Quantity of Antibody Test Kit")
        except Exception:
            LOGGER.info("Exception in Selecting Antibody Test method")
            self.takeScreenshot("Selecting Antibody Test method")
            raise Exception

    """
        @author             : sreenivas
        Description         : This method is used to Select Quantity of Antigen Self Test Kits
    """

    def select_antigen_self_kit(self):
        try:
            title = self.driver.title
            assert 'Products' in title
            print("Title of the page:", title)
            self.element_Is_Visible("xpath", self.order_Antigen_Self_Test)
            element = self.getElement(self.order_Antigen_Self_Test, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
            print("Selected Quantity of Antigen Self Test Kit")
        except Exception:
            LOGGER.info("Exception in Selecting Antigen Self Test method")
            self.takeScreenshot("Selecting Antigen Self Test method")
            raise Exception

    """
        @author             : sreenivas
        Description         : This method is used to Click Check Out
    """

    def click_check_out(self):
        try:
            self.element_Is_Visible("xpath", self.check_out)
            element = self.getElement(self.check_out, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
            print("Check Out button is Clicked")
        except Exception:
            LOGGER.info("Exception in Clicking Check Out button method")
            self.takeScreenshot("Clicking Check Out button method")
            raise Exception

    """
        @author             : sreenivas
        Description         : This method is used to Enter Fullname
    """

    def enter_shipping_fullname(self, name):
        try:
            title = self.driver.title
            assert 'Shipping' in title
            print("Title of the page:", title)
            self.element_Is_Visible("xpath", self.shipping_fullname)
            self.clickElement("xpath", self.shipping_fullname)
            sleep(1)
            self.driver.find_element_by_xpath(self.shipping_fullname).clear()
            self.enterText("xpath", self.shipping_fullname, name)
            sleep(1)
            print("Fullname is Entered")
        except Exception:
            LOGGER.info("Exception in Entering Fullname method")
            self.takeScreenshot("Entering Fullname method")
            raise Exception

    """
        @author             : sreenivas
        Description         : This method is used to Enter Phone Number
    """

    def enter_shipping_phone_number(self, phone):
        try:
            self.element_Is_Visible("xpath", self.shipping_phone_number)
            element = self.getElement(self.shipping_phone_number, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
            sleep(1)
            self.driver.find_element_by_xpath(self.shipping_phone_number).clear()
            self.enterText("xpath", self.shipping_phone_number, phone)
            print("Phone Number is Entered")
        except Exception:
            LOGGER.info("Exception in Entering Phone Number method")
            self.takeScreenshot("Entering Phone Number method")
            raise Exception

    """
        @author             : sreenivas
        Description         : This method is used to Enter Shipping Address
    """

    def enter_shipping_address(self, address):
        try:
            self.element_Is_Visible("xpath", self.shipping_address)
            element = self.getElement(self.shipping_address, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
            sleep(1)
            self.driver.find_element_by_xpath(self.shipping_address).clear()
            self.enterText("xpath", self.shipping_address, address)
            time.sleep(3)
            element1 = self.getElement(self.shipping_address_input, "xpath")
            self.driver.execute_script("arguments[0].click();", element1)
            print("Shipping Address is Entered")
        except Exception:
            LOGGER.info("Exception in Entering Shipping Address method")
            self.takeScreenshot("Entering Shipping Address method")
            raise Exception

    """
        @author             : sreenivas
        Description         : This method is used to Click Next 
    """

    def click_order_next(self):
        try:
            self.element_Is_Visible("xpath", self.order_next)
            element = self.getElement(self.order_next, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
            print("Next button is clicked")
            sleep(5)
        except Exception:
            LOGGER.info("Exception in Clicking Next button method")
            self.takeScreenshot("Clicking Next button method")
            raise Exception

    """
            @author             : sreenivas
            Description         : This method is used to Place Order
        """

    def click_place_order(self):
        try:
            self.element_Is_Visible("xpath", self.place_order)
            element = self.getElement(self.place_order, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
            print("Place Order is clicked")
            sleep(5)
        except Exception:
            LOGGER.info("Exception in Clicking Place Order method")
            self.takeScreenshot("Clicking Place Order method")
            raise Exception

    """
        @author             : sreenivas
        Description         : This method is used to Enter Card Number 
    """

    def enter_card_number(self, number):
        try:
            sleep(5)
            # title = self.driver.title
            # assert 'Checkout' in title
            # print("Title of the page:", title)
            a = self.driver.find_element_by_xpath(self.submit)
            actions = ActionChains(self.driver)
            actions.move_to_element(a).perform()
            self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.iframe))
            self.element_Is_Visible("xpath", self.card_number)
            self.enterText("xpath", self.card_number, number)
            print("Card Number is Entered")
            self.driver.switch_to.default_content()
        except Exception:
            LOGGER.info("Exception in Entering Card Number method")
            self.takeScreenshot("Entering Card Number method")
            raise Exception

    """
        @author             : sreenivas
        Description         : This method is used to Enter Expiry Date 
    """

    def enter_expiry_date(self, number):
        try:
            self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.iframe))
            self.element_Is_Visible("xpath", self.expiry_date)
            sleep(1)
            self.enterText("xpath", self.expiry_date, number)
            print("Expiry Date is Entered")
            self.driver.switch_to.default_content()
            sleep(1)
        except Exception:
            LOGGER.info("Exception in Entering Expiry Date method")
            self.takeScreenshot("Entering Expiry Date method")
            raise Exception

    """
        @author             : sreenivas
        Description         : This method is used to Enter CVC Number
    """

    def enter_cvc(self, number):
        try:
            self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.iframe))
            self.element_Is_Visible("xpath", self.cvc)
            sleep(1)
            self.enterText("xpath", self.cvc, number)
            print("CVC number is Entered")
            self.driver.switch_to.default_content()
            sleep(2)
        except Exception:
            LOGGER.info("Exception in Entering CVC number method")
            self.takeScreenshot("Entering CVC number method")
            raise Exception

    """
        @author             : sreenivas
        Description         : This method is used to Clicking Submit Button
    """

    def click_submit(self):
        try:
            self.element_Is_Visible("xpath", self.submit)
            element = self.getElement(self.submit, "xpath")
            self.driver.execute_script("arguments[0].click();", element)
            print("Submit Button is Clicked")
        except Exception:
            LOGGER.info("Exception in Clicking Submit Button method")
            self.takeScreenshot("Clicking Submit Button method")
            raise Exception

    """
        @author             : sreenivas
        Description         : This method is used to Verifying order
    """

    def verify_order_(self):
        try:
            data = ReadData()
            test_data = data.get_test_data()
            self.element_Is_Visible("xpath", self.verify_order)
            verify = self.driver.find_element_by_xpath(self.verify_order).text
            verify_order_text = test_data["validation"]["verify order"]
            if verify == verify_order_text:
                assert True
                print("Order has been placed")
        except Exception:
            LOGGER.info("Exception in Clicking Submit Button method")
            self.takeScreenshot("Clicking Submit Button method")
            raise Exception

    """
        @author             : sreenivas reddy
        Description         : This method is used to Get User Unique Id
    """

    def get_unique_id(self):
        try:
            sleep(20)
            global Unique_id
            self.element_Is_Visible("xpath", self.unique_id)
            Unique_id = self.driver.find_element_by_xpath(self.unique_id).text
            print(Unique_id)
            self.data.write_data_into_excel1(2, 2, Unique_id)
            return Unique_id
        except Exception:
            print("Exception in Get Unique Id method")
            self.takeScreenshot("Get Unique Id method")
            raise Exception

    """
        @author             : sreenivas reddy
        Description         : This method is used to Click Notification Bell Icon
    """

    def click_notification_bell_icon(self):
        try:
            sleep(2)
            self.element_Is_Visible("xpath", self.notification_bell_icon)
            # self.clickElement("xpath", self.notification_bell_icon)
            element = self.driver.find_element_by_xpath(self.notification_bell_icon)
            self.driver.execute_script("arguments[0].click();", element)
            print("Notification Bell Icon is clicked")
        except Exception:
            print("Exception in Clicking Notification Bell Icon method")
            self.takeScreenshot("Clicking Notification Bell Icon method")
            raise Exception

    """
        @author             : sreenivas reddy
        Description         : This method is used to Click See Request 
    """

    def click_see_request(self):
        try:
            sleep(10)
            self.element_Is_Visible("xpath", self.see_request)
            element = self.driver.find_element_by_xpath(self.see_request)
            self.driver.execute_script("arguments[0].click();", element)
            print("See Request Button is clicked")
        except Exception:
            print("Exception in Clicking See Request Button method")
            self.takeScreenshot("Clicking See Request Button method")
            raise Exception

    """
        @author             : sreenivas reddy
        Description         : This method is used to Click Approve Once Button
    """

    def click_approve_once(self):
        try:
            self.element_Is_Visible("xpath", self.approve_once)
            element = self.driver.find_element_by_xpath(self.approve_once)
            self.driver.execute_script("arguments[0].click();", element)
            print("Approve Once Button is clicked")
        except Exception:
            print("Exception in Clicking Approve Once Button method")
            self.takeScreenshot("Clicking Approve Once Button method")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to clicking the hamburger icon
    """

    def click_hamburger_icon(self):
        try:
            self.element_Is_Visible("xpath", self.hamburger_icon)
            self.driver.find_element_by_xpath(self.hamburger_icon).click()
            sleep(2)
            print("Click hamburger button")
        except Exception:
            print("Exception in clicking hamburger icon method")
            self.takeScreenshot("click hamburger icon")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to click to reset U-Pass id
    """

    def click_reset_id(self):
        try:
            self.element_Is_Visible("xpath", self.reset_id)
            self.clickElement("xpath", self.reset_id)
            sleep(2)
            print("Reset U-Pass id of user successfully")
        except Exception:
            print("Exception in click reset id")
            self.takeScreenshot("click reset U-Pass id")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to view scan history
    """

    def click_view_scan_history(self):
        try:
            self.element_Is_Visible("xpath", self.view_scan_history)
            self.clickElement("xpath", self.view_scan_history)
            print("view scan history of user")
        except Exception:
            LOGGER.info("Exception in click view scan history")
            self.takeScreenshot("click view scan history")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to download JPEG QR code
    """

    def click_download_qr_code(self):
        try:
            self.element_Is_Visible("xpath", self.download_qr_code)
            self.clickElement("xpath", self.download_qr_code)
            sleep(3)
            print("download QR code of user")
        except Exception:
            LOGGER.info("Exception in download QR code")
            self.takeScreenshot("Download QR code")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to click to get care
    """

    def click_get_care(self):
        try:
            self.element_Is_Visible("xpath", self.get_care_btn)
            title = self.driver.title
            assert 'Pass' in title
            print("Title of the page:", title)
            self.driver.find_element_by_xpath(self.get_care_btn).click()
            sleep(5)
            print("Get care button is clicked")
        except Exception:
            LOGGER.info("Exception in get care method")
            self.takeScreenshot("click get care")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to click where button
    """

    def click_places_btn(self):
        try:
            self.element_Is_Visible("xpath", self.place_btn)
            self.clickElement("xpath", self.place_btn)
            LOGGER.info("Click Places button")
        except Exception:
            LOGGER.info("Exception in click places method")
            self.takeScreenshot("click places")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to search place
    """

    def click_search_bar(self, search):
        try:
            self.element_Is_Visible("xpath", self.search_tb)
            self.clickElement("xpath", self.search_tb)
            self.enterText("xpath", self.search_tb, search)
            pyautogui.press('Enter')
            sleep(1)
            LOGGER.info("click search bar")
        except Exception:
            LOGGER.info("Exception in click search bar method")
            self.takeScreenshot("click search bar")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used to select the shs(Sunset High School) students program
    """

    def click_shs_students_program(self):
        try:
            self.element_Is_Visible("xpath", self.shs_students_program)
            self.clickElement("xpath", self.shs_students_program)
            sleep(3)
            print("SHS Students Program clicked successfully")
        except Exception:
            print("Exception in click shs students program method")
            self.takeScreenshot("click shs students program")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used to select the shs(Sunset High School) athletics program
    """

    def click_shs_athletics_program(self):
        try:
            self.element_Is_Visible("xpath", self.shs_athletics_program)
            self.clickElement("xpath", self.shs_athletics_program)
            sleep(3)
            print("SHS Athletics Program clicked successfully")
        except Exception:
            print("Exception in click shs athletics program method")
            self.takeScreenshot("click shs athletics program")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used to select the shs(Sunset High School) Employees program
    """

    def click_shs_employees_vaccinated_program(self):
        try:
            self.element_Is_Visible("xpath", self.shs_employees_vaccinated_program)
            self.clickElement("xpath", self.shs_employees_vaccinated_program)
            sleep(3)
            print("SHS Employees vaccinated Program clicked successfully")
        except Exception:
            print("Exception in click shs employees vaccinated program method")
            self.takeScreenshot("click shs athletics program")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used to favourite the program 
    """

    def select_favourite_program(self):
        try:
            self.element_Is_Visible("xpath", self.favourite_program)
            self.clickElement("xpath", self.favourite_program)
            sleep(2)
            print("Selected Program favourite successfully")
        except Exception:
            print("Exception in select favourite program method")
            self.takeScreenshot("select favourite program")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used to Un-favourite the program 
    """

    def unselect_favourite_program(self):
        try:
            self.element_Is_Visible("xpath", self.un_favourite_program)
            self.clickElement("xpath", self.un_favourite_program)
            print("Unselected favourite program successfully")
        except Exception:
            print("Exception in unselect favourite program method")
            self.takeScreenshot("unselect favourite program")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used to click the requirements of a selected program
    """

    def click_requirements(self):
        try:
            self.element_Is_Visible("xpath", self.requirements_btn)
            self.clickElement("xpath", self.requirements_btn)
            sleep(3)
            print("Requirements clicked successfully")
        except Exception:
            print("Exception in click requirements button method")
            self.takeScreenshot("click requirements button")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used to verify the health tab under requirements page
    """

    def verify_health_tb(self):
        try:
            self.element_Is_Visible("xpath", self.verify_health)
            health_tb = self.driver.find_element_by_xpath(self.verify_health).text
            print(health_tb)
            if health_tb == 'HEALTH' or 'Health':
                assert True
                print("Health tab verified successfully")
            else:
                assert False
        except Exception:
            print("Exception in Verify Health tab under Requirements page")
            self.takeScreenshot("Verify health tab under requirements page")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to click the records
    """

    def click_records(self):
        try:
            sleep(2)
            self.element_Is_Visible("xpath", self.records_btn)
            self.clickElement("xpath", self.records_btn)
            sleep(2)
            LOGGER.info("Click records")
        except Exception:
            LOGGER.info("Exception in click records method")
            self.takeScreenshot("click records")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to click Add/Get record
    """

    def click_add_or_get_record(self):
        try:
            self.element_Is_Visible("xpath", self.add_or_record_btn)
            self.clickElement("xpath", self.add_or_record_btn)
            sleep(2)
            LOGGER.info("click add/get record button")
        except Exception:
            LOGGER.info("Exception in click add or get record method")
            self.takeScreenshot("click add or get record")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to scan document
    """

    def click_scan_document(self):
        try:
            self.element_Is_Visible("xpath", self.scan_document_btn)
            self.clickElement("xpath", self.scan_document_btn)
            sleep(2)
            print("Scan document clicked successfully")
        except Exception:
            LOGGER.info("Exception in scan document method")
            self.takeScreenshot("click scan document")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to scan code
    """

    def click_scan_code(self):
        try:
            scan = self.driver.find_element_by_xpath(self.scan_code_btn)
            self.driver.execute_script("arguments[0].click();", scan)
            print("Scan code button clicked successfully")
        except Exception:
            LOGGER.info("Exception in click scan code method")
            self.takeScreenshot("click scan code")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to link the record
    """

    def click_to_link_record(self):
        try:
            self.element_Is_Visible("xpath", self.link_to_record)
            self.clickElement("xpath", self.link_to_record)
            LOGGER.info("click to link record")
        except Exception:
            LOGGER.info("Exception in link record method")
            self.takeScreenshot("click to link record")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to select holder name(Scan document/Scan code/Link record)
    """

    def select_holder_name(self):
        try:
            self.element_Is_Visible("xpath", self.name_tb)
            self.clickElement("xpath", self.name_tb)
            self.clickElement("xpath", self.first_name)
        except Exception:
            print("Exception in select holder method")
            self.takeScreenshot("Select holder name")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to select record category type 'Health'
    """

    def select_record_category_health(self):
        try:
            self.element_Is_Visible("xpath", self.record_category)
            self.clickElement("xpath", self.record_category)
            self.clickElement("xpath", self.record_category_health)
        except Exception:
            print("Exception in select_record_category_health method")
            self.takeScreenshot("select_record_category_health")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to select record type covid pcr test
    """

    def select_record_type_covid_pcr(self):
        try:
            self.element_Is_Visible("xpath", self.record_type)
            self.clickElement("xpath", self.record_type)
            self.clickElement("xpath", self.record_type_covid_pcr_test)
            sleep(2)
        except Exception:
            print("Exception in select_record_type_covid_pcr method")
            self.takeScreenshot("select_record_type_covid_pcr")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to select record type covid vaccination
    """

    def select_record_type_covid_vaccination(self):
        try:
            self.element_Is_Visible("xpath", self.record_type)
            self.clickElement("xpath", self.record_type)
            self.clickElement("xpath", self.record_type_covid_vaccination)
            sleep(2)
        except Exception:
            print("Exception in select_record_type_covid_vaccination method")
            self.takeScreenshot("select_record_type_covid_vaccination")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to select record type covid 19 test antigen
    """

    def select_record_type_covid_19_test_antigen(self):
        try:
            self.element_Is_Visible("xpath", self.record_type)
            self.clickElement("xpath", self.record_type)
            self.clickElement("xpath", self.record_type_covid_19_test_antigen)
            sleep(2)
        except Exception:
            print("Exception in select_record_type_covid__19_test_antigen method")
            self.takeScreenshot("select_record_type_covid__19_test_antigen")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to select record type immunization
    """

    def select_record_type_immunization(self):
        try:
            self.element_Is_Visible("xpath", self.record_type)
            self.clickElement("xpath", self.record_type)
            self.clickElement("xpath", self.record_type_immunization)
            sleep(2)
        except Exception:
            print("Exception in select_record_type_immunization method")
            self.takeScreenshot("select_record_type_immunization")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to select record type covid 19 test antibody
    """

    def select_record_type_covid_19_test_antibody(self):
        try:
            self.element_Is_Visible("xpath", self.record_type)
            self.clickElement("xpath", self.record_type)
            self.clickElement("xpath", self.record_type_covid_19_test_antibody)
            sleep(2)
        except Exception:
            print("Exception in select_record_type_covid_19_test_anitbody method")
            self.takeScreenshot("select_record_type_covid_19_test_anitbody")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to select record type covid 19 rt pcr
    """

    def select_record_type_covid_19_rt_pcr(self):
        try:
            self.element_Is_Visible("xpath", self.record_type)
            self.clickElement("xpath", self.record_type)
            self.clickElement("xpath", self.record_type_covid_19_rt_pcr)
            sleep(2)
        except Exception:
            print("Exception in select_record_type_covid_19_rt_pcr method")
            self.takeScreenshot("select_record_type_covid_19_rt_pcr")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to select issuer for health 'CDC'
    """

    def select_issuer_type_cdc(self):
        try:
            self.element_Is_Visible("xpath", self.issuer_type)
            self.clickElement("xpath", self.issuer_type)
            sleep(1)
            self.clickElement("xpath", self.issuer_type_cdc)
            print("CDC type health issuer selected successfully")
        except Exception:
            print("Exception in select issuer type cdc for health method")
            self.takeScreenshot("select issuer type cdc")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to select issuer for health 'Inspire health'
    """

    def select_issuer_type_inspire_health(self):
        try:
            self.element_Is_Visible("xpath", self.issuer_type)
            self.clickElement("xpath", self.issuer_type)
            sleep(1)
            self.clickElement("xpath", self.issuer_type_inspire_health)
            print("Inspire health issuer selected successfully")
        except Exception:
            print("Exception in select issuer type inspire health method")
            self.takeScreenshot("select issuer type inspire health")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to select issuer for Covid-19 RT-PCR health 'Inspire health'
    """

    def select_issuer_type_inspire_health_1(self):
        try:
            self.element_Is_Visible("xpath", self.issuer_type)
            self.clickElement("xpath", self.issuer_type)
            sleep(1)
            self.clickElement("xpath", self.issuer_type_inspire_health_1)
            print("Inspire health 1 issuer selected successfully")
        except Exception:
            print("Exception in select issuer type inspire health 1 method")
            self.takeScreenshot("select issuer type inspire health 1")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to select record category type ID
    """

    def select_record_category_id(self):
        try:
            self.element_Is_Visible("xpath", self.record_category)
            self.clickElement("xpath", self.record_category)
            self.clickElement("xpath", self.record_category_id)
        except Exception:
            print("Exception in select_record_category_id method")
            self.takeScreenshot("select_record_category_id")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to select record type driver's license
    """

    def select_record_type_driver_license(self):
        try:
            self.element_Is_Visible("xpath", self.record_type)
            self.clickElement("xpath", self.record_type)
            self.clickElement("xpath", self.record_type_driver_license)
            sleep(2)
        except Exception:
            print("Exception in select_record_type_driver_license method")
            self.takeScreenshot("select_record_type_driver_license")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to select record type employee card
    """

    def select_record_type_employee_id_card(self):
        try:
            self.element_Is_Visible("xpath", self.record_type)
            self.clickElement("xpath", self.record_type)
            self.clickElement("xpath", self.record_type_employee_id_card)
            sleep(2)
        except Exception:
            print("Exception in select_record_type_employee_id_card method")
            self.takeScreenshot("select_record_type_employee_id_card")
            raise Exception

    """
         @author             : Somasekhar
         Description         : This method is used to select record type passport
    """

    def select_record_type_passport(self):
        try:
            self.element_Is_Visible("xpath", self.record_type)
            self.clickElement("xpath", self.record_type)
            self.clickElement("xpath", self.record_type_passport)
            sleep(2)
        except Exception:
            print("Exception in select_record_type_passport method")
            self.takeScreenshot("select_record_type_passport")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to select record type passport
    """

    def select_record_type_student_id_card(self):
        try:
            self.element_Is_Visible("xpath", self.record_type)
            self.clickElement("xpath", self.record_type)
            self.clickElement("xpath", self.record_type_student_id_card)
            sleep(2)
        except Exception:
            print("Exception in select_record_type_student_id_card method")
            self.takeScreenshot("select_record_type_student_id_card")
            raise Exception

    """
         @author             : Somasekhar
         Description         : This method is used to select issuer type(texas) for driver license
    """

    def select_issuer_type_texas(self):
        try:
            self.element_Is_Visible("xpath", self.issuer_type)
            self.clickElement("xpath", self.issuer_type)
            self.clickElement("xpath", self.issuer_type_texas)
        except Exception:
            print("Exception in select issuer type texas for driver license method")
            self.takeScreenshot("select issuer type texas for driver license")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to select issuer type(alabama) for driver license
    """

    def select_issuer_type_alabama(self):
        try:
            self.element_Is_Visible("xpath", self.issuer_type)
            self.clickElement("xpath", self.issuer_type)
            self.clickElement("xpath", self.issuer_type_alabama)
        except Exception:
            print("Exception in select issuer type albama for driver license method")
            self.takeScreenshot("select issuer type albama for driver license")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to select issuer type(alaska) for driver license
    """

    def select_issuer_type_alaska(self):
        try:
            self.element_Is_Visible("xpath", self.issuer_type)
            self.clickElement("xpath", self.issuer_type)
            self.clickElement("xpath", self.issuer_type_alaska)
        except Exception:
            print("Exception in select issuer type alaska for driver license method")
            self.takeScreenshot("select issuer type alaska for driver license")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to select issuer type for employee
    """

    def select_issuer_for_employee(self):
        try:
            self.element_Is_Visible("xpath", self.issuer_type)
            self.clickElement("xpath", self.issuer_type)
            self.clickElement("xpath", self.issuer_type_employee_card)
        except Exception:
            print("Exception in select_issuer_for_employee method")
            self.takeScreenshot("select_issuer_for_employee")
            raise Exception

    """
         @author             : Somasekhar
         Description         : This method is used to select issuer type for student
    """

    def select_issuer_for_student(self):
        try:
            self.element_Is_Visible("xpath", self.issuer_type)
            self.clickElement("xpath", self.issuer_type)
            self.clickElement("xpath", self.issuer_type_student_card)
        except Exception:
            print("Exception in select_issuer_for_student method")
            self.takeScreenshot("select_issuer_for_student")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to select issuer type for student
    """

    def select_issuer_for_passport(self):
        try:
            self.element_Is_Visible("xpath", self.issuer_type)
            self.clickElement("xpath", self.issuer_type)
            self.clickElement("xpath", self.issuer_type_passport)
        except Exception:
            print("Exception in select_issuer_for_passport method")
            self.takeScreenshot("select_issuer_for_passport")
            raise Exception

    """
         @author             : Somasekhar
         Description         : This method is used to click to scan code under scan code records
    """

    def click_to_scan_code_button(self):
        try:
            scan_code = self.driver.find_element_by_xpath(self.scan_code_button)
            self.driver.execute_script("arguments[0].click();", scan_code)
        except Exception:
            print("Exception in scan button for records method")
            self.takeScreenshot("click scan button")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to scan a document 
    """

    def click_to_scan_button(self):
        try:
            scan = self.driver.find_element_by_xpath(self.scan)
            self.driver.execute_script("arguments[0].click();", scan)
            sleep(2)
            self.element_Is_Visible("xpath", self.click_scan)
            self.clickElement("xpath", self.click_scan)
            sleep(2)
            print("scan button clicked")
        except Exception:
            print("Exception in click_the_scan_code method")
            self.takeScreenshot("click_the_scan_code")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to search a record under link record
    """

    def click_search_records(self):
        try:
            search = self.driver.find_element_by_xpath(self.search_records)
            self.driver.execute_script("arguments[0].click();", search)
            print("Search records button clicked")
        except Exception:
            print("Exception in click search records method")
            self.takeScreenshot("click search records")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to confirm the record
    """

    def click_confirm(self):
        try:
            self.element_Is_Visible("xpath", self.confirm_btn)
            self.clickElement("xpath", self.confirm_btn)
            sleep(2)
            print("Confirm button clicked successfully")
        except Exception:
            print("Exception in click confirm method")
            self.takeScreenshot("Click confirm method")
            raise Exception

    """
        author             : Somasekhar
        Description         : This method is used to save button 
    """

    def click_save_button(self):
        try:
            save = self.driver.find_element_by_xpath(self.click_save)
            self.driver.execute_script("arguments[0].click();", save)
            sleep(2)
            print("Save button clicked successfully")
        except Exception:
            print("Exception in click save button method")
            self.takeScreenshot("Click save button method")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to save the record 
    """

    def click_save_record(self):
        try:
            save = self.driver.find_element_by_xpath(self.save_record_btn)
            self.driver.execute_script("arguments[0].click();", save)
            print("Clicked save record button")
            sleep(2)
        except Exception:
            print("Exception in click_save_record method")
            self.takeScreenshot("click_save_record")
            raise Exception

    """
       @author             : Somasekhar
       Description         : This method is used to click use existing record/document 
    """

    def click_use_existing_record(self):
        try:
            self.element_Is_Visible("xpath", self.use_existing_btn)
            self.clickElement("xpath", self.use_existing_btn)
            print("Use existing clicked successfully")
            sleep(1)

        except Exception:
            print("Exception in click use existing record method")
            self.takeScreenshot("click use existing record")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to upload a document for existing record
    """

    def upload_document(self, path):
        try:
            document = self.driver.find_element_by_xpath(self.use_existing_btn)
            self.driver.execute_script("arguments[0].click();", document)
            sleep(2)
            pyautogui.write(path)
            pyautogui.press('enter')
            print("uploaded existing record successfully")
        except Exception:
            print("Exception in click use existing record method")
            self.takeScreenshot("click use existing record")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used to click health tab under Records page
    """

    def click_health_tb(self):
        try:
            self.element_Is_Visible("xpath", self.health_record)
            self.clickElement("xpath", self.health_record)
            sleep(8)
            print("Health tab clicked successfully")
        except Exception:
            print("Exception in click health tab method")
            self.takeScreenshot("click health tab")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used to click id tab under Records page
    """

    def click_id_tb(self):
        try:
            self.element_Is_Visible("xpath", self.id_record)
            self.clickElement("xpath", self.id_record)
            sleep(8)
            print("ID tab clicked successfully")
        except Exception:
            print("Exception in click ID tab method")
            self.takeScreenshot("click ID tab")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to verify the covid pcr test record under records tab
    """

    def verify_covid_pcr_test(self):
        try:
            data = ReadData()
            test_data = data.get_test_data()
            self.element_Is_Visible("xpath", self.verify_record_type_covid_pcr_test)
            covid_pcr_test = self.driver.find_element_by_xpath(self.verify_record_type_covid_pcr_test).text
            print(covid_pcr_test)
            if covid_pcr_test == test_data["validation"]["covid pcr"] or test_data["validation"]["covid pcr1"]:
                assert True
                print("Verified Covid PCR Test record")
            else:
                assert False
        except Exception:
            print("Exception in verify covid pcr test method")
            self.takeScreenshot("verify covid pcr test record")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to verify the covid vaccination record under records tab
    """

    def verify_covid_vaccination(self):
        try:
            data = ReadData()
            test_data = data.get_test_data()
            self.element_Is_Visible("xpath", self.verify_record_type_covid_vaccination)
            covid_vaccination = self.driver.find_element_by_xpath(self.verify_record_type_covid_vaccination).text
            print(covid_vaccination)
            if covid_vaccination == test_data["validation"]["covid vaccination"] or test_data["validation"][
                "covid vaccination1"]:
                assert True
                print("Verified Covid Vaccination record")
            else:
                assert False
        except Exception:
            print("Exception in verify covid vaccination method")
            self.takeScreenshot("verify covid vaccination record")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to verify the covid 19 test antigen record under records tab
    """

    def verify_covid_19_test_antigen(self):
        try:
            data = ReadData()
            test_data = data.get_test_data()
            self.element_Is_Visible("xpath", self.verify_record_type_covid_19_antigen)
            verify = self.driver.find_element_by_xpath(self.verify_record_type_covid_19_antigen).text
            print(verify)
            if verify == test_data["validation"]["antigen inspire"] or test_data["validation"]["antigen inspire1"]:
                assert True
                print("Verified Covid 19 test antigen record")
            else:
                assert False
        except Exception:
            print("Exception in verify covid 19 test antigen method")
            self.takeScreenshot("verify covid 19 test antigen record")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to verify the immunization record under records tab
    """

    def verify_immunization(self):
        try:
            data = ReadData()
            test_data = data.get_test_data()
            self.element_Is_Visible("xpath", self.verify_record_type_immunization)
            verify = self.driver.find_element_by_xpath(self.verify_record_type_immunization).text
            print(verify)
            if verify == test_data["validation"]["health immunization"]:
                assert True
                print("Verified Immunization record")
            else:
                assert False
        except Exception:
            print("Exception in verify immunization method")
            self.takeScreenshot("verify immunization record")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to verify the covid 19 test antibody record under records tab
    """

    def verify_covid_19_test_antibody(self):
        try:
            data = ReadData()
            test_data = data.get_test_data()
            self.element_Is_Visible("xpath", self.verify_record_type_covid_19_antibody)
            verify = self.driver.find_element_by_xpath(self.verify_record_type_covid_19_antibody).text
            print(verify)
            if verify == test_data["validation"]["verify antibody"] or test_data["validation"]["verify antibody1"]:
                assert True
                print("Verified Covid 19 test antibody record")
            else:
                assert False
        except Exception:
            print("Exception in verify covid 19 test antibody method")
            self.takeScreenshot("verify covid 19 test antibody record")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to verify the covid 19 test antibody record under records tab
    """

    def verify_covid_19_rt_pcr(self):
        try:
            data = ReadData()
            test_data = data.get_test_data()
            self.element_Is_Visible("xpath", self.verify_record_type_covid_19_rt_pcr)
            verify = self.driver.find_element_by_xpath(self.verify_record_type_covid_19_rt_pcr).text
            print(verify)
            if verify == test_data["validation"]["verify rt pcr"] or test_data["validation"]["verify rt pcr1"]:
                assert True
                print("Verified Covid 19 RT-PCR test record")
            else:
                assert False
        except Exception:
            print("Exception in verify covid 19 rt-pcr test method")
            self.takeScreenshot("verify covid 19 rt-pcr test record")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to verify the passport record under ID records tab
    """

    def verify_passport_record(self):
        try:
            data = ReadData()
            test_data = data.get_test_data()
            self.element_Is_Visible("xpath", self.verify_record_type_passport)
            verify = self.driver.find_element_by_xpath(self.verify_record_type_passport).text
            print(verify)
            if verify == test_data["validation"]["verify passport"]:
                assert True
                print("Verified Passport record")
            else:
                assert False
        except Exception:
            print("Exception in verify passport record method")
            self.takeScreenshot("verify passport record record")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to verify the texas driver license record under ID records tab
    """

    def verify_texas_driver_license_record(self):
        try:
            data = ReadData()
            test_data = data.get_test_data()
            self.element_Is_Visible("xpath", self.verify_record_type_texas_driver_license)
            verify = self.driver.find_element_by_xpath(self.verify_record_type_texas_driver_license).text
            print(verify)
            if verify == test_data["validation"]["verify license"]:
                assert True
                print("Verified Texas Driver license record")
            else:
                assert False
        except Exception:
            print("Exception in verify texas driver license record method")
            self.takeScreenshot("verify texas driver license record")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to verify the alabama driver license record under ID records tab
    """

    def verify_alabama_driver_license_record(self):
        try:
            data = ReadData()
            test_data = data.get_test_data()
            self.element_Is_Visible("xpath", self.verify_record_type_alabama_driver_license)
            verify = self.driver.find_element_by_xpath(self.verify_record_type_alabama_driver_license).text
            print(verify)
            if verify == test_data["validation"]["alabama license"]:
                assert True
                print("Verified Alabama Driver license record")
            else:
                assert False
        except Exception:
            print("Exception in verify alabama driver license record method")
            self.takeScreenshot("verify alabama driver license record")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to verify the alaska driver license record under ID records tab
    """

    def verify_alaska_driver_license_record(self):
        try:
            data = ReadData()
            test_data = data.get_test_data()
            self.element_Is_Visible("xpath", self.verify_record_type_alaska_driver_license)
            verify = self.driver.find_element_by_xpath(self.verify_record_type_alaska_driver_license).text
            print(verify)
            if verify == test_data["validation"]["alaska license"]:
                assert True
                print("Verified Alaska Driver license record")
            else:
                assert False
        except Exception:
            print("Exception in verify alaska driver license record method")
            self.takeScreenshot("verify alaska driver license record")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to verify the student id card record under ID records tab
    """

    def verify_student_id_card_record(self):
        try:
            data = ReadData()
            test_data = data.get_test_data()
            self.element_Is_Visible("xpath", self.verify_record_type_student_id_card)
            verify = self.driver.find_element_by_xpath(self.verify_record_type_student_id_card).text
            print(verify)
            if verify == test_data["validation"]["student id card"]:
                assert True
                print("Verified Dallas Independent School District record")
            else:
                assert False
        except Exception:
            print("Exception in verify student id card record method")
            self.takeScreenshot("verify student id card record record")
            raise Exception

    """
        @author             : Sreenivas Reddy
        Description         : This method is used to click latest health record under records page
    """

    def select_health_record(self):
        try:
            self.element_Is_Visible("xpath", self.select_record)
            print("visible")
            a = self.driver.find_element_by_xpath(self.select_record)
            if a.is_displayed():
                action = ActionChains(self.driver)
                action.click(on_element=a)
                action.perform()
                print("Health record clicked successfully")
            else:
                print("Records not found")
        except Exception:
            print("Exception in clicking Health record method")
            self.takeScreenshot("clicking Health record")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to click to delete the record from U-Pass
    """

    def click_delete_from_u_pass(self):
        try:
            self.element_Is_Visible("xpath", self.delete_from_record)
            self.clickElement("xpath", self.delete_from_record)
            sleep(2)
            print("Clicked Delete from U-Pass button")
        except Exception:
            print("Exception in click Delete from U-Pass button method")
            self.takeScreenshot("click Delete from U-Pass button")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to selected record to delete from Health/ID tab under 'Records' page 
    """

    def click_delete_record(self):
        try:
            self.element_Is_Visible("xpath", self.delete_record)
            self.clickElement("xpath", self.delete_record)
            sleep(2)
            print("Record deleted successfully")
        except Exception:
            print("Exception in click delete record method")
            self.takeScreenshot("click delete record")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to verify the delete record message
    """

    def verify_delete_message(self):
        try:
            data = ReadData()
            test_data = data.get_test_data()
            self.element_Is_Visible("xpath", self.verify_delete_record)
            delete = self.driver.find_element_by_xpath(self.verify_delete_record).text
            print(delete)
            if delete == test_data["validation"]["cancel appointment"]:
                assert True
                print("Verified delete record message successfully")
            else:
                assert False
        except Exception:
            print("Exception in verify delete message method")
            self.takeScreenshot("verify delete message")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used to select the dropdown on top of record page
    """

    def click_drop_down_from_records(self):
        try:
            self.element_Is_Visible("xpath", self.click_dependent)
            self.clickElement("xpath", self.click_dependent)
            print("Clicked drop down on top of records page")
        except Exception:
            print("Exception in click dropdown on top of records page method")
            self.takeScreenshot("click dropdown from records")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used to select the dependent from dropdown of records page
    """

    def select_the_dependent(self):
        try:
            self.element_Is_Visible("xpath", self.first_dependent)
            self.clickElement("xpath", self.first_dependent)
        except Exception:
            print("Exception in select the dependent method")
            self.takeScreenshot("select the dependent")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used to select the dependent holder name(Scan document/Scan code/link record)
    """

    def select_dependent_holder_name(self):
        try:
            self.element_Is_Visible("xpath", self.name_tb)
            self.clickElement("xpath", self.name_tb)
            self.clickElement("xpath", self.select_dependent)
            print("Dependent Name is selected")
        except Exception:
            print("Exception in Selecting Dependent Holder Name Method")
            self.takeScreenshot("Selecting Dependent Holder Name Method")
            raise Exception
