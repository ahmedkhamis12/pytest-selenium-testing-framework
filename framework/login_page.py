from selenium.webdriver.common.by import By


class LoginPage:
    USER_FIELD = (By.ID, "username")
    PASS_FIELD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MSG = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.USER_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASS_FIELD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MSG).text
