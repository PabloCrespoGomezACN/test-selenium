# src/test.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep



# Set options for not prompting DevTools information
# ___________
# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])

print("testing started")

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')


# No need to provide executable_path, Selenium will search in the system's PATH
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
sleep(3)

# Get page title
title = driver.title

# Test if title is correct
assert "Swag Labs" in title
print("TEST 0: `title` test passed")

# Close the driver
driver.quit()
