import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)
#mobilename = "Blackberry"
driver.find_element(By.LINK_TEXT, "Shop").click()
driver.find_element(By.XPATH, "//app-card[4]/div/div/button").click()
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
name = driver.find_element(By.XPATH, "//div/h4/a").text
assert name == "Blackberry"
driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
driver.find_element(By.CSS_SELECTOR, "#country").send_keys("ind")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div/ul/li")))

countries = driver.find_elements(By.XPATH, "//div/ul/li")
for country in countries:
    if country.text == "India":
        country.click()
        break

driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR, ".btn-info").click()
driver.find_element(By.CLASS_NAME, "btn-lg").click()
print(driver.find_element(By.CSS_SELECTOR, ".alert-dismissible").text)

time.sleep(4)