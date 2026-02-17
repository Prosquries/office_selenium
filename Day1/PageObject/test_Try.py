import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from Try1 import TravelFormPage

class TestTry:

    def test_DummyWebserver(self):
        self.serv_obj = Service()
        self.driver = webdriver.Chrome(service = self.serv_obj)

        self.driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        lp = TravelFormPage(self.driver)
        lp.set_username("Aarav","Mathur")
        lp.set_date("Mar","2005","18")
        lp.set_Gender()
        lp.set_destinations("Jaipur","Delhi")
        self.act_title = self.driver.title

        try:
            assert self.act_title == "Dummy ticket for applying visa - Verifiable flight reservation for embassy"
            self.driver.close()

        except:
            print("Page not found")
            self.driver.get_screenshot_as_file(r"D:\Aarav\Selenium\Day1\Screenshots\screenshot_123.png")
            self.driver.close()
            assert False

        self.driver.quit()