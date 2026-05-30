from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

# Using Select class

country = driver.find_element(By.ID, "country")

sle = Select(country)
sle.select_by_value("usa")
sle.select_by_index(2) #index starts from 0
sle.select_by_visible_text("")
