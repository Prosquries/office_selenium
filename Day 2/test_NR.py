import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from SighnupZipangApp_PageObject import ZipangNR

class Test_NR:

    def test_case_1_NR_ClickedAndVerify(self):
        self.serv_obj = Service()
        self.driver = webdriver.Chrome(service=self.serv_obj)

        try:
            self.driver.get("https://zipang.myauctionstech.in/en/preview/products/698c1d65cc71343464b96334/Certificate%20Linking/2026-02-22%2012%3A10")
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)

            nr = ZipangNR(self.driver)
            nr.set_HomePage()
            nr.set_Login()
            nr.set_Email("aarav.2mathur@outlook.com")
            nr.set_password("Aarav")
            nr.set_LoginButton()
            nr.set_Accept_buttons()
            nr.set_previewButton()
            time.sleep(1)
            nr.set_Grid_view_button()
            time.sleep(1)

            # Your logic
            nr.set_NR_button()
            time.sleep(5)
            nr.set_NR_present()

        finally:
            self.driver.quit()

    def test_case_2_NR_VerifyWithoutClick(self):

        self.serv_obj = Service()
        self.driver = webdriver.Chrome(service=self.serv_obj)

        try:
            self.driver.get("https://zipang.myauctionstech.in/en/preview/products/698c1d65cc71343464b96334/Certificate%20Linking/2026-02-22%2012%3A10")
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)

            nr = ZipangNR(self.driver)
            nr.set_HomePage()
            nr.set_Login()
            nr.set_Email("aarav.2mathur@outlook.com")
            nr.set_password("Aarav")
            nr.set_LoginButton()
            nr.set_Accept_buttons()
            nr.set_previewButton()
            time.sleep(1)
            nr.set_Grid_view_button()
            time.sleep(1)

            # Your logic fixed
            After_click = nr.set_NR_displayed_after()
            Before_click = nr.set_NR_displayed_before()

            assert After_click != Before_click

        finally:
            self.driver.quit()