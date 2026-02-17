from selenium.webdriver.common.by import By

class LoginPageObject:
    # Locators
    Email_text_Id = "Email"
    password_text_ID = "Password"
    Login_btn_XPATH = "//button[normalize-space()='Log in']"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Actions
    def set_username(self, username):
        username_txt = self.driver.find_element(By.ID,self.Email_text_Id)
        username_txt.clear()
        username_txt.send_keys(username)

    def set_password(self, password):
        password_txt = self.driver.find_element(By.ID,self.password_text_ID)
        password_txt.clear()
        password_txt.send_keys(password)

    def click_Login(self):
        self.driver.find_element(By.XPATH, self.Login_btn_XPATH).click()