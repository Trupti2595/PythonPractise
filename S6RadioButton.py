import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

radiobutton = driver.find_elements(By.XPATH, '//input[@class="radioButton"]')
radiobutton[2].click()
assert radiobutton[2].is_selected()

driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()



time.sleep(2)