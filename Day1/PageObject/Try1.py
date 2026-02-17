from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



class TravelFormPage:

    # ------------------ Locators ------------------

    FirstName_txt_xpath = "//input[@id='travname']"
    LastName_txt_xpath = "//input[@id='travlastname']"

    Date_picker_xpath = "//input[@id='dob']"
    Month_picker_xpath = "//select[@aria-label='Select month']"
    Year_picker_xpath = "//select[@aria-label='Select year']"
    Day_picker_xpath = "//table[@class='ui-datepicker-calendar']/tbody/tr/td"

    Gender_radio_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/form[2]/div[2]/div[1]/div[1]/p[4]/span[1]/input[1]"


    From_City_xpath = "//input[@id='fromcity']"
    To_City_xpath = "//input[@id='tocity']"

    Dept_Date_xpath = "//input[@id='departon']"
    Dept_Month_xpath = "//select[@aria-label='Select month']"
    Dept_year_xpath = "//select[@aria-label='Select year']"
    Dept_Day_xpath = "//table[@class='ui-datepicker-calendar']/tbody/tr/td"


    Billing_Name_xpath = "//input[@id='billname']"
    Billing_phone_xpath = "//input[@id='billing_phone']"
    Billing_Email_xpath = "//input[@id='billing_email']"
    Billing_Country_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/form[2]/div[2]/div[1]/div[1]/div[5]/p[4]/span[1]/span[1]/span[1]/span[1]/span[1]"
    Billing_address_xpath = "//input[@name = 'billing_address_1']"
    Billing_Town_xpath = "//input[@id='billing_city']"
    Billing_State_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/form[2]/div[2]/div[1]/div[1]/div[5]/p[8]/span[1]/span[1]/span[1]/span[1]/span[1]"
    Billing_Pincode_xpath = "//input[@id='billing_postcode']"

    Place_holder_xpath = "//button[@id='place_order']"

    # ------------------ Constructor ------------------

    def __init__(self, driver):
        self.driver = driver

    # ------------------ Actions ------------------

    def set_username(self, first_name, last_name):

        first_name_txt = self.driver.find_element(By.XPATH, self.FirstName_txt_xpath)
        first_name_txt.clear()
        first_name_txt.send_keys(first_name)

        last_name_txt = self.driver.find_element(By.XPATH, self.LastName_txt_xpath)
        last_name_txt.clear()
        last_name_txt.send_keys(last_name)

    def set_date(self, month, year, day):

        # Open date picker first
        self.driver.find_element(By.XPATH, self.Date_picker_xpath).click()

        # Select month
        month_dropdown = Select(self.driver.find_element(By.XPATH, self.Month_picker_xpath))
        month_dropdown.select_by_visible_text(month)

        # Select year
        year_dropdown = Select(self.driver.find_element(By.XPATH, self.Year_picker_xpath))
        year_dropdown.select_by_visible_text(year)

        # Select day
        days = self.driver.find_elements(By.XPATH, self.Day_picker_xpath)

        for d in days:
            if d.text == day:
                d.click()
                break

    def set_Gender(self):
        self.driver.find_element(By.XPATH,self.Gender_radio_xpath).click()

    def set_destinations(self, from_city, to_city):

        from_txt = self.driver.find_element(By.XPATH, self.From_City_xpath)
        from_txt.clear()
        from_txt.send_keys(from_city)

        to_txt = self.driver.find_element(By.XPATH, self.To_City_xpath)
        to_txt.clear()
        to_txt.send_keys(to_city)

    def set_deptDate(self,Month,Year,Day):

        # Open the date picker
        self.driver.find_element(By.XPATH,self.Dept_Date_xpath).click()

        # Select Month
        Mon = Select(self.driver.find_element(By.XPATH,self.Dept_Month_xpath))
        Mon.select_by_visible_text(Month)

        # Selecting Year
        Yea = Select(self.driver.find_element(By.XPATH,self.Dept_year_xpath))
        Yea.select_by_visible_text(Year)

        # Selecting Day
        Days = self.driver.find_elements(By.XPATH,self.Dept_Day_xpath)

        for D in Days:
            if D.text == Day:
                D.click()
                break

    def set_Billing(self,BillName,BillNumber,BillEmail,BillCountry,BillAddress,BillTown,BillState,BillPincode):

        BillName_text = self.driver.find_element(By.XPATH,self.Billing_Name_xpath)
        BillName_text.send_keys(BillName)

        BillNumber_text = self.driver.find_element(By.XPATH,self.Billing_phone_xpath)
        BillNumber_text.send_keys(BillNumber)

        BillEmail_text = self.driver.find_element(By.XPATH,self.Billing_Email_xpath)
        BillEmail_text.send_keys(BillEmail)

        # Click country dropdown
        self.driver.find_element(By.XPATH, self.Billing_Country_xpath).click()

        # Type country
        country_input = self.driver.find_element(By.XPATH, "//input[@class='select2-search__field']")
        country_input.send_keys(BillCountry)
        country_input.send_keys(Keys.ENTER)

        BillAddress_text = self.driver.find_element(By.XPATH,self.Billing_address_xpath)
        BillAddress_text.send_keys(BillAddress)

        BillTown_text = self.driver.find_element(By.XPATH,self.Billing_Town_xpath)
        BillTown_text.send_keys(BillTown)

        self.driver.find_element(By.XPATH, self.Billing_State_xpath).click()

        state_input = self.driver.find_element(By.XPATH, "//input[@class='select2-search__field']")
        state_input.send_keys(BillState)
        state_input.send_keys(Keys.ENTER)

        BillPincode_text = self.driver.find_element(By.XPATH,self.Billing_Pincode_xpath)
        BillPincode_text.send_keys(BillPincode)

