from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from utils.browser_config import driver


class Web_Driver_Utils:

    def element_is_visible(self, xpath):
        wait = WebDriverWait(driver, 60)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

    def element_is_present(self, xpath):
        wait = WebDriverWait(driver, 60)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))

    def text_present_in_element(self, xpath, visible_text):
        wait = WebDriverWait(driver, 60)
        wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, xpath), visible_text))

    def element_to_be_clickable(self, xpath):
        wait = WebDriverWait(driver, 60)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))

