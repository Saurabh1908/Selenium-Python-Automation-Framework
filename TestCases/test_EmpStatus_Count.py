import pytest
from selenium.webdriver.common.by import By
import time
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import dashboard
from selenium.webdriver import ActionChains
from PageObjects.EmploymentStatusPage import EmpStatus
@pytest.mark.usefixtures("setUp")
class TestLogin():
    def test_001(self):
        lg = Login(self.driver)
        db = dashboard(self.driver)
        es = EmpStatus(self.driver)
        lg.input_username("Admin")
        time.sleep(3)
        lg.input_userpassword("admin123")
        time.sleep(3)
        lg.click_login()
        time.sleep(3)
        ActionChains(self.driver).move_to_element(db.hover_Admin()).perform()
        time.sleep(3)
        ActionChains(self.driver).move_to_element(db.hover_Job()).perform()

        ActionChains(self.driver).move_to_element(db.click_Employment_Status()).click().perform()

        old_status_count=0
        for i in es.total_status():
            old_status_count=old_status_count+1
            print(old_status_count)
        es.click_AddButton()
        time.sleep(3)
        # es.input_new_status("Automation Tester")
        # time.sleep(3)
        # es.click_SaveButton()
        # New_status_count=0
        # for j in es.total_status():
        #     New_status_count=New_status_count+1
        # print(New_status_count)


