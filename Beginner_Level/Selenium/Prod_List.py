import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
time.sleep(5)
