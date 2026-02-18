import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from SighnupZipangApp_PageObject import ZipangSearch

class Test_Search:

    def test_case_1_Valid_Search(self):
        self.serv_obj = Service()
        self.driver = webdriver.Chrome(service = self.serv_obj)

        try:
            self.driver.get("https://zipang.myauctionstech.in/en/preview/products/698c1d65cc71343464b96334/Certificate%20Linking/2026-02-22%2012%3A10")
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)

            sa = ZipangSearch(self.driver)
            sa.set_HomePage()
            sa.set_Login()
            sa.set_Email("aarav.2mathur@outlook.com")
            sa.set_password("Aarav")
            sa.set_LoginButton()
            sa.set_Accept_buttons()
            sa.set_previewButton()
            time.sleep(1)
            sa.set_Grid_view_button()

            ## Case 1 Searching valid data

            sa.set_SearchButton("1")
            sa.set_Search_Valid()


        finally:
            self.driver.quit()

    def test_case_2_Invlaid_Search(self):
        self.serv_obj = Service()
        self.driver = webdriver.Chrome(service = self.serv_obj)

        try:
            self.driver.get("https://zipang.myauctionstech.in/en/preview/products/698c1d65cc71343464b96334/Certificate%20Linking/2026-02-22%2012%3A10")
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)

            sa = ZipangSearch(self.driver)
            sa.set_HomePage()
            sa.set_Login()
            sa.set_Email("aarav.2mathur@outlook.com")
            sa.set_password("Aarav")
            sa.set_LoginButton()
            sa.set_Accept_buttons()
            sa.set_previewButton()
            time.sleep(1)
            sa.set_Grid_view_button()

            # case 2 Invalid data

            sa.set_SearchButton("aarav")
            sa.set_Search_Valid()

        finally:
            self.driver.quit()

    def test_case_3_Empty_Search(self):
        self.serv_obj = Service()
        self.driver = webdriver.Chrome(service = self.serv_obj)

        try:
            self.driver.get("https://zipang.myauctionstech.in/en/preview/products/698c1d65cc71343464b96334/Certificate%20Linking/2026-02-22%2012%3A10")
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)

            sa = ZipangSearch(self.driver)
            sa.set_HomePage()
            sa.set_Login()
            sa.set_Email("aarav.2mathur@outlook.com")
            sa.set_password("Aarav")
            sa.set_LoginButton()
            sa.set_Accept_buttons()
            sa.set_previewButton()
            time.sleep(1)
            sa.set_Grid_view_button()

            # Case 3 empty search
            sa.set_SearchButton("")
            sa.is_result_present()

        finally:
            self.driver.quit()

