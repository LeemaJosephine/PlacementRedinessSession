from selenium import webdriver

# Launch chrome browser
driver = webdriver.Chrome()

# Load the url
driver.get("https://www.google.com")

# Maximize the browser
driver.maximize_window()

# Adding implicit waits
driver.implicitly_wait(25)

# Get Title
title = driver.title
print("The title of the Webpage is" , title)

# Close the browser
driver.close()