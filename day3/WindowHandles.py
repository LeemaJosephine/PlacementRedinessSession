from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//button[text()='    click   ']").click()

main = driver.current_window_handle

handles = driver.window_handles

for handle in handles:
    if handle != main:
        driver.switch_to.window(handle)
        break

print(driver.title)