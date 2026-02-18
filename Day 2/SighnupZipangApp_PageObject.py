import time
from encodings.punycode import selective_find
from selenium.webdriver import ActionChains, Keys
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    # Submit_Button_xpath = "//span[normalize-space()='Create Your Account']"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # Action

        self.wait = WebDriverWait(driver, 15,2)

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

    # def set_Submit_button(self):                  # Can not be done bu automation due to capcha
    #     input("Solve captcha and press Enter to continue...")
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Submit_Button_xpath))).click()

class ZipangLogin:
    #------ locators --------
    HomePageNev_Icon_xpath = "//img[@alt='zipang image #1']"
    Login_button_xpath = "//span[@id='sign-in']"
    Email_text_xpath = "//input[@id='email']"
    Password_text_xpath = "//input[@id='password']"
    Submit_button_xpath = "//div[@class='MuiGrid-root sc-hGjceG bYqeUY MuiGrid-container MuiGrid-align-items-xs-center MuiGrid-justify-content-xs-space-between']//span[@class='MuiButton-label'][normalize-space()='Login']"
    New_password_text_xpath = "//input[@id='newPassword']"
    Confirm_password_text_xpath = "//input[@id='confirmPassword']"
    Set_password_button_xpath = "//button[normalize-space()='SET PASSWORD']"
    Accept_button1_xpath = "//button[normalize-space()='ACCEPT']"
    Accept_button2_xpath = "/html/body/div[3]/div[3]/div/button"
    Accept_button3_xpath = "/html/body/div[3]/div[3]/div/button"
    Accept_button4_xpath = "/html/body/div[3]/div[3]/div/button"
    Preview_button_xpath = "//span[contains(text(),'PREVIEW')]"
    Select_all_button_xpath = "//button[normalize-space()='Select All']"
    Bid_icon_xpath = "//img[@title='Select items to bulk prebid or watchlist']"
    Increase_biding_xpath = "//button[contains(.,'100')]"
    Place_bid_button_xpath = "//button[normalize-space()='Place Bid']"
    Grid_view_button_xpath = "//img[@title='List view of Product']"
    page_changer_xpath = "//button[@title='Go to next page']//*[name()='svg']"
    Enter_amount_text_xpath = "(//input[@id='preBiddingPrice'])[2]"
    Press_yes_button_xpath = "//button[normalize-space()='Yes']"

    # -------Constructor -----------

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    # ------- Actions ---------------

    def set_HomePage(self):
        self.driver.find_element(By.XPATH,self.HomePageNev_Icon_xpath).click()

    def set_Login(self):
        self.driver.find_element(By.XPATH,self.Login_button_xpath).click()

    def set_Email(self,Email):
        Email_text = self.driver.find_element(By.XPATH,self.Email_text_xpath)
        Email_text.send_keys(Email)

    def set_password(self,Password):
        Password_text = self.driver.find_element(By.XPATH,self.Password_text_xpath)
        Password_text.send_keys(Password)

    def set_LoginButton(self):
        self.driver.find_element(By.XPATH,self.Submit_button_xpath).click()

    def set_NewPassword(self,Password):
        new_password_Text = self.driver.find_element(By.XPATH,self.New_password_text_xpath)
        new_password_Text.send_keys(Password)

    def set_ConfirmPassword(self,Password):
        Conf_password_text = self.driver.find_element(By.XPATH,self.Confirm_password_text_xpath)
        Conf_password_text.send_keys(Password)

    def set_Set_PasswordButton(self):
        self.driver.find_element(By.XPATH,self.Set_password_button_xpath).click()

    def set_Accept_buttons(self):
        self.driver.find_element(By.XPATH,self.Accept_button1_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Accept_button2_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Accept_button3_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Accept_button4_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Accept_button4_xpath).click()

    def set_previewButton(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Preview_button_xpath))).click()

    def set_Select_all_button(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.Select_all_button_xpath))).click()

    def set_Bid_icon(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.Bid_icon_xpath))).click()

    def set_Increase_button(self):
        Button=self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.Increase_biding_xpath)))

        for B in Button:
            B.click()

    def set_Place_button(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Place_bid_button_xpath))).click()

    def set_Grid_view_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Grid_view_button_xpath).click()

    def set_PageChanger(self):
        self.driver.find_element(By.XPATH,self.page_changer_xpath).click()

    def set_Enter_amount_text(self,prebid):
        prebid_text=self.driver.find_element(By.XPATH,self.Enter_amount_text_xpath)
        prebid_text.send_keys(prebid)

    def set_Press_yes_button(self):
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        self.driver.find_element(By.XPATH,self.Press_yes_button_xpath).click()

class ZipangSearch:

    #----------- Locators ----------------
    HomePageNev_Icon_xpath = "//img[@alt='zipang image #1']"
    Login_button_xpath = "//span[@id='sign-in']"
    Email_text_xpath = "//input[@id='email']"
    Password_text_xpath = "//input[@id='password']"
    Submit_button_xpath = "//div[@class='MuiGrid-root sc-hGjceG bYqeUY MuiGrid-container MuiGrid-align-items-xs-center MuiGrid-justify-content-xs-space-between']//span[@class='MuiButton-label'][normalize-space()='Login']"
    New_password_text_xpath = "//input[@id='newPassword']"
    Confirm_password_text_xpath = "//input[@id='confirmPassword']"
    Set_password_button_xpath = "//button[normalize-space()='SET PASSWORD']"
    Accept_button1_xpath = "//button[normalize-space()='ACCEPT']"
    Accept_button2_xpath = "/html/body/div[3]/div[3]/div/button"
    Accept_button3_xpath = "/html/body/div[3]/div[3]/div/button"
    Accept_button4_xpath = "/html/body/div[3]/div[3]/div/button"
    Preview_button_xpath = "//span[contains(text(),'PREVIEW')]"
    Grid_view_button_xpath = "//img[@title='List view of Product']"
    Search_text_xpath = "//input[@id='free-solo-demo']"
    Element_Button_xpath = "//th[2]//span[1]//button[1]"
    No_of_Elements_xpath = "//tbody/tr/td[2]"

    #----------- Constructor --------------

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    #------------ Actions -----------------

    def set_HomePage(self):
        self.driver.find_element(By.XPATH,self.HomePageNev_Icon_xpath).click()

    def set_Login(self):
        self.driver.find_element(By.XPATH,self.Login_button_xpath).click()

    def set_Email(self,Email):
        Email_text = self.driver.find_element(By.XPATH,self.Email_text_xpath)
        Email_text.send_keys(Email)

    def set_password(self,Password):
        Password_text = self.driver.find_element(By.XPATH,self.Password_text_xpath)
        Password_text.send_keys(Password)

    def set_LoginButton(self):
        self.driver.find_element(By.XPATH,self.Submit_button_xpath).click()

    def set_Set_PasswordButton(self):
        self.driver.find_element(By.XPATH,self.Set_password_button_xpath).click()

    def set_Accept_buttons(self):
        self.driver.find_element(By.XPATH,self.Accept_button1_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Accept_button2_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Accept_button3_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Accept_button4_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Accept_button4_xpath).click()

    def set_previewButton(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Preview_button_xpath))).click()

    def set_Grid_view_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Grid_view_button_xpath).click()

    def set_SearchButton(self,search):
        search_text = self.driver.find_element(By.XPATH,self.Search_text_xpath)
        search_text.send_keys(search)
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    ## Test Seach
    def set_Search_Valid(self):
        Element=self.driver.find_element(By.XPATH,self.Element_Button_xpath)
        assert Element.is_displayed()

    def is_result_present(self):
        Elements = self.driver.find_elements(By.XPATH,self.No_of_Elements_xpath)
        assert len(Elements) == 1

class ZipangNR:

# --------- Locators -----------------
    HomePageNev_Icon_xpath = "//img[@alt='zipang image #1']"
    Login_button_xpath = "//span[@id='sign-in']"
    Email_text_xpath = "//input[@id='email']"
    Password_text_xpath = "//input[@id='password']"
    Submit_button_xpath = "//div[@class='MuiGrid-root sc-hGjceG bYqeUY MuiGrid-container MuiGrid-align-items-xs-center MuiGrid-justify-content-xs-space-between']//span[@class='MuiButton-label'][normalize-space()='Login']"
    New_password_text_xpath = "//input[@id='newPassword']"
    Confirm_password_text_xpath = "//input[@id='confirmPassword']"
    Set_password_button_xpath = "//button[normalize-space()='SET PASSWORD']"
    Accept_button1_xpath = "//button[normalize-space()='ACCEPT']"
    Accept_button2_xpath = "/html/body/div[3]/div[3]/div/button"
    Accept_button3_xpath = "/html/body/div[3]/div[3]/div/button"
    Accept_button4_xpath = "/html/body/div[3]/div[3]/div/button"
    Preview_button_xpath = "//span[contains(text(),'PREVIEW')]"
    Grid_view_button_xpath = "//img[@title='List view of Product']"
    NR_Button_xpath = "//img[@alt='reserve']"
    NR_present_xpath = "//td[3][contains(.,'NR')]"
#----------- constructor --------------
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
#----------- Actions --------------------

    def set_HomePage(self):
        self.driver.find_element(By.XPATH,self.HomePageNev_Icon_xpath).click()

    def set_Login(self):
        self.driver.find_element(By.XPATH,self.Login_button_xpath).click()

    def set_Email(self,Email):
        Email_text = self.driver.find_element(By.XPATH,self.Email_text_xpath)
        Email_text.send_keys(Email)

    def set_password(self,Password):
        Password_text = self.driver.find_element(By.XPATH,self.Password_text_xpath)
        Password_text.send_keys(Password)

    def set_LoginButton(self):
        self.driver.find_element(By.XPATH,self.Submit_button_xpath).click()

    def set_Set_PasswordButton(self):
        self.driver.find_element(By.XPATH,self.Set_password_button_xpath).click()

    def set_Accept_buttons(self):
        self.driver.find_element(By.XPATH,self.Accept_button1_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Accept_button2_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Accept_button3_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Accept_button4_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Accept_button4_xpath).click()

    def set_previewButton(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Preview_button_xpath))).click()

    def set_Grid_view_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Grid_view_button_xpath).click()

    def set_NR_displayed_before(self):
        nr_elements = self.driver.find_elements(By.XPATH, self.NR_present_xpath)
        return len(nr_elements)

    def set_NR_button(self):
        self.driver.find_element(By.XPATH,self.NR_Button_xpath).click()

    def set_NR_present(self):
        NR_present=self.driver.find_elements(By.XPATH,self.NR_present_xpath)
        assert len(NR_present) > 0

    def set_NR_displayed_after(self):
        self.driver.find_element(By.XPATH, self.NR_Button_xpath).click()
        nr_elements = self.driver.find_elements(By.XPATH, self.NR_present_xpath)
        return len(nr_elements)

class ZipangDownload:

#-------------- Locators---------------
    HomePageNev_Icon_xpath = "//img[@alt='zipang image #1']"
    Login_button_xpath = "//span[@id='sign-in']"
    Email_text_xpath = "//input[@id='email']"
    Password_text_xpath = "//input[@id='password']"
    Submit_button_xpath = "//div[@class='MuiGrid-root sc-hGjceG bYqeUY MuiGrid-container MuiGrid-align-items-xs-center MuiGrid-justify-content-xs-space-between']//span[@class='MuiButton-label'][normalize-space()='Login']"
    New_password_text_xpath = "//input[@id='newPassword']"
    Confirm_password_text_xpath = "//input[@id='confirmPassword']"
    Set_password_button_xpath = "//button[normalize-space()='SET PASSWORD']"
    Accept_button1_xpath = "//button[normalize-space()='ACCEPT']"
    Accept_button2_xpath = "/html/body/div[3]/div[3]/div/button"
    Accept_button3_xpath = "/html/body/div[3]/div[3]/div/button"
    Accept_button4_xpath = "/html/body/div[3]/div[3]/div/button"
    Preview_button_xpath = "//span[contains(text(),'PREVIEW')]"
    Grid_view_button_xpath = "//img[@title='List view of Product']"
    Download_option_xpath = "//img[@alt='exportsheet']"

# ---------------- Constructor --------------

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

# ----------------- Action ------------------

    def set_HomePage(self):
        self.driver.find_element(By.XPATH,self.HomePageNev_Icon_xpath).click()

    def set_Login(self):
        self.driver.find_element(By.XPATH,self.Login_button_xpath).click()

    def set_Email(self,Email):
        Email_text = self.driver.find_element(By.XPATH,self.Email_text_xpath)
        Email_text.send_keys(Email)

    def set_password(self,Password):
        Password_text = self.driver.find_element(By.XPATH,self.Password_text_xpath)
        Password_text.send_keys(Password)

    def set_LoginButton(self):
        self.driver.find_element(By.XPATH,self.Submit_button_xpath).click()

    def set_Set_PasswordButton(self):
        self.driver.find_element(By.XPATH,self.Set_password_button_xpath).click()

    def set_Accept_buttons(self):
        self.driver.find_element(By.XPATH,self.Accept_button1_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Accept_button2_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Accept_button3_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Accept_button4_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Accept_button4_xpath).click()

    def set_previewButton(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Preview_button_xpath))).click()

    def set_Grid_view_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.Grid_view_button_xpath).click()

    def set_Download_option(self):
        self.driver.find_element(By.XPATH,self.Download_option_xpath).click()

class ZipangFav:

# ------------ Locators -----------------

    HomePageNev_Icon_xpath = "//img[@alt='zipang image #1']"
    Login_button_xpath = "//span[@id='sign-in']"
    Email_text_xpath = "//input[@id='email']"
    Password_text_xpath = "//input[@id='password']"
    Submit_button_xpath = "//div[@class='MuiGrid-root sc-hGjceG bYqeUY MuiGrid-container MuiGrid-align-items-xs-center MuiGrid-justify-content-xs-space-between']//span[@class='MuiButton-label'][normalize-space()='Login']"
    New_password_text_xpath = "//input[@id='newPassword']"
    Confirm_password_text_xpath = "//input[@id='confirmPassword']"
    Set_password_button_xpath = "//button[normalize-space()='SET PASSWORD']"
    Accept_button1_xpath = "//button[normalize-space()='ACCEPT']"
    Accept_button2_xpath = "/html/body/div[3]/div[3]/div/button"
    Accept_button3_xpath = "/html/body/div[3]/div[3]/div/button"
    Accept_button4_xpath = "/html/body/div[3]/div[3]/div/button"
    Preview_button_xpath = "//span[contains(text(),'PREVIEW')]"
    Grid_view_button_xpath = "//img[@title='List view of Product']"
    Heart_SVG_element_xpath = "//*[name()='svg' and contains(@class,'fa-heart')]"

# ------------ Constructor --------------
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

# ------------ Actions ------------------

    def set_HomePage(self):
        self.driver.find_element(By.XPATH,  self.HomePageNev_Icon_xpath).click()


    def set_Login(self):
        self.driver.find_element(By.XPATH, self.Login_button_xpath).click()


    def set_Email(self, Email):
        Email_text = self.driver.find_element(By.XPATH, self.Email_text_xpath)
        Email_text.send_keys(Email)


    def set_password(self, Password):
        Password_text = self.driver.find_element(By.XPATH, self.Password_text_xpath)
        Password_text.send_keys(Password)


    def set_LoginButton(self):
        self.driver.find_element(By.XPATH, self.Submit_button_xpath).click()


    def set_Set_PasswordButton(self):
        self.driver.find_element(By.XPATH, self.Set_password_button_xpath).click()


    def set_Accept_buttons(self):
        self.driver.find_element(By.XPATH, self.Accept_button1_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Accept_button2_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Accept_button3_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Accept_button4_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Accept_button4_xpath).click()


    def set_previewButton(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Preview_button_xpath))).click()


    def set_Grid_view_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Grid_view_button_xpath).click()

    def set_favoriteButton(self):
        heart = self.driver.find_element(By.XPATH, self.Heart_SVG_element_xpath)
        before_color = heart.value_of_css_property("color")

        heart.click()
        time.sleep(2)

        after_color = heart.value_of_css_property("color")

        assert before_color != after_color
