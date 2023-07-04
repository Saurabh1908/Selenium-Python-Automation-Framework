from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class dashboard():
    def __init__(self, driver):
        self.driver = driver
        self.text_present_xpath = "//p[@class='oxd-userdropdown-name']"
        self.button_admin_xpath  = "//a[@class='oxd-main-menu-item active']"
        self.button_job_xpath  = "//a[@class='oxd-brand']"
        self.button_employment_status_xpath= "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[1]/a[1]"

    def Text_Present(self):
        return self.driver.find_element(By.XPATH, self.text_present_xpath).text

    def hover_Admin(self):
        return self.driver.find_element(By.XPATH, self.button_admin_xpath)

    def hover_Job(self):
        return self.driver.find_element(By.XPATH, self.button_job_xpath)

    def click_Employment_Status(self):
        return self.driver.find_element(By.XPATH, self.button_employment_status_xpath)




