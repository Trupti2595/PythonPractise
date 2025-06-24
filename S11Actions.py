import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover")).perform()
actions.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()

time.sleep(3)