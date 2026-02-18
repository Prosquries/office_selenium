import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from SighnupZipangApp_PageObject import ZipangDownload

class Test_Downloads:

    def test_Download_Clickable(self):

        self.serv_obj = Service()

        download_path = r"D:\Aarav\Selenium\Day 2\Downloads"

        ops = webdriver.ChromeOptions()
        prefs = {
            "download.default_directory": download_path
        }
        ops.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(service=self.serv_obj, options=ops)

        try:
            self.driver.get("https://zipang.myauctionstech.in/en/preview/products/698c1d65cc71343464b96334/Certificate%20Linking/2026-02-22%2012%3A10")
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)

            sa = ZipangDownload(self.driver)
            sa.set_HomePage()
            sa.set_Login()
            sa.set_Email("aarav.2mathur@outlook.com")
            sa.set_password("Aarav")
            sa.set_LoginButton()
            sa.set_Accept_buttons()
            sa.set_previewButton()
            time.sleep(1)
            sa.set_Grid_view_button()
            sa.set_Download_option()
            time.sleep(5)
            files = os.listdir(download_path)

            assert len(files) > 0
        finally:
            self.driver.quit()

