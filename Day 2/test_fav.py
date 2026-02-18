import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from SighnupZipangApp_PageObject import ZipangFav

class Test_Downloads:

    def test_Fav(self):
            self.serv_obj = Service()
            self.driver = webdriver.Chrome(service=self.serv_obj)

            try:
                self.driver.get("https://zipang.myauctionstech.in/en/preview/products/698c1d65cc71343464b96334/Certificate%20Linking/2026-02-22%2012%3A10")
                self.driver.maximize_window()
                self.driver.implicitly_wait(10)

                fa = ZipangFav(self.driver)
                fa.set_HomePage()
                fa.set_Login()
                fa.set_Email("aarav.2mathur@outlook.com")
                fa.set_password("Aarav")
                fa.set_LoginButton()
                fa.set_Accept_buttons()
                fa.set_previewButton()
                time.sleep(1)
                fa.set_Grid_view_button()
                time.sleep(3)
                fa.set_favoriteButton()
                time.sleep(2)
            finally:
                self.driver.quit()