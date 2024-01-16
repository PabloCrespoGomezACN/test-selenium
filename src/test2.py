from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
from values import APP_URL

def run_test():
    print('TESTING STARTED')

    capabilities = {
        'browserName': 'chrome',
        'platform': 'LINUX',
        'goog:chromeOptions': {
            'args': ['--headless', '--disable-gpu', '--no-sandbox']
        }
    }

    grid_url = "https://app-{{ devops_namespace }}.apps.{{ ocp_cluster_name }}.acic-navan.com/wd/hub"

    driver = webdriver.Remote(
        command_executor=grid_url,
        desired_capabilities=capabilities
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
except AssertionError as e:
    print(f'Testing failed: {str(e)}')
except Exception as e:
    print(f'An unexpected error occurred: {str(e)}')
