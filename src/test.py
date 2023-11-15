from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# Set options for not prompting DevTools information
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

print("testing started")
# Provide the full path to the ChromeDriver executable
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=options)
driver.get("https://www.saucedemo.com/")
sleep(3)

# Get page title
title = driver.title

# Test if title is correct
assert "Swag Labs" in title
print("TEST 0: `title` test passed")

# Close the driver
driver.quit()
