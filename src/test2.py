from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# Import the value of PARAM_APP_HOST_URL from hello.py
# from values import PARAM_APP_HOST_URL

print('TESTING STARTED')

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

# Create a Chrome WebDriver instance with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Use the Remote WebDriver to connect to the Selenium Grid Hub
# Make sure to replace "http://172.30.178.107:4444" with your actual hub URL
grid_url = "http://172.30.178.107:4444/grid/console"
driver = webdriver.Remote(command_executor=grid_url, options=chrome_options)

try:
    driver.get("https://www.saucedemo.com/")
    print(driver.title)
finally:
    driver.quit()
