import pytest
from selenium import webdriver
import os
os.chdir(r"D:\Aarav\Selenium\Day1\Screenshots")
class TestClass:

    @pytest.mark.parametrize('user,passwd',[("Admin","admin123"),("admin","admin123"),("Admin","abc"),("abc","abc")])
    def test_login(self,user,passwd):
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        self.serv_obj = Service()
        self.driver = webdriver.Chrome(service=self.serv_obj)

        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys(user)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys(passwd)
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

        try:
            Heading = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
            assert Heading == "Dashboard"
            print("The Heading is displayed, Test passed")

        except Exception as e:
            print("Test failed")
            self.driver.save_screenshot(fr"D:\Aarav\Selenium\Day1\Screenshots\screenshot_{user}_{passwd}.png")
            self.driver.close()
            assert False


        self.driver.close()