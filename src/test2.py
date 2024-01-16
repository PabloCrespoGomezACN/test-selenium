from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Specify the URL of the Selenium Hub
hub_url = "http://172.30.226.167:4444"

# Specify the desired capabilities for the browser (e.g., Chrome)
desired_capabilities = DesiredCapabilities.CHROME.copy()

# Create a WebDriver instance pointing to the Selenium Hub
driver = webdriver.Remote(command_executor=hub_url, options=webdriver.ChromeOptions())

# Now, you can use 'driver' to interact with the Selenium Grid
# For example:
driver.get("https://www.saucedemo.com/")
print(driver.title)

# Close the WebDriver session
driver.quit()
