from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# To run headless
options.add_argument('--headless')

# Browser Capabilities
options.add_argument('--incognito')
options.add_argument('--disable-notifications')

driver = webdriver.Chrome(options=options)
driver.get("https://testautomationpractice.blogspot.com/")
print(driver.title)