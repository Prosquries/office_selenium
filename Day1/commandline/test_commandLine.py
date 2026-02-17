import pytest

class TestCLI:
    def test_Login(self, Setup):
        self.driver = Setup
        from selenium.webdriver.common.by import By

        self.driver.implicitly_wait(10)

        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
        Heading=self.driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']").text
        try:
            assert Heading == "Dashboard"
            print("It matches the Heading Valid test")
        except:
            print("The Page is not found hence test case failed")
            self.driver.close()
            assert False

        self.driver.close()