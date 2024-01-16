from selenium import webdriver

print('TESTING STARTED')

# Specify the URL of the Selenium Grid Hub
grid_url = "http://172.30.226.167:4444/wd/hub"

# Create capabilities with browser version
capabilities = {
    "browserName": "chrome",
    "browserVersion": "latest",  # Specify the version you want to use
}

# Set up the WebDriver with the specified capabilities
driver = webdriver.Remote(command_executor=grid_url, desired_capabilities=capabilities)

try:
    driver.get("https://www.saucedemo.com/")
    print(driver.title)
finally:
    driver.quit()
