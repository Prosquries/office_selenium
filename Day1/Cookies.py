from XLUtils import *

serv_obj = Service()
driver = webdriver.Chrome(service = serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)

print("Printing all the cookies")
print("#######################################################################################")
Cookies = driver.get_cookies()
print(Cookies)
print("The length of the cookies",len(Cookies))
print(type(Cookies))

# Adding our own cookies
print("Adding our own cookie")
print("#######################################################################################")
driver.add_cookie({"name":"MyCokie","value":"123456"})
cookies = driver.get_cookies()
print(cookies)
print(len(cookies))

# If user wants to print only the name and values of the cookies
print()
print("print only name and value of the cookie")

print("#######################################################################################")
for cook in cookies:
    print(cook.get("name"),":",cook.get("value"))
print()

# Deleting our / specific cookie
driver.delete_cookie("MyCokie")
print("Deleting the cookie")

print("#######################################################################################")
cookies = driver.get_cookies()
print(cookies)
print(len(cookies))