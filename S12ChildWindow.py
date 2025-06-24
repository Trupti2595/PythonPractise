from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.LINK_TEXT, "Click Here").click()

windowslist = driver.window_handles

driver.switch_to.window(windowslist[1])
newwindow = driver.find_element(By.TAG_NAME, "h3").text
print(newwindow)

driver.switch_to.window(windowslist[0])
oldwindow = driver.find_element(By.TAG_NAME, "h3").text
print(oldwindow)
