import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/selectable/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.switch_to.frame(0)

actions = ActionChains(driver)
items = driver.find_elements(By.XPATH,"//li[@class='ui-widget-content ui-selectee']")

actions.click_and_hold(items[0]).move_to_element(items[3]).release().perform()
time.sleep(5)
