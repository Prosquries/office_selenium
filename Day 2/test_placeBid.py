import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from SighnupZipangApp_PageObject import ZipangPlaceBid

class Test_PlaceBid:

    def test_case_1_PlaceBid_Withoutamount(self):
        self.serv_obj = Service()
        self.driver = webdriver.Chrome(service = self.serv_obj)

        try:
            self.driver.get("https://zipang.myauctionstech.in/en/preview/products/698c1d65cc71343464b96334/Certificate%20Linking/2026-02-22%2012%3A10")
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)

            pb = ZipangPlaceBid(self.driver)
            pb.set_HomePage()
            pb.set_Login()
            pb.set_Email("aarav.2mathur@outlook.com")
            pb.set_password("Aarav")
            pb.set_LoginButton()
            pb.set_Accept_buttons()
            pb.set_previewButton()
            time.sleep(1)
            pb.set_Grid_view_button()
            time.sleep(3)
            # Case 1 Placing the bid without any amount
            pb.set_placeBid_xpath_empty()

        finally:
            self.driver.quit()

    def test_case_2_PlaceBid_EnterValidamount(self):

        self.serv_obj = Service()
        self.driver = webdriver.Chrome(service=self.serv_obj)

        try:
            self.driver.get(
                "https://zipang.myauctionstech.in/en/preview/products/698c1d65cc71343464b96334/Certificate%20Linking/2026-02-22%2012%3A10")
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)

            pb = ZipangPlaceBid(self.driver)
            pb.set_HomePage()
            pb.set_Login()
            pb.set_Email("aarav.2mathur@outlook.com")
            pb.set_password("Aarav")
            pb.set_LoginButton()
            pb.set_Accept_buttons()
            pb.set_previewButton()
            time.sleep(1)
            pb.set_Grid_view_button()
            time.sleep(3)
            # Case 1 Placing the bid without any amount
            pb.set_placeBid_xpath_ValidAmount()

        finally:
            self.driver.quit()

    def test_case_3_PlaceBid_EnterNegativeamount(self):

        self.serv_obj = Service()
        self.driver = webdriver.Chrome(service=self.serv_obj)

        try:
            self.driver.get(
                "https://zipang.myauctionstech.in/en/preview/products/698c1d65cc71343464b96334/Certificate%20Linking/2026-02-22%2012%3A10")
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)

            pb = ZipangPlaceBid(self.driver)
            pb.set_HomePage()
            pb.set_Login()
            pb.set_Email("aarav.2mathur@outlook.com")
            pb.set_password("Aarav")
            pb.set_LoginButton()
            pb.set_Accept_buttons()
            pb.set_previewButton()
            time.sleep(1)
            pb.set_Grid_view_button()
            time.sleep(3)
            # Case 1 Placing the bid without any amount
            pb.set_placeBid_xpath_Negativeamount()

        finally:
            self.driver.quit()

    def test_case_4_PlaceBid_StringAsAmount(self):

        self.serv_obj = Service()
        self.driver = webdriver.Chrome(service=self.serv_obj)

        try:
            self.driver.get(
                "https://zipang.myauctionstech.in/en/preview/products/698c1d65cc71343464b96334/Certificate%20Linking/2026-02-22%2012%3A10")
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)

            pb = ZipangPlaceBid(self.driver)
            pb.set_HomePage()
            pb.set_Login()
            pb.set_Email("aarav.2mathur@outlook.com")
            pb.set_password("Aarav")
            pb.set_LoginButton()
            pb.set_Accept_buttons()
            pb.set_previewButton()
            time.sleep(1)
            pb.set_Grid_view_button()
            time.sleep(3)
            # Case 1 Placing the bid without any amount
            pb.set_placeBid_xpath_StringAsAmount()

        finally:
            self.driver.quit()