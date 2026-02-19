import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from SighnupZipangApp_PageObject import ZipangBulkBid


class Test_BulkBid:

    def test_case_1_Bulk_WithoutSelection(self):

        self.serv_obj = Service()
        self.driver = webdriver.Chrome(service = self.serv_obj)

        try:
            self.driver.get("https://zipang.myauctionstech.in/en/preview/products/698c1d65cc71343464b96334/Certificate%20Linking/2026-02-22%2012%3A10")
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)

            bb = ZipangBulkBid(self.driver)
            bb.set_HomePage()
            bb.set_Login()
            bb.set_Email("aarav.2mathur@outlook.com")
            bb.set_password("Aarav")
            bb.set_LoginButton()
            bb.set_Accept_buttons()
            bb.set_previewButton()
            time.sleep(1)
            bb.set_Grid_view_button()
            time.sleep(3)
            # Case 1 Placing the bid without any amount
            bb.set_BulkBidButton_xpath_WithoutSelection()

        finally:
            self.driver.quit()

    def test_case_2_BulkBid_WithSelection(self):

        self.serv_obj = Service()
        self.driver = webdriver.Chrome(service=self.serv_obj)

        try:
            self.driver.get(
                "https://zipang.myauctionstech.in/en/preview/products/698c1d65cc71343464b96334/Certificate%20Linking/2026-02-22%2012%3A10")
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)

            bb = ZipangBulkBid(self.driver)
            bb.set_HomePage()
            bb.set_Login()
            bb.set_Email("aarav.2mathur@outlook.com")
            bb.set_password("Aarav")
            bb.set_LoginButton()
            bb.set_Accept_buttons()
            bb.set_previewButton()
            time.sleep(1)
            bb.set_Grid_view_button()
            time.sleep(3)
            # Case 1 Placing the bid without any amount
            bb.set_BulkBidButton_xpath_WithSelection()

        finally:
            self.driver.quit()
