from XLUtils import *

def headless_chrome():
    serv_boj = Service()
    ops = webdriver.ChromeOptions()
    ops.add_argument('--headless')
    driver = webdriver.Chrome(options = ops , service = serv_boj)
    driver.implicitly_wait(10)
    return driver

def headless_edge():
    serv_boj = Service()
    ops = webdriver.EdgeOptions()
    ops.add_argument('--headless')
    driver = webdriver.Edge(options = ops , service = serv_boj)
    driver.implicitly_wait(10)
    return driver


driver = headless_edge()
driver.get("https://testautomationpractice.blogspot.com/#")
driver.maximize_window()

Tile=driver.title

if Tile == "Automation Testing Practice":
    print("Automation test successful")
else:
    print("Automation test failed")

# Headless mode - When we are sure the test will pass but we will run the raw test for the terminal outputs

