from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.pl/maps")
# driver.find_element_by_class_name('widget-minimap-shim-button')  # wyjatek NoSuchElementException

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "widget-minimap-shim"))
)
element.screenshot('satelita.png')
driver.close()
