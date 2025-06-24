import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
name = "Rahul"
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()

time.sleep(2)