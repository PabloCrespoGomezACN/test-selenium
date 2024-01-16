from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
from values import APP_URL
from values import HOST_URL

def run_test():
    print('TESTING STARTED')

    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['platform'] = 'LINUX'

    HOST_URL = "https://app-{{ devops_namespace }}.apps.{{ ocp_cluster_name }}.acic-navan.com"
    # HOST_URL = "https://selenium-hub-client-dev-pgoa-devops-namespace.apps.ocpairbgdev1.acic-navan.com/ui"

    driver = webdriver.Remote(
        command_executor = HOST_URL
        # command_executor = "https://selenium-hub-client-dev-pgoa-devops-namespace.apps.ocpairbgdev1.acic-navan.com/ui"
    )
    
    driver.get(APP_URL)
    
    sleep(3)

    # Get page title
    title = driver.title

    # Test if title is correct
    assert 'Swag Labs' in title
    print(f'TEST 0: {title}\nTest passed')

    # Close the driver
    driver.quit()

# Run the test and handle success or failure
try:
    run_test()
    print('Testing was successful!')
# except AssertionError as e:
#    print(f'Testing failed: {str(e)}')
# except Exception as e:
#    print(f'An unexpected error occurred: {str(e)}')
