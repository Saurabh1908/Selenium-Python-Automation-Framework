import pytest
from selenium.webdriver.common.by import By
import time
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import dashboard
from Utilities.logger import logClass
from Utility_Script.excel_methods import ExcelMethods
sheet_name = 'test_Login'
import configparser
# config = configparser.ConfigParser()
# config.read("C:\\Users\\Admin\\PycharmProjects\\Selenium_Python_Framework\\Utilities\\input.properties")

@pytest.mark.usefixtures("setUp")
class Testlogin(logClass):

    @pytest.mark.parametrize("sr_no,username,password,condition",ExcelMethods('test_Login').get_parameters())
    def test_001(self,sr_no,username,password,condition):
        log=self.getThe_logs()
        log.info("TEST CASE 001")
        log.info("Test Case Start")
        lg = Login(self.driver)
        db = dashboard(self.driver)

        # lg.input_username(config.get("Credential","correct_username"))
        lg.input_username(username)
        log.info("Enter the Username")

        time.sleep(3)
        # lg.input_userpassword(config.get("Credential","correct_password"))
        lg.input_userpassword(password)
        time.sleep(3)
        log.info("Enter the Password")
        lg.click_login()
        log.info("Click the Login Button")
        time.sleep(3)
        if condition =="positive condition":
            if "Paul" in db.Text_Present():
                status = True
                log.info("Test Case Pass")
            else:
                # self.driver.save_screenshot("C:\\Users\Admin\\PycharmProjects\\Selenium_Python_Framework\\Screenshot\\test_Login_001.png")
                log.critical("Test Case Fail")
                status = False
        elif condition == "negative condition":
            if "Invalid credentials" in lg.Invalid_msg():
                status = True
                log.info("Test Case Pass")
            else:
                log.info("Test Case Fail")
                status = False
        ExcelMethods(sheet_name).update_result_in_excel(sr_no,status)
        assert status


    # def test_002(self):
    #     log = self.getThe_logs()
    #     log.info("TEST CASE 002")
    #     log.info("Test Case Start")
    #     lg=Login(self.driver)
    #
    #     lg.input_username(config.get("Credential","incorrect_username"))
    #     log.info("Enter the Username")
    #     time.sleep(3)
    #     lg.input_userpassword(config.get("Credential","correct_password"))
    #     log.info("Enter the Username")
    #     time.sleep(3)
    #     lg.click_login()
    #     log.info("Click the Login Button")
    #     time.sleep(3)
    #     if "Invalid credentials" in lg.Invalid_msg():
    #         assert True
    #         log.info("Test Case Pass")
    #     else:
    #         log.info("Test Case Fail")
    #         assert False
    #
    #
    # def test_003(self):
    #     log = self.getThe_logs()
    #     log.info("TEST CASE 003")
    #     log.info("Test Case Start")
    #     lg=Login(self.driver)
    #     lg.input_username(config.get("Credential","correct_username"))
    #     log.info("Enter the Username")
    #     time.sleep(3)
    #     lg.input_userpassword(config.get("Credential","incorrect_password"))
    #     log.info("Enter the Password")
    #     time.sleep(3)
    #     lg.click_login()
    #     log.info("Click the Login Button")
    #     time.sleep(3)
    #     if "Invalid credentials" in lg.Invalid_msg():
    #         assert True
    #         log.info("Test Case Pass")
    #     else:
    #         log.info("Test Case Fail")
    #         assert False
    #
