import time

from selenium import webdriver
from selenium.webdriver.common.by import By
browsersortedveggies = []
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//div/table/thead/tr/th[1]").click()
veggielist = driver.find_elements(By.XPATH, '//td[1]')

for veggieslist in veggielist:
    browsersortedveggies.append(veggieslist.text)
originallist = browsersortedveggies.copy()
print(originallist)
print(browsersortedveggies)

browsersortedveggies.sort()

assert browsersortedveggies == originallist


time.sleep(3)