import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.ID,"alertBtn").click()

# Handle simple alert
alert = driver.switch_to.alert
alert.accept()

# Handle Comfirmation Alert
driver.find_element(By.ID, "confirmBtn").click()
time.sleep(3)
alert = driver.switch_to.alert
alert.dismiss()

#Handle Prompt alert
driver.find_element(By.ID, "promptBtn").click()
time.sleep(3)
alert = driver.switch_to.alert
alert.send_keys("Hello World")
alert.accept()


time.sleep(10)