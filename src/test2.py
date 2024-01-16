from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print('TESTING STARTED')

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

# Specify the URL of the Selenium Grid Hub
grid_url = "http://172.30.226.167:4444/wd/hub"

# Create capabilities with browser version
capabilities = {
    "browserName": "chrome",
    "browserVersion": "latest",  # Specify the version you want to use
}

# Add desired capabilities to Chrome options
chrome_options.add_experimental_option("w3c", False)
chrome_options.add_experimental_option("capabilities", capabilities)

# Create a Chrome WebDriver instance with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Use the Remote WebDriver to connect to the Selenium Grid Hub
driver = webdriver.Remote(command_executor=grid_url, options=chrome_options)

try:
    driver.get("https://www.saucedemo.com/")
    print(driver.title)
finally:
    driver.quit()
