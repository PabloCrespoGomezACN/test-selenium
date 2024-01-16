from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# Import the value of PARAM_APP_HOST_URL from hello.py
# from values import PARAM_APP_HOST_URL

print('TESTING STARTED')

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

# No need to provide executable_path, Selenium will search in the system's PATH
# driver = webdriver.Chrome(options=options)

options = webdriver.Chrome()
driver = webdriver.Remote(command_executor="http://localhost:4444", options=options)
driver.get("https://www.saucedemo.com/")
print(driver.title)
driver.quit()
