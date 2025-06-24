import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)

vegetablelist = ["Cucumber - 1 Kg", "Capsicum"]
actuallist=[]
driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("cu")
time.sleep(2)
list = driver.find_elements(By.XPATH, "//div/div/div/h4")

for list1 in list:
    actuallist.append(list1.text)
print(actuallist)
assert vegetablelist == actuallist


