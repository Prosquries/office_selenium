from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from LoginPageObject import LoginPageObject
import time

class TestLogin:
    def test_login(self):
        self.serv_obj = Service()
        self.driver = webdriver.Chrome(service=self.serv_obj)

        self.driver.get("https://admin-demo.nopcommerce.com/login?returnUrl=%2Fadmin%2F")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        lp = LoginPageObject(self.driver)
        lp.set_username("admin@yourstore.com")
        lp.set_password("admin")
        lp.click_Login()
        self.act_title = self.driver.title

        assert self.act_title == "Just a moment..."
        self.driver.close()