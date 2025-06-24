from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized") #chrome will open in maximize
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("headless")


driver = webdriver.Chrome(options = chrome_options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
print(driver.title)