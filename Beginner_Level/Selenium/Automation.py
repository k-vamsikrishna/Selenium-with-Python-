import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service()
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
time.sleep(5)
driver.find_elements(By.XPATH,"//input[@value='radio1']")
