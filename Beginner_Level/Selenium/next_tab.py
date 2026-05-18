import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,document.boby.scrollHeight)")
time.sleep(5)
