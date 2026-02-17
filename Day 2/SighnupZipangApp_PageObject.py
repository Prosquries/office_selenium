import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ZipangappSighnup:
    # Locators
    HomePageNev_Icon_xpath = "//img[@alt='zipang image #1']"
    Register_button_xpath = "//span[normalize-space()='Register']"
    FirstName_text_xpath = "//input[@name='firstName']"
    LastName_text_xpath = "//input[@name='lastName']"
    Company_text_xpath = "//input[@name='company']"
    Email_text_xpath = "//input[@name='email']"
    Occupation_Radio_xpath = "//input[@value='AuctioneerAndBidder']"
    Address_text_xpath = "//input[@name='address']"
    Country_drop_xpath = "//div[@id='Country']"
    State_drop_xpath = f"//div[@id='State']"
    City_drop_xpath = "//div[@id='City']"
    Phone_text_xpath = "//input[@name='phone']"
    Language_text_xpath = "//div[@id='Preferred Language']"
    Agree_Checkbox_xpath = "//input[@id='checkedTerms']"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # Action
    def set_Homepage_nev(self):
        self.driver.find_element(By.XPATH,self.HomePageNev_Icon_xpath).click()

    def set_Register_button(self):
        self.driver.find_element(By.XPATH,self.Register_button_xpath).click()

    def set_FirstName(self,FirstName):
        FirstName_text = self.driver.find_element(By.XPATH,self.FirstName_text_xpath)
        FirstName_text.send_keys(FirstName)

    def set_LastName(self,LastName):
        LastName_text = self.driver.find_element(By.XPATH,self.LastName_text_xpath)
        LastName_text.send_keys(LastName)

    def set_Company(self,Company):
        Company_text = self.driver.find_element(By.XPATH,self.Company_text_xpath)
        Company_text.send_keys(Company)

    def set_Email(self,Email):
        Email_text = self.driver.find_element(By.XPATH,self.Email_text_xpath)
        Email_text.send_keys(Email)

    def set_Occupation(self):
        self.driver.find_element(By.XPATH,self.Occupation_Radio_xpath).click()

    def set_Address(self,Address):
        Address_text = self.driver.find_element(By.XPATH,self.Address_text_xpath)
        Address_text.send_keys(Address)

    def set_Country(self,Country):
        self.driver.find_element(By.XPATH, self.Country_drop_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,f"//ul[contains(@class,'MuiList-root')]//li[normalize-space()='{Country}']").click()

    def set_State(self,State):
        self.driver.find_element(By.XPATH, self.State_drop_xpath).click()
        time.sleep(1)

        self.driver.find_element(By.XPATH,f"//ul[contains(@class,'MuiList-root')]//li[normalize-space()='{State}']").click()

    def set_City(self,City):
        self.driver.find_element(By.XPATH,self.City_drop_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,f"//ul[contains(@class,'MuiList-root')]//li[normalize-space()='{City}']").click()

    def set_phone(self,Phone):
        Phone_text = self.driver.find_element(By.XPATH,self.Phone_text_xpath)
        Phone_text.send_keys(Phone)

    def set_Language(self,Lang):
        self.driver.find_element(By.XPATH,self.Language_text_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,f"//ul[contains(@class,'MuiList-root')]//li[normalize-space()='{Lang}']").click()

    def set_Agree(self):
        self.driver.find_element(By.XPATH,self.Agree_Checkbox_xpath).click()