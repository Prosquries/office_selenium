import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from SighnupZipangApp_PageObject import ZipangappSighnup
from SighnupZipangApp_PageObject import ZipangLogin

class Test_Sighnup:

    def test_Sighnup(self):
        self.serv_obj = Service()
        self.driver = webdriver.Chrome(service = self.serv_obj)

        self.driver.get("https://zipang.myauctionstech.in/en/preview/products/698c1d65cc71343464b96334/Certificate%20Linking/2026-02-22%2012%3A10")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        lp = ZipangappSighnup(self.driver)
        lp.set_Homepage_nev()
        lp.set_Register_button()
        lp.set_FirstName("Aarav")
        lp.set_LastName("Mathur")
        lp.set_Company("Sysquare")
        lp.set_Email("aarav.2mathur@outlook.com")
        lp.set_Occupation()
        lp.set_Address("24/143 swarn path")
        lp.set_Country("India")
        time.sleep(1)
        lp.set_State("Rajasthan")
        time.sleep(1)
        lp.set_City("Jaipur")
        time.sleep(1)
        lp.set_phone("1234567890")
        lp.set_Language("ENGLISH")
        time.sleep(1)
        lp.set_Agree()
        # lp.set_Submit_button()
        input ("Press Enter to Continue...")
        self.driver.close()

        self.driver.close()