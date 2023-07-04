from selenium.webdriver.common.by import By


class EmpStatus():
    def __init__(self, driver):
        self.driver = driver
        self.button_add_status_xpath = "//i[@class='oxd-icon bi-plus oxd-button-icon']"
        self.inputfield_name_xpath = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
        self.total_field_xpath = "//div[@class='oxd-table-card']"
        self.button_save_xpath = "//button[@type='submit']"
    def click_AddButton(self):
        self.driver.find_element(By.XPATH,self.button_add_status_xpath).click()

    def input_new_status(self,Name):
        self.driver.find_element(By.XPATH,self.inputfield_name_xpath).send_keys(Name)

    def total_status(self):
        return self.driver.find_elements(By.XPATH, self.total_field_xpath)

    def click_SaveButton(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()

