import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_login:

    def test_login_Chrome(self):
        from selenium.webdriver.chrome.service import Service
        self.serv_obj = Service()
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.implicitly_wait(10)

        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        self.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

        assert self.driver.title == "OrangeHRM"
        self.driver.quit()

    def test_login_Edge(self):
        from selenium.webdriver.edge.service import Service
        self.serv_obj = Service()
        self.driver = webdriver.Edge(service=self.serv_obj)
        self.driver.implicitly_wait(10)

        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        self.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

        assert self.driver.title == "OrangeHRM"
        self.driver.quit()

# python -m pytest -v -s -n=2 .\test_parallilism.py To run both at the same time
# python -m pytest -v -s .\test_parallilism.py To run single at a time