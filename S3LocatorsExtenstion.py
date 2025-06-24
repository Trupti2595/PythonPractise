import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver2 = webdriver.Chrome()
driver2.get("https://rahulshettyacademy.com/client")
driver2.find_element(By.LINK_TEXT, "Forgot password?").click()
driver2.find_element(By.XPATH, '//form/div[1]/input').send_keys("demo@gmail.com")
driver2.find_element(By.CSS_SELECTOR, 'form div:nth-child(2) input').send_keys("Hello@123")
driver2.find_element(By.ID, 'confirmPassword').send_keys("Hello@123")
driver2.find_element(By.XPATH, '//button[@type="submit"]').click()

time.sleep(2)