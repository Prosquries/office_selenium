import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from SighnupZipangApp_PageObject import ZipangLogin

class Test_Login:

    def test_Login(self):
        self.serv_obj = Service()
        self.driver = webdriver.Chrome(service = self.serv_obj)

        self.driver.get("https://zipang.myauctionstech.in/en/preview/products/698c1d65cc71343464b96334/Certificate%20Linking/2026-02-22%2012%3A10")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        pl = ZipangLogin(self.driver)
        pl.set_HomePage()
        pl.set_Login()
        pl.set_Email("aarav.2mathur@outlook.com")
        pl.set_password("Aarav")
        pl.set_LoginButton()
        # pl.set_NewPassword("Aarav")
        # pl.set_ConfirmPassword("Aarav")   # Only for one time
        # pl.set_Set_PasswordButton()
        pl.set_Accept_buttons()
        pl.set_previewButton()
        time.sleep(3)
        pl.set_Select_all_button()
        time.sleep(3)
        pl.set_Bid_icon()
        time.sleep(3)
        pl.set_Increase_button()
        time.sleep(3)
        pl.set_Place_button()
        pl.set_Grid_view_button()
        self.driver.get_screenshot_as_file(r"D:\Aarav\Selenium\Day 2\Screenshots\Screenshots1.png")
        pl.set_PageChanger()
        pl.set_Enter_amount_text("123546")
        pl.set_Press_yes_button()
        time.sleep(1)
        self.driver.get_screenshot_as_file(r"D:\Aarav\Selenium\Day 2\Screenshots\Screenshots2.png")
