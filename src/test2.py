from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Replace with the URL of your Selenium Grid Hub
grid_url = "https://selenium-hub-client-dev-pgoa-devops-namespace.apps.ocpairbgdev1.acic-navan.com/wd/hub"

# Create a dictionary of desired capabilities
desired_capabilities = {
    "browserName": "chrome",
    "version": "latest",
    "platform": "ANY",
    "name": "Your Test Name",
}

# Create a WebDriver instance pointing to the Grid
driver = webdriver.Remote(command_executor=grid_url, desired_capabilities=desired_capabilities)

try:
    # Navigate to your web app
    driver.get("https://www.saucedemo.com/")

    # Get page title
    title = driver.title

    # Test if title is correct
    assert 'Swag Labs' in title
    print(f'TEST 0: {title}\nTest passed')

finally:
    # Close the browser window
    driver.quit()
