from XLUtils import *
serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.implicitly_wait(10)

# Click radio button
radio = driver.find_element(By.ID, "product_550")
radio.click()
print(radio.is_selected())   # Better check than is_displayed()

# Name fields
driver.find_element(By.ID, "travname").send_keys("Aarav")
driver.find_element(By.ID, "travlastname").send_keys("Mathur")

# Optional note
driver.find_element(By.ID, "order_comments").send_keys("This is optional note written by Selenium")

# Click date field first
driver.find_element(By.ID, "dob").click()

# Select Month
month = Select(driver.find_element(By.CLASS_NAME, "ui-datepicker-month"))
month.select_by_visible_text("Mar")

# Select Year
year = Select(driver.find_element(By.CLASS_NAME, "ui-datepicker-year"))
year.select_by_visible_text("2005")

# Select Day
days = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//a")

for day in days:
    if day.text == "18":
        day.click()
        break

# Select Gender
driver.find_element(By.ID, "sex_1").click()

# Click Add more passengers checkbox
driver.find_element(By.ID, "addmorepax").click()

# From City
driver.find_element(By.XPATH,"//input[@id='fromcity']").send_keys("Jaipur")

# To city
driver.find_element(By.XPATH,"//input[@id='tocity']").send_keys("Delhi")

# Departure Date

# Departure Date
driver.find_element(By.ID, "departon").click()

# Select Month
mon = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
mon.select_by_visible_text("Feb")

# Select Year
yea = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
yea.select_by_visible_text("2027")

# Select Day
dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td")

for d in dates:
    if d.text == "12":
        d.click()
        break

# Additional Address
driver.find_element(By.XPATH,"//textarea[@id='notes']").send_keys("24/143 jaipur")

input ("Enter")