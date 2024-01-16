from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

grid_url = "https://selenium-hub-client-dev-pgoa-devops-namespace.apps.ocpairbgdev1.acic-navan.com/wd/hub"
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['platform'] = "LINUX"

driver = webdriver.Remote(
    command_executor=grid_url,
    desired_capabilities=capabilities
)

# Your test script here

driver.quit()
