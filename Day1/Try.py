from XLUtils import *

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)

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
    if value == "option1" or value == "option2":
        check.click()

# Switch window
driver.find_element(By.XPATH,"//button[@id='openwindow']").click()
time.sleep(2)

WindowIDS=driver.window_handles
Parent = WindowIDS[0]
child = WindowIDS[1]

driver.switch_to.window(Parent)
driver.switch_to.window(child)
driver.maximize_window()
time.sleep(1)
driver.close()
driver.switch_to.window(Parent)

# switch tabs
time.sleep(1)
New_tab = driver.find_element(By.XPATH,"//a[@id='opentab']")
New_tab.click()

time.sleep(1)
driver.switch_to.window(Parent)
driver.switch_to.window(driver.window_handles[1])
driver.switch_to.window(driver.window_handles[0])

# Alert pop ups
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Aarav Mathur")
driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
alertwindow = driver.switch_to.alert
print(alertwindow.text)
alertwindow.accept()

# Table operations

NUMBER_OF_ROWS = len(driver.find_elements(By.XPATH,"//table[@class='table-display']/tbody/tr"))
NUMBER_OF_COLS = len(driver.find_elements(By.XPATH,"//table[@class='table-display']/tbody/tr/th"))

print("Number of coulumns",NUMBER_OF_COLS)

count = 0

for number_of_rows in range(2,NUMBER_OF_ROWS+1):
    count +=1
print("Number of rows",count)

# Printing table of content
Table_of_cont = driver.find_element(By.XPATH,"//table[@class='table-display']/tbody/tr[3]/td[2]")

for r in range(2,NUMBER_OF_ROWS+1):
    for c in range(1,NUMBER_OF_COLS+1):
        Table_of_cont = driver.find_element(By.XPATH,"//table[@class='table-display']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(Table_of_cont,end='   ')
        print()

# Hide and Show bars

Hide_button = driver.find_element(By.XPATH,"//input[@id='hide-textbox']")
Show_button = driver.find_element(By.XPATH,"//input[@id='show-textbox']")

Input_filed = driver.find_element(By.XPATH,"//input[@id='displayed-text']")

if Input_filed.is_displayed():
    Input_filed.send_keys("Aarav Mathur")
    print("Element was already displayed")
else:
    Show_button.click()
    Input_filed.send_keys("Aarav Mathur")
    print("Element was not displayed")

# Total amount sum of the table

Table_amount = driver.find_elements(By.XPATH,"//body[1]/div[3]/div[2]/fieldset[2]/div[1]/table[1]/tbody[1]/tr/td[4]")

total_sum = 0

for sum in Table_amount:
    amount = int(sum.text)
    total_sum += amount

print("The total amount is:",total_sum)

if total_sum == 296:
    print("The amount is perfect")
else:
    print("The amount is not perfect")

# Mouse Hover by Action chains
Mouse1 = driver.find_element(By.XPATH,"//button[@id='mousehover']")
Mouse2 = driver.find_element(By.XPATH,"//a[normalize-space()='Reload']")
time.sleep(1)

Action = ActionChains(driver)
Action.move_to_element(Mouse1).move_to_element(Mouse2).click().perform()

# Play with iframes

# driver.switch_to.frame("iframe-name")  // Check
# driver.find_element(By.XPATH,"//legend[normalize-space()='iFrame Example']").click()

# Links

all_links = driver.find_elements(By.TAG_NAME,"a")

links = 0

for link in all_links:
    url = link.get_attribute("href")
    try:
        res = requests.get(url)
    except:
        None
    if res.status_code >= 400:
        print("The url is broken",url)
        links += 1
    else:
        print("The url is not broken",url)

print("Total number of broken links",links)

input ("Press enter to close the browser")