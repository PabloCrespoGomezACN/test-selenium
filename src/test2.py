from selenium import webdriver

options = webdriver.Chrome()
driver = webdriver.Remote(command_executor="http://localhost:4444", options=options)
driver.get("https://www.saucedemo.com/")
print(driver.title)
driver.quit()
