
from XLUtils import *
serv_obj = Service()
driver =  webdriver.Chrome(service = serv_obj)

driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.maximize_window()
driver.implicitly_wait(10)

driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-left")
print("Left:", driver.find_element(By.TAG_NAME, "body").text)

driver.switch_to.parent_frame()

driver.switch_to.frame("frame-middle")
print("Middle:",driver.find_element(By.TAG_NAME,"body").text)

driver.switch_to.parent_frame()

driver.switch_to.frame("frame-right")
print("Right:",driver.find_element(By.TAG_NAME,"body").text)

driver.switch_to.default_content()

driver.switch_to.frame("frame-bottom")
print("Bottom:",driver.find_element(By.TAG_NAME,"body").text)

print("Please press Enter to exit")