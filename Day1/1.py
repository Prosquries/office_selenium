
from XLUtils import *

serv_obj = Service()

driver = webdriver.Chrome(service = serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Aarav")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("aarav2005@gmail.coom")

driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("1234567890")
driver.find_element(By.XPATH,"//textarea[@id='textarea']").send_keys("2 sector Mansarovar Jaipur")

driver.find_element(By.XPATH,"//input[@id='male']").click()

Weeks=driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for check in Weeks:
    get=check.get_attribute('id')
    if get == 'monday' or get == 'friday':
        check.click()

Dropdown = Select(driver.find_element(By.XPATH,"//select[@id='country']"))
Dropdown.select_by_visible_text("India") # Selecting country

dropdown_colours = Select(driver.find_element(By.XPATH,"//select[@id='colors']"))
dropdown_colours.select_by_visible_text("Blue")

dropdown_List = Select(driver.find_element(By.XPATH,"//select[@id='animals']"))
dropdown_List.select_by_visible_text("Dog")

# pop up window
driver.find_element(By.XPATH,"//button[@id='promptBtn']").click()

alertwindow = driver.switch_to.alert
print(alertwindow.text)

alertwindow.send_keys("My name is Aarav")
alertwindow.accept()

time.sleep(5)
driver.find_element(By.XPATH,"//button[@id='confirmBtn']").click()
AlertWindow = driver.switch_to.alert
print(AlertWindow.text)
AlertWindow.dismiss()

# Mouse Hover actions from actionchains
Mouse_1 = driver.find_element(By.XPATH,"//button[normalize-space()='Point Me']")
Mouse_2 = driver.find_element(By.XPATH,"//a[normalize-space()='Laptops']")

Action = ActionChains(driver)
Action.move_to_element(Mouse_1).move_to_element(Mouse_2).click().perform()

# Double click action from the actionchains
act = driver.find_element(By.XPATH,"/html[1]/body[1]/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[4]/div[3]/div[1]/aside[1]/div[1]/div[7]/div[1]/input[1]")
act.clear()
act.send_keys("My name is Aarav")
Mouse_3 = driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
Action1 = ActionChains(driver)
Action1.double_click(Mouse_3).perform()

# Drag and drop actions from the action chains
source=driver.find_element(By.XPATH,"//p[normalize-space()='Drag me to my target']")
target=driver.find_element(By.XPATH,"//div[@id='droppable']")
Action.click_and_hold(source).pause(0.5).move_to_element(target).pause(0.5).release().perform()

# Dynamic button
Button = driver.find_element(By.XPATH, "//button[contains(text(),'ST')]")
Button.click()
time.sleep(3)
Button.click()

# Day 2 Date Picker

month1 = "March"
Year1 = "2020"
Day1 = "18"
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

while True:
    mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yea = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon==month1 and yea==Year1:
        break;
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
        # driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
# Now setting up the date

Date = driver.find_elements(By.XPATH,"//a[@class='ui-state-default']")

for ele in Date:
    if ele.text==Day1:
        ele.click()
        break;

# Open date picker
driver.find_element(By.ID, "txtDate").click()

# Select Month
month = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
month.select_by_visible_text("Jun")

# Select Year
year = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
year.select_by_visible_text("2016")

# Select Date
dates = driver.find_elements(By.XPATH, "//a[@class='ui-state-default']")

for d in dates:
    if d.text == "8" and d.is_displayed():
        d.click()
        break;

driver.find_element(By.XPATH,"//input[@id='start-date']").send_keys("18/03/2005")
driver.find_element(By.XPATH,"//input[@id='end-date']").send_keys("18/03/2026")
driver.find_element(By.XPATH,"//button[@class='submit-btn']").click()

# Uploading the file but also using manual testing too
driver.find_element(By.ID, "singleFileInput").send_keys(r"D:\Aarav\Assighnment 3 week 2\Assignment 3 week 1.pdf")

driver.find_element(By.XPATH, "//button[normalize-space()='Upload Single File']").click()

# Uploading multiple files
driver.find_element(By.ID, "multipleFilesInput").send_keys(
    r"D:\Aarav\Assighnment 3 week 2\Assignment 3 week 1.pdf" + "\n" +
    r"D:\Aarav\Assighnment 3 week 2\Assignment 3 Week 2 part 1.postman_collection.json")

driver.find_element(By.XPATH,"//button[normalize-space()='Upload Multiple Files']").click()

# Pagination Web Table
pages = driver.find_elements(By.XPATH, "//ul[@class='pagination']//a")

for p in range(len(pages)):

    pages[p].click()

    price_elements = driver.find_elements(By.XPATH, "//tbody/tr/td[3][contains(text(),'$')]")
    checkboxes = driver.find_elements(By.XPATH, "//tbody/tr/td[4]/input")

    for i in range(len(price_elements)):
        price_text = price_elements[i].text
        price = float(price_text.replace("$", ""))

        if price >= 10:
                checkboxes[i].click()
                print(price_text)
# Laptop Links
print("Playing with the live links")

apple = driver.find_element(By.ID, "apple")
lenovo = driver.find_element(By.XPATH, "//a[@id='lenovo']")
Dell = driver.find_element(By.XPATH, "//a[@id='dell']")

# Open Apple in new tab
ActionChains(driver).key_down(Keys.CONTROL).click(apple).key_up(Keys.CONTROL).perform()

time.sleep(2)

# Open Lenovo in new tab
ActionChains(driver).key_down(Keys.CONTROL).click(lenovo).key_up(Keys.CONTROL).perform()

# Open Dell in  new tab
ActionChains(driver).key_down(Keys.CONTROL).click(Dell).key_up(Keys.CONTROL).perform()
time.sleep(3)

windowIds = driver.window_handles

parent = windowIds[0]
child = windowIds[1]
child2 = windowIds[2]
child3 = windowIds[3]

# Switch & print titles
time.sleep(1)
driver.switch_to.window(child)
print("Title of child:", driver.title)

time.sleep(1)
driver.switch_to.window(child2)
print("Title of child2:", driver.title)

time.sleep(1)
driver.switch_to.window(parent)
print("Title of parent:", driver.title)

time.sleep(1)
driver.switch_to.window(child3)
print("Title of child3",driver.title)


## Now with broken links
driver.switch_to.window(parent)
all_links=driver.find_elements(By.TAG_NAME,"a")

count=0

for link in all_links:
    url=link.get_attribute("href")
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        print(url,"is broken link")
        count+=1
    else:
        print(url,"Is the actual link")

print("The total number of broken link are",count)

# Play with tables

# Static web tables

# Number of rows and col
NoOfRows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
NoOfCol=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th"))

print(NoOfRows)
print(NoOfCol)

# Read specific row and col data
Table_content=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]").text

# Read all the rows and col data
print("Table_content")
for r in range(2,NoOfRows+1):
    for c in range(1,NoOfCol+1):
        Table_content = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
        print(Table_content,end='   ')
    print()

# Dynamic Table

# Number of Rows
NO_OF_ROWS =len( driver.find_elements(By.XPATH,"//table[@id = 'taskTable']/tbody[@id = 'rows']/tr"))
NO_OF_COL = len(driver.find_elements(By.XPATH,"//table[@id = 'taskTable']/thead/tr[@id = 'headers']/th"))

print("Number of rows",NO_OF_ROWS)
print("Number of coloumns",NO_OF_COL)

# Printing table of content and since this is dynamic table so the content will not be constant or static

TABLE_CONTENT = driver.find_element(By.XPATH,"//table[@id = 'taskTable']/tbody[@id = 'rows']/tr[4]/td[1]").text

# Read all the content of the dynamic table
print("Dynamic table content")
for j in range(1,NO_OF_ROWS+1):
    for k in range(1,NO_OF_COL):
        TABLE_CONTENT = driver.find_element(By.XPATH,"//table[@id = 'taskTable']/tbody[@id = 'rows']/tr["+str(j)+"]/td["+str(k)+"]").text
        print(TABLE_CONTENT,end='  ')
    print()

# Play with slider
Min_slider=driver.find_element(By.XPATH,"//div[@id='slider-range']//span[contains(@class,'ui-slider-handle')][1]")
Max_slider=driver.find_element(By.XPATH,"//div[@id='slider-range']//span[contains(@class,'ui-slider-handle')][2]")

print("The locations of the sliders Before")
print(Min_slider.location)
print(Max_slider.location)


Action = ActionChains(driver)
Action.drag_and_drop_by_offset(Min_slider,-87,0)
Action.drag_and_drop_by_offset(Max_slider,105,0)
Action.perform()

print("The locations of the sliders After")
print(Min_slider.location)
print(Max_slider.location)

# Scrolling Dropdown

# Click dropdown first
driver.find_element(By.ID, "comboBox").click()

wait = WebDriverWait(driver, 10)

dropdown = wait.until(
    EC.presence_of_element_located((By.ID, "dropdown"))
)

while True:
    try:
        item = driver.find_element(By.XPATH, "//div[text()='Item 180']")
        driver.execute_script("arguments[0].click();", item)
        break
    except:
        driver.execute_script("arguments[0].scrollTop += 100;", dropdown)

# Play with frames
print("The frame section is not present is the current web application so we use 'https://the-internet.herokuapp.com/nested_frames' in the another Frames.py file")

input("Enter to exit")