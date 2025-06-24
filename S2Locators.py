import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver1 = webdriver.Chrome()
driver1.get("https://rahulshettyacademy.com/angularpractice/")
driver1.maximize_window()

#Locators: ID, Xpath, CSSselector, ClassName, Name, LinkText
driver1.find_element(By.NAME, "email").send_keys('abc@gmail.com')
driver1.find_element(By.ID, 'exampleInputPassword1').send_keys('Test@1234')
driver1.find_element(By.ID, 'exampleCheck1').click()

#Static Dropdown
dropdown = Select(driver1.find_element(By.ID, 'exampleFormControlSelect1'))
dropdown.select_by_visible_text('Female')
dropdown.select_by_index(0)
#dropdown.select_by_value()

#CSSSelector syntax: tagname[attribute='value'] or #ID or .classname
driver1.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys('Trupti Bansod')
driver1.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()

#Xpath syntax: //tagname[@attribute= 'value']
driver1.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver1.find_element(By.CLASS_NAME, "alert").text
driver1.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello Again")
driver1.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

#print(message)
#assert "Succevdszfss!" in message


time.sleep(5)