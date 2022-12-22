from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("chromedriver")
web_url = "PLACEHOLDER"
cookie = "insert cookie name"
val = "insert cookie value"

while True:
    driver.get(web_url)
    driver.add_cookie({'name': cookie, 'value': val})
    time.sleep(.15)

