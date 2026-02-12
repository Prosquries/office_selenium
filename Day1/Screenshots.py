from XLUtils import *

os.chdir(r"D:\Aarav\Selenium\Day1\Screenshots")

# ops = webdriver.ChromeOptions()
# ops.add_argument("--headless=new")
# ops.add_argument("--window-size=1920,1080")
serv_obj = Service()
driver = webdriver.Chrome(service = serv_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(10)

Radio = driver.find_element(By.XPATH,"//input[@value='radio1']")
Radio.click()

# Checking if the radio button is clicked or not
print(Radio.is_selected())

# Selecting the country
country=driver.find_element(By.XPATH,"//input[@id='autocomplete']")
country.send_keys("Ind")
Action = ActionChains(driver)
time.sleep(2)
Action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
print(country.get_attribute("value"))

# Selecting the option 1 from the drop-down
Dropdown = Select(driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']"))
Dropdown.select_by_visible_text("Option1")

# Check box buttons

Check = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for check in Check:
    value = check.get_attribute("value")
    if value == "option1" or value == "option3":
        check.click()

driver.save_screenshot("screenshot.png")
driver.get_screenshot_as_file("capture.png") # Both the methods will take the screenshots no problem.

input("Enter")