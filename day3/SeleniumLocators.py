from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch chrome browser
driver = webdriver.Chrome()

# Load the url
driver.get("https://testautomationpractice.blogspot.com/")

# Maximize the browser
driver.maximize_window()

# Adding implicit waits
driver.implicitly_wait(25)

# Using ID
driver.find_element(By.ID, "name").send_keys("testuser")

# class name
wikipedia_input = driver.find_element(By.CLASS_NAME, "wikipedia-search-input")
wikipedia_input.send_keys("AI")

# Using link text
driver.find_element(By.LINK_TEXT,"GUI Elements").click()

driver.back() # Go back

# Using partial link text
driver.find_element(By.PARTIAL_LINK_TEXT,"GUI Elem").click()

# Using name
driver.find_element(By.NAME,"start").click()

#Using Xpath -> Relative -> Attribute bases with Index based
driver.find_element(By.XPATH,"(//input[@class='form-control'])[1]").send_keys("usertest")

# Using text based xpath
text = driver.find_element(By.XPATH,"//h2[text()='Tabs']").text
print("The text captured is: " , text)

# Using contains based

driver.find_element(By.XPATH,"(//input[contains(@class,'form-cont')])[1]").send_keys("demouser")

# Using tagname
links = driver.find_elements(By.TAG_NAME,"a")
for link in links:
    print(link.get_attribute("href"))

# Using CSS Selector
driver.find_element(By.CSS_SELECTOR, "input[id='name']").send_keys("welcomeuser")



