import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkbox = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
print(len(checkbox))

for check in checkbox:
    if check.get_attribute("value") == 'option1':
        #check.click()
        assert check.is_selected()
        break

time.sleep(2)