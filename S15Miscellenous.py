import time

from selenium import webdriver

#head mode: whatever actions performed can be visible
#headless mode: all the actions will be in backend, not a single action can be visible
chrom_options = webdriver.ChromeOptions()
chrom_options.add_argument("headless")
chrom_options.add_argument("--ignore-certificate-error") #to gnore the pages like not trustable site or anything like this


driver = webdriver.Chrome(options = chrom_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

#driver.execute_script("window.scroll(0,500)") #to scroll little bit down
driver.execute_script("window.scroll(0,document.body.scrollHeight)") #to scroll all the way down
driver.get_screenshot_as_file("screen.png")
time.sleep(2)