
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.maximize_window()
driver.implicitly_wait(3)

driver.find_element(By.TAG_NAME, "button").click()

#Explicit wait
wait = WebDriverWait(driver, 15)

element = wait.until(EC.visibility_of_element_located((By.XPATH,"//h4[text()='Hello World!']")))
print(element.text)

#Fluent wait
# wait = WebDriverWait(driver, 15,poll_frequency=2)
#
# element = wait.until(EC.visibility_of_element_located((By.XPATH,"//h4[text()='Hello World!']")))
# print(element.text)