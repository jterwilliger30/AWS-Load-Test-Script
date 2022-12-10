from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("chromedriver")

while True:
    driver.get("https://prod.indigo.fakeflickr.biz")
    driver.add_cookie({'name': '', 'value': ''})
    time.sleep(.15)

