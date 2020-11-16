from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(10) # seconds
driver.get("https://www.google.pl/maps")
element = driver.find_element_by_class_name('widget-minimap-shim-button')
element.screenshot('satelita.png')
driver.close()