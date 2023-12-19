import time
import random
import imaplib
import email
import logging
from time import sleep

import pyautogui

from utils.browser_config import driver
from POM.Locators.locators import ManagerAppElements
from utils.read_data import ReadData
from selenium.webdriver.common.keys import Keys
from POM.BaseTest.selenium_driver import SeleniumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from POM.BaseTest.screenshot import Screenshot
LOGGER = logging.getLogger(__name__)


class ManagerPortal(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    screenshot = Screenshot(driver)

    continue_btn = ManagerAppElements.continue_btn
    continue_btn_2 = ManagerAppElements.continue_btn_2
    continue_btn_3 = ManagerAppElements.continue_btn
    get_started_btn = ManagerAppElements.get_started_btn
    create_new_login_btn = ManagerAppElements.create_new_login_btn
    full_name = ManagerAppElements.full_name
    enter_email = ManagerAppElements.enter_email
    birthdate = ManagerAppElements.birthdate
    phone_number = ManagerAppElements.phone_number
    password = ManagerAppElements.password
    confirm_password = ManagerAppElements.confirm_password
    verify_authentication_page = ManagerAppElements.verify_authentication_page
    go_to_upass_btn = ManagerAppElements.go_to_upass_btn
    menu_button = ManagerAppElements.menu_button
    my_profile = ManagerAppElements.my_profile
    verify_new_account = ManagerAppElements.verify_new_account
    program_page = ManagerAppElements.program_page
    select_program_drop_down = ManagerAppElements.select_program_drop_down
    select_program_shs = ManagerAppElements.select_program_shs
    verify_programs = ManagerAppElements.verify_programs
    existing_account = ManagerAppElements.existing_account
    username_tb = ManagerAppElements.username_tb
    password_tb = ManagerAppElements.password_tb
    sign_in_btn = ManagerAppElements.sign_in_btn
    available_programs_active = ManagerAppElements.available_programs_active
    available_programs_inactive = ManagerAppElements.available_programs_inactive
    available_programs_draft = ManagerAppElements.available_programs_draft
    active_tb = ManagerAppElements.active_tb
    in_active_tb = ManagerAppElements.in_active_tb
    draft_tb = ManagerAppElements.draft_tb
    select_program_shs_student = ManagerAppElements.select_program_shs_student
    select_program_shs_Athletics = ManagerAppElements.select_program_shs_Athletics
    select_program_shs_Employees = ManagerAppElements.select_program_shs_Employees
    status_active = ManagerAppElements.status_active
    new_button = ManagerAppElements.new_button
    program_name = ManagerAppElements.program_name
    save_draft = ManagerAppElements.save_draft
    verify_program_message = ManagerAppElements.verify_program_message
    verify_new_program = ManagerAppElements.verify_program

    program_employees = ManagerAppElements.program_employees
    scan_verify = ManagerAppElements.scan_verify
    use_id = ManagerAppElements.use_id
    upass_id_number = ManagerAppElements.upass_id_number
    verify_id = ManagerAppElements.verify_id
    upass_verification_waiting = ManagerAppElements.upass_verification_waiting
    upass_result = ManagerAppElements.result
    verify_result = ManagerAppElements.verify_result
    bell_icon = ManagerAppElements.bell_icon
    see_request = ManagerAppElements.see_request
    approve_once = ManagerAppElements.approve_once
    does_not_pass = ManagerAppElements.does_not_pass
    program_settings = ManagerAppElements.program_settings
    edit_button = ManagerAppElements.edit_button
    select_status_program_setting = ManagerAppElements.select_status_program_setting
    select_status_directory = ManagerAppElements.select_status_directory
    select_status_active = ManagerAppElements.select_status_active
    select_status_inactive = ManagerAppElements.select_status_inactive
    save_button = ManagerAppElements.save_button
    back_button_program_settings = ManagerAppElements.back_button_program_settings
    back_button_directory_page_settings = ManagerAppElements.back_button_directory_page_settings
    directory_page_settings = ManagerAppElements.directory_page_settings
    select_status_unpublished = ManagerAppElements.select_status_unpublished
    select_status_published = ManagerAppElements.select_status_published

    verify_program_update_message = ManagerAppElements.verify_program_update_message
    program_back_button = ManagerAppElements.program_back_button
    program_name_tb = ManagerAppElements.program_name_tb
    description_tb = ManagerAppElements.description_tb
    program_shs_250 = ManagerAppElements.program_shs_250
    directory_page_message = ManagerAppElements.verify_directory_page_message

    swipe_program_card = ManagerAppElements.swipe_program
    delete_program = ManagerAppElements.delete_btn
    delete_bt = ManagerAppElements.delete_bt
    activate_program_card = ManagerAppElements.activate_btn
    deactivate_program_card = ManagerAppElements.deactivate_btn
    program_card = ManagerAppElements.program_card

    data = ReadData()
    test_data = data.get_test_data()
    """
        @author : Sreenivas Reddy
        Description: This method used to launch U-Pass login page
    """

    def upass_portal_page(self):
        try:
            title = driver.title
            assert 'UPass Manager' in title
            print("Title of the page:", title)
            self.element_Is_Visible("xpath", self.continue_btn)
            self.element_clickable("xpath", self.continue_btn)
            self.clickElement("xpath", self.continue_btn)

            self.element_Is_Visible("xpath", self.continue_btn_2)
            self.element_clickable("xpath", self.continue_btn_2)
            self.clickElement("xpath", self.continue_btn_2)

            self.element_Is_Visible("xpath", self.get_started_btn)
            self.element_clickable("xpath", self.get_started_btn)
            self.clickElement("xpath", self.get_started_btn)

        except Exception:
            print("Exception in U-pass portal page")
            self.screenshot.attach_screenshot_to_allure_report("U-pass portal page")
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
            # print('Title of the page is not matched')
            print("Exception in clicking Create New login Button")
            self.screenshot.attach_screenshot_to_allure_report("Clicking Create New login Button")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Enter Fullname
    """

    def enter_full_legal_name(self):
        try:
            data = ReadData()
            test_data = data.get_test_data()
            title = driver.title
            assert 'Create Account' in title
            print("Title of the page:", title)
            self.element_Is_Visible("xpath", self.full_name)
            full_name = driver.find_element_by_xpath(self.full_name)
            full_name.send_keys(test_data["details"]["name"])
            time.sleep(2)
            fullname = full_name.get_attribute('value')
            sleep(1)
            print("Full Legal Name is entered :", fullname)
            return fullname
        except Exception:
            print("Exception in Entering Full Legal Name")
            self.screenshot.attach_screenshot_to_allure_report("Entering Full Legal Name")
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
            enter_email = driver.find_element_by_xpath(self.enter_email)
            enter_email.send_keys("sreenivasreddyunisys+" + str(random.randint(99999, 1000000)) + "@gmail.com")
            time.sleep(2)
            email_entered = enter_email.get_attribute('value')
            print("Entered email id is:", email_entered)
            return email_entered
        except Exception:
            print("Exception in entering email ")
            self.screenshot.attach_screenshot_to_allure_report("Enter Email")
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
            print("Date of Birth  is entered")
        except Exception:
            print("Exception in Entering Date of Birth")
            self.screenshot.attach_screenshot_to_allure_report("Entering Date of Birth")
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
            print("Phone Number  is entered")
        except Exception:
            print("Exception in Entering Phone Number")
            self.screenshot.attach_screenshot_to_allure_report("Entering Phone Number")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Enter Password
    """

    def enter_password(self, password):
        try:
            driver.find_element_by_xpath(self.confirm_password).send_keys(Keys.END)
            self.element_Is_Visible("xpath", self.password)
            self.clickElement("xpath", self.password)
            self.enterText("xpath", self.password, password)
            sleep(1)
            print("Password  is entered")
        except Exception:
            print("Exception in Entering Password")
            self.screenshot.attach_screenshot_to_allure_report("Entering Password")
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
            print("Exception in Entering Confirm Password")
            self.screenshot.attach_screenshot_to_allure_report("Entering Confirm Password")
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
                                # print(body)
                                import re
                                a = (re.search("(?P<url>https?://[^\\s]+)", body).group("url"))
                                b = a.partition('http://www.w3.org/1999/xhtml"')
                                c = (b[0])
                                link.append(c)
                                new_otp = st.join(link)
                                # print(link)
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
            sleep(5)
            d = self.verify_email_upass()
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(d)
            sleep(2)
            driver.switch_to.window(driver.window_handles[0])
            print("Email is Verified Successfully")
            self.element_Is_Visible("xpath", self.verify_authentication_page)
            self.element_Is_Visible("xpath", self.continue_btn_3)
            self.clickElement("xpath", self.continue_btn_3)
            sleep(1)
            print("Continue button is clicked")
        except Exception:
            print("Exception in Clicking Continue button")
            self.screenshot.attach_screenshot_to_allure_report("Clicking Continue button")
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
            print("Continue button is clicked")
        except Exception:
            print("Exception in Clicking Continue button")
            self.screenshot.attach_screenshot_to_allure_report("Clicking Continue button")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Click Go To Upass Button
    """

    def click_go_to_upass(self):
        try:
            self.element_Is_Visible("xpath", self.go_to_upass_btn)
            self.clickElement("xpath", self.go_to_upass_btn)
            print("Go To Upass button is clicked")
            self.data.write_data_into_excel(2, 2, email_entered)
            sleep(2)
        except Exception:
            print("Exception in Clicking Go To Upass button")
            self.screenshot.attach_screenshot_to_allure_report("Clicking Go To Upass button")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to verify created account
    """
    def verify_created_account(self):
        try:
            self.element_Is_Visible("xpath", self.program_page)
            actual = driver.find_element_by_xpath(self.program_page).text
            expected = "Programs"
            if actual == expected:
                assert True
                print("New User Account is Successfully created")
        except Exception:
            print("Exception in Clicking Verifying Account")
            self.screenshot.attach_screenshot_to_allure_report("Verifying Account")
            raise Exception

    """
            @author             : Sreenivas reddy
            Description         : This method is used to login to an existing account
    """

    def click_existing_account(self):
        try:
            login = driver.find_element_by_xpath(self.existing_account)
            driver.execute_script("arguments[0].click();", login)
            handles = driver.window_handles
            for handle in handles:
                driver.switch_to.window(handle)
        except Exception:
            self.screenshot.attach_screenshot_to_allure_report("Clicking existing account button")
            raise Exception

    """
    @author             : Somasekhar
    Description         : This method is used to enter username
    """

    def enter_username(self, username):
        try:
            wait = WebDriverWait(driver, 30)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.username_tb)))
            wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.username_tb)))
            driver.find_element_by_xpath(self.username_tb).send_keys(username)
            print("Username is Entered")
        except Exception:
            print("Exception in enter username method")
            self.screenshot.attach_screenshot_to_allure_report("enter user name in login page")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to enter password
    """

    def enter_login_password(self, password):
        try:
            wait = WebDriverWait(driver, 30)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.password_tb)))
            wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.password_tb)))
            driver.find_element_by_xpath(self.password_tb).send_keys(password)
            print("Password is entered")
        except Exception:
            print("Exception in enter password method")
            self.screenshot.attach_screenshot_to_allure_report("enter password in login page")
            raise Exception

    """
        @author             : Somasekhar
        Description         : This method is used to sign in to U-Pass holder application
    """

    def click_signin(self):
        try:
            self.element_Is_Visible("xpath", self.sign_in_btn)
            self.clickElement("xpath", self.sign_in_btn)
            time.sleep(5)
            handles = driver.window_handles
            for handle in handles:
                driver.switch_to.window(handle)
            print("Signin button is clicked")
        except Exception:
            print("Exception in click signin method")
            self.screenshot.attach_screenshot_to_allure_report("click sign in")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Click Menu Button
    """

    def click_menu_button(self):
        try:
            self.element_Is_Visible("xpath", self.menu_button)
            self.clickElement("xpath", self.menu_button)
            sleep(2)
            print("Menu button is clicked")
        except Exception:
            print("Exception in Clicking Menu button")
            self.screenshot.attach_screenshot_to_allure_report("Clicking Menu button")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Select Program drop down under My Organizations
    """

    def select_program_dropdown_btn(self):
        try:
            self.element_Is_Visible("xpath", self.select_program_drop_down)
            self.clickElement("xpath", self.select_program_drop_down)
            sleep(2)
            print("Menu button is clicked")
        except Exception:
            print("Exception in Clicking Program Dropdown button")
            self.screenshot.attach_screenshot_to_allure_report("Clicking Program Dropdown button")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Select Program SHS under My Organizations
    """

    def click_program_shs(self):
        try:
            self.element_Is_Visible("xpath", self.select_program_shs)
            self.clickElement("xpath", self.select_program_shs)
            sleep(2)
            print("SHS program is selected")
        except Exception:
            print("Exception in selecting SHS program")
            self.screenshot.attach_screenshot_to_allure_report("selecting SHS program")
            raise Exception

    """
            @author : Sreenivas Reddy
            Description: This method used to Verify Available  programs
    """

    def verify_view_programs(self):
        try:
            self.element_Is_Visible("xpath", self.verify_programs)
            sleep(5)
            self.clickElement("xpath", self.active_tb)
            # self.clickElement("xpath", self.active_tb)
            active_programs = driver.find_elements_by_xpath(self.available_programs_active)
            for program in active_programs:
                View_programs = program.text
                print("Available programs in Active tab are :" + View_programs)
            self.clickElement("xpath", self.in_active_tb)
            sleep(5)
            inactive_programs = driver.find_elements_by_xpath(self.available_programs_inactive)
            for program in inactive_programs:
                View_programs1 = program.text
                print("Available programs Inactive tab are :" + View_programs1)
            self.clickElement("xpath", self.draft_tb)
            sleep(5)
            draft_programs = driver.find_elements_by_xpath(self.available_programs_draft)
            for program in draft_programs:
                View_programs2 = program.text
                print("Available programs in Draft tab are :" + View_programs2)
        except Exception:
            print("Exception in verifying Available Programs")
            self.screenshot.attach_screenshot_to_allure_report("verifying Available Programs")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Select program SHS-Student under Active Programs
    """

    def select_active_program_student(self):
        try:
            self.element_Is_Visible("xpath", self.select_program_shs_student)
            self.clickElement("xpath", self.select_program_shs_student)
            print("Selected Program is SHS-Student")
        except Exception:
            print("Exception in Selecting Programs under Active Tab")
            self.screenshot.attach_screenshot_to_allure_report("Selecting Programs under Active Tab")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Select program SHS-Student under Active Programs
    """

    def verify_status_of_program_active(self):
        try:
            self.element_Is_Visible("xpath", self.status_active)
            status = driver.find_element_by_xpath(self.status_active)
            status_prgm = status.text
            print(status_prgm)
            assert status_prgm == 'Active'
        except Exception:
            print("Exception in Verifying Status of Program")
            self.screenshot.attach_screenshot_to_allure_report("Verifying Status of Program")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Click New Button to Create Program
    """
    def click_new_button(self):
        try:
            self.element_Is_Visible("xpath", self.new_button)
            self.clickElement("xpath", self.new_button)
            print("New Button is Clicked")
        except Exception:
            print("Exception in Clicking New Button Method ")
            self.screenshot.attach_screenshot_to_allure_report("Clicking New Button Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Enter Program Name
    """

    def enter_new_program_name(self,name):
        try:
            self.element_Is_Visible("xpath", self.program_name)
            self.clickElement("xpath", self.program_name)
            sleep(1)
            self.enterText("xpath", self.program_name,name)

            print("Program Name is Entered")
        except Exception:
            print("Exception in Entering Program Name Method ")
            self.screenshot.attach_screenshot_to_allure_report("Entering Program Name Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Click Save Draft Button
    """
    def click_save_draft_button(self):
        try:

            self.element_Is_Visible("xpath", self.save_draft)
            self.clickElement("xpath", self.save_draft)
            print("Save Draft Button is Clicked")
            self.element_Is_Visible("xpath", self.verify_program_message)
        except Exception:
            print("Exception in Clicking Save Draft Button Method ")
            self.screenshot.attach_screenshot_to_allure_report("Clicking Save Draft Button Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Verify Weather Program is Created or Not
    """

    def verify_created_program(self):
        try:
            self.element_Is_Visible("xpath", self.verify_program_message)
            actual = driver.find_element_by_xpath(self.verify_program_message).text
            expected = "Program has been created as a draft! Activate to publish program!"
            if actual == expected:
                assert True
                print("Program has been created")
        except Exception:
            print("Exception in Verifying Program Method ")
            self.screenshot.attach_screenshot_to_allure_report("Verifying Program Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Click SHS-Employee Program
    """
    def click_program_employees(self):
        try:
            self.element_Is_Visible("xpath", self.program_employees)
            self.clickElement("xpath", self.program_employees)
            print("Program Employee is Selected")
        except Exception:
            print("Exception in Selecting Employee program Method ")
            self.screenshot.attach_screenshot_to_allure_report("Selecting Employee program Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Make Program Status Active under Program Settings
    """
    def click_program_settings(self):
        try:
            self.element_Is_Visible("xpath", self.program_settings)
            self.clickElement("xpath", self.program_settings)
            print("Program settings button is clicked successfully")
        except Exception:
            print("Exception in Clicking Program Settings Method ")
            self.screenshot.attach_screenshot_to_allure_report("Clicking Program Settings Method")
            raise Exception

    # """
    #     @author : Sreenivas Reddy
    #     Description: This method used to Make Program Status Inactive under Program Settings
    # """
    #
    # def select_program_status_inactive(self):
    #     try:
    #         self.element_Is_Visible("xpath", self.program_settings)
    #         self.clickElement("xpath", self.program_settings)
    #
    #         self.element_Is_Visible("xpath", self.edit_button)
    #         self.clickElement("xpath", self.edit_button)
    #         print("Edit button is clicked")
    #
    #         self.element_Is_Visible("xpath", self.select_status_program_setting)
    #         self.clickElement("xpath", self.select_status_program_setting)
    #
    #         self.element_Is_Visible("xpath", self.select_status_inactive)
    #         self.clickElement("xpath", self.select_status_inactive)
    #         print("Program Status Inactive is Selected")
    #     except Exception:
    #         print("Exception in Selecting Program Status Inactive Method ")
    #         self.screenshot.attach_screenshot_to_allure_report("Selecting Program Status Inactive Method")
    #         raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Click Save Button 
    """

    def click_save_button(self):
        try:
            self.element_Is_Visible("xpath", self.save_button)
            element = self.getElement(self.save_button, "xpath")
            driver.execute_script("arguments[0].click();", element)
            print("Save button is clicked")
        except Exception:
            print("Exception in Clicking Save Button Method ")
            self.screenshot.attach_screenshot_to_allure_report("Clicking Save Button Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Click Back Button 
    """

    def click_back_button_program_settings(self):
        try:
            self.element_Is_Visible("xpath", self.back_button_program_settings)
            self.clickElement("xpath", self.back_button_program_settings)
            print("Back button is clicked")
        except Exception:
            print("Exception in Clicking Back Button Method ")
            self.screenshot.attach_screenshot_to_allure_report("Clicking Back Button Method")
            raise Exception

    """
         @author : Sreenivas Reddy
        Description: This method used to Click Back Button 
    """

    def click_back_button_directory_page_settings(self):
        try:
            self.element_Is_Visible("xpath", self.back_button_directory_page_settings)
            self.clickElement("xpath", self.back_button_directory_page_settings)
            print("Back button is clicked")
        except Exception:
            print("Exception in Clicking Back Button Method ")
            self.screenshot.attach_screenshot_to_allure_report("Clicking Back Button Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Make Program Published under Directory Page Settings
    """

    def select_program_published(self):
        try:
            self.element_Is_Visible("xpath", self.select_status_directory)
            self.clickElement("xpath", self.select_status_directory)

            self.element_Is_Visible("xpath", self.select_status_published)
            self.clickElement("xpath", self.select_status_published)
            print("Program Status Published is Selected")
        except Exception:
            print("Exception in Selecting Program Status Published Method ")
            self.screenshot.attach_screenshot_to_allure_report("Selecting Program Status Published Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Make Program Unpublished under Directory Page Settings
    """

    def select_program_unpublished(self):
        try:
            self.element_Is_Visible("xpath", self.select_status_directory)
            self.clickElement("xpath", self.select_status_directory)

            self.element_Is_Visible("xpath", self.select_status_unpublished)
            self.clickElement("xpath", self.select_status_unpublished)
            print("Program Status Published is Selected")
        except Exception:
            print("Exception in Selecting Program Status Unpublished Method ")
            self.screenshot.attach_screenshot_to_allure_report("Selecting Program Status Unpublished Method")
            raise Exception
    """
        @author : Sreenivas Reddy
        Description: This method used to Click Scan/Verify
    """
    def click_scan_verify_button(self):
        try:
            self.element_Is_Visible("xpath", self.scan_verify)
            element = self.getElement(self.scan_verify, "xpath")
            driver.execute_script("arguments[0].click();", element)
            # self.clickElement("xpath", self.scan_verify)
            print("Scan/Verify Button is Clicked")
        except Exception:
            print("Exception in Clicking Scan/Verify Button Method ")
            self.screenshot.attach_screenshot_to_allure_report("Clicking Scan/Verify Button Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Click Scan/Verify
    """

    def click_switch_upass_holder(self):
        try:
            d = "https://upassuat.unisys.com"
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(d)
            sleep(2)
            self.element_Is_Visible("xpath", self.continue_btn)
            # driver.switch_to.window(driver.window_handles[0])
        except Exception:
            print("Exception in Clicking Scan/Verify Button Method ")
            self.screenshot.attach_screenshot_to_allure_report("Clicking Scan/Verify Button Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Click Use Id NUmber Instead of Scan 
    """

    def click_use_id_number(self):
        try:
            sleep(2)
            driver.switch_to.window(driver.window_handles[0])
            self.element_Is_Visible("xpath", self.use_id)
            element = self.getElement(self.use_id, "xpath")
            driver.execute_script("arguments[0].click();", element)
            print("Use Id NUmber Instead Button is Clicked")
            # self.clickElement("xpath", self.use_id)
        except Exception:
            print("Exception in Clicking Use Id NUmber Instead Button Method")
            self.screenshot.attach_screenshot_to_allure_report("Clicking Use Id NUmber Instead Button Method")
            raise Exception
    """
        @author : Sreenivas Reddy
        Description: This method used to Enter Id Number
    """
    def enter_id_number(self,text):
        try:
            self.element_Is_Visible("xpath", self.upass_id_number)
            sleep(2)
            self.enterText("xpath", self.upass_id_number,text)
            print("Id Number is entered")
        except Exception:
            print("Exception in Entering Id Number Method ")
            self.screenshot.attach_screenshot_to_allure_report("Entering Id Number Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Click Verify Button
    """
    def click_verify_button(self):
        try:
            self.element_Is_Visible("xpath", self.verify_id)
            self.clickElement("xpath", self.verify_id)
            print("Verify Button is clicked")
            self.element_Is_Visible("xpath", self.upass_verification_waiting)
            sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            sleep(2)
        except Exception:
            print("Exception in Clicking Verify Button Method ")
            self.screenshot.attach_screenshot_to_allure_report("Clicking Verify Button Method")
            raise Exception

    """
        @author : Sreenivas Reddy
        Description: This method used to Verify the result Pass or Not Pass
    """
    def verify_upass_result(self):
        try:
            sleep(2)
            driver.switch_to.window(driver.window_handles[0])
            sleep(2)
            self.element_Is_Visible("xpath", self.verify_result)
            self.element_Is_Visible("xpath", self.upass_result)
            result = driver.find_element_by_xpath(self.upass_result).text
            print(result)
            if result == "Pass":
                assert True
                print("Record Passed")
            elif result == "Does Not Pass":
                assert True
                print("Record does not pass")
            else:
                assert False
            sleep(5)
        except Exception:
            print("Exception in Clicking Verify Button Method")
            self.screenshot.attach_screenshot_to_allure_report("Clicking Verify Button Method")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used to click the edit button
    """
    def click_edit_button(self):
        try:
            self.element_Is_Visible("xpath", self.edit_button)
            self.clickElement("xpath", self.edit_button)
            print("Edit button is clicked")
        except Exception:
            print("Exception in Clicking Edit Method")
            self.screenshot.attach_screenshot_to_allure_report("Clicking Edit button Method")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used to select the program status is Active
    """
    def select_the_program_status_active(self):
        try:
            self.element_Is_Visible("xpath", self.select_status_program_setting)
            self.clickElement("xpath", self.select_status_program_setting)

            self.element_Is_Visible("xpath", self.select_status_active)
            self.clickElement("xpath", self.select_status_active)
            print("Program Status Active is Selected")
        except Exception:
            print("Exception in Selecting Program Status Active Method ")
            self.screenshot.attach_screenshot_to_allure_report("Selecting Program Status Active Method")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used to verify the program update message
    """
    def verify_the_program_update(self):
        try:
            self.element_Is_Visible("xpath", self.verify_program_update_message)
            actual = driver.find_element_by_xpath(self.verify_program_update_message).text
            print(actual)
            expected = "Your program has been updated!"
            if actual == expected:
                assert True
            else:
                assert False
        except Exception:
            print("Exception in Verify the program update method")
            self.screenshot.attach_screenshot_to_allure_report("Verify the program update")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used to go back to active/inactive/drafts tab
    """
    def click_cross_mark(self):
        try:
            self.element_Is_Visible("xpath", self.program_back_button)
            self.clickElement("xpath", self.program_back_button)
            print("Cross mark clicked successfully")
        except Exception:
            print("Exception in Clicking cross mark/back method")
            self.screenshot.attach_screenshot_to_allure_report("Click cross mark/back")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used verify the active programs under active tab
    """
    def verify_active_programs(self):
        try:
            self.element_Is_Visible("xpath", self.verify_programs)
            sleep(5)
            self.clickElement("xpath", self.active_tb)
            active_programs = driver.find_elements_by_xpath(self.available_programs_active)
            for program in active_programs:
                view_programs = program.text
                print("Available programs in Active tab are :" + view_programs)
        except Exception:
            print("Exception in Verify Active programs under Active tab")
            self.screenshot.attach_screenshot_to_allure_report("Verify active programs")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used verify the inactive programs under inactive tab
    """
    def verify_inactive_programs(self):
        try:
            self.clickElement("xpath", self.in_active_tb)
            sleep(5)
            inactive_programs = driver.find_elements_by_xpath(self.available_programs_inactive)
            for program in inactive_programs:
                view_programs = program.text
                print("Available programs Inactive tab are :" + view_programs)
        except Exception:
            print("Exception in Verify InActive programs under InActive tab")
            self.screenshot.attach_screenshot_to_allure_report("Verify inactive programs")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used verify the inactive programs under inactive tab
    """
    def verify_drafts_programs(self):
        try:
            self.clickElement("xpath", self.draft_tb)
            sleep(5)
            draft_programs = driver.find_elements_by_xpath(self.available_programs_draft)
            for program in draft_programs:
                view_programs = program.text
                print("Available programs in Draft tab are :" + view_programs)
        except Exception:
            print("Exception in Verify drafts programs under Drafts tab")
            self.screenshot.attach_screenshot_to_allure_report("Verify drafts programs")
            raise Exception
    """
        @author     : Somasekhar
        Description : This method is used to select the program status is inactive
    """
    def select_the_program_status_inactive(self):
        try:
            self.element_Is_Visible("xpath", self.select_status_program_setting)
            self.clickElement("xpath", self.select_status_program_setting)

            self.element_Is_Visible("xpath", self.select_status_inactive)
            self.clickElement("xpath", self.select_status_inactive)
            print("Program Status Inactive is Selected")
        except Exception:
            print("Exception in Selecting Program Status Inactive Method ")
            self.screenshot.attach_screenshot_to_allure_report("Selecting Program Status Inactive Method")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used to click the directory page settings of a program
    """
    def click_directory_page_settings(self):
        try:
            self.element_Is_Visible("xpath", self.directory_page_settings)
            self.clickElement("xpath", self.directory_page_settings)
            print("Directory page settings clicked successfully")
        except Exception:
            print("Exception in Clicking directory page settings method")
            self.screenshot.attach_screenshot_to_allure_report("click directory page settings")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used to change the program name for existing program
    """
    def change_the_program_name(self, name):
        try:
            self.element_Is_Visible("xpath", self.program_name_tb)
            self.clickElement("xpath", self.program_name_tb)
            driver.find_element_by_xpath(self.program_name_tb).send_keys(Keys.CONTROL + "a", Keys.DELETE)
            sleep(2)
            self.enterText("xpath", self.program_name_tb, name)
            print("Changed the program name successfully")
        except Exception:
            print("Exception in Change the program name method")
            self.screenshot.attach_screenshot_to_allure_report("change the program name")
            raise Exception
    """
        @author     : Somasekhar
        Description : This method is used to enter the description in existing program
    """
    def enter_description(self, description):
        try:
            self.element_Is_Visible("xpath", self.description_tb)
            self.clickElement("xpath", self.description_tb)
            driver.find_element_by_xpath(self.description_tb).send_keys(Keys.CONTROL + "a", Keys.DELETE)
            sleep(2)
            self.enterText("xpath", self.description_tb, description)
            pyautogui.press('Enter')
            print("Description is entered successfully")
        except Exception:
            print("Exception in Enter description method")
            self.screenshot.attach_screenshot_to_allure_report("Enter description")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used to select the active program(SHS_250)
    """
    def select_active_program_shs_250(self):
        try:
            program = driver.find_element_by_xpath(self.program_shs_250)
            driver.execute_script("arguments[0].click();", program)
            print("Program selected")
        except Exception:
            print("Exception in Select active program shs_250 method")
            self.screenshot.attach_screenshot_to_allure_report("select active program shs_250")
            raise Exception

    """
        @author     : Somasekhar
        Description : This method is used to 
    """
    def verify_directory_page_message(self):
        try:
            self.element_Is_Visible("xpath", self.directory_page_message)
            actual = driver.find_element_by_xpath(self.directory_page_message).text
            print(actual)
            expected = "Changes saved successfully."
            if actual == expected:
                assert True
            else:
                assert False
        except Exception:
            print("Exception in Verify directory page message method")
            self.screenshot.attach_screenshot_to_allure_report("verify directory page message")
            raise Exception

    # def swipe_program(self):
    #     try:
    #         self.element_Is_Visible("xpath", self.swipe_program_card)
    #         source = driver.find_element_by_xpath(self.swipe_program_card)
