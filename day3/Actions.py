import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

actions = ActionChains(driver)

# Scroll until element is Visible

point_me = driver.find_element(By.XPATH,"//button[text()='Point Me']")
driver.execute_script("arguments[0].scrollIntoView();", point_me)

# Mouse Hover
actions.move_to_element(point_me).perform()

# Double click
copy_text = driver.find_element(By.XPATH,"//button[text()='Copy Text']")
actions.double_click(copy_text).perform()

# Drag and drop
source = driver.find_element(By.ID,"draggable")
dest = driver.find_element(By.ID,"droppable")

actions.drag_and_drop(source, dest).perform()

# Right Click
actions.context_click().perform()



time.sleep(5)