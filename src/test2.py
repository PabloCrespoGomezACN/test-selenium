from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print('TESTING STARTED')

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

# Specify the URL of the Selenium Grid Hub
grid_url = "http://172.30.178.107:4444/wd/hub"

# Create capabilities with browser version
capabilities = {
    "browserName": "chrome",
    "browserVersion": "latest",  # Specify the version you want to use
}

# Create a Chrome WebDriver instance with the specified options
driver = webdriver.Chrome(options=chrome_options, desired_capabilities=capabilities)

# Use the Remote WebDriver to connect to the Selenium Grid Hub
driver = webdriver.Remote(command_executor=grid_url, options=chrome_options, desired_capabilities=capabilities)

try:
    driver.get("https://www.saucedemo.com/")
    print(driver.title)
finally:
    driver.quit()
