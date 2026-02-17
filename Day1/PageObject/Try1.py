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
