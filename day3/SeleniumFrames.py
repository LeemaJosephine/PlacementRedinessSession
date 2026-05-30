import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.implicitly_wait(10)

# switch to frame using id or name

driver.switch_to.frame("singleframe")

driver.find_element(By.TAG_NAME,"input").send_keys("Hello")

driver.switch_to.default_content()

driver.find_element(By.LINK_TEXT,"Iframe with in an Iframe").click()

# Nested frames

parent_frame= driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
# switch to the parent frame
driver.switch_to.frame(parent_frame)

chile_frame = driver.find_element(By.XPATH,"//h5[text()='Nested iFrames']/following::iframe")
# switch to child frame
driver.switch_to.frame(chile_frame)

driver.find_element(By.TAG_NAME,"input").send_keys("Hello")

time.sleep(10)