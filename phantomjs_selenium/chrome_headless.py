from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = "/usr/sbin/chromium"
options.add_argument("headless")
options.add_argument("window-size=1200x600")
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://lovesun.xyz')
print(driver.title)
driver.get_screenshot_as_file('main-page.png')
driver.close()
