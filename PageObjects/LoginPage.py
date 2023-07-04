from selenium.webdriver.common.by import By


class Login():
    def __init__(self,driver):
        self.driver = driver
        self.text_username_xpath = "//input[@placeholder='Username']"
        self.text_userpassword_xpath = "//input[@type='password']"
        self.text_login_css = "button[type='submit']"
        self.text_invalidmsg_xpath = "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"

    def input_username(self,Username):
        self.driver.find_element(By.XPATH, self.text_username_xpath).send_keys(Username)

    def input_userpassword(self,Password):
        self.driver.find_element(By.XPATH, self.text_userpassword_xpath).send_keys(Password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.text_login_css).click()

    def Invalid_msg(self):
        return self.driver.find_element(By.XPATH, self.text_invalidmsg_xpath ).text




