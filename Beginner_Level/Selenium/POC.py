import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://www.rahulshettyacademy.com/angularpractice/")
time.sleep(5)

driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys("Vamsi")
time.sleep(5)

driver.find_element(By.XPATH, "(//input[@name='email'])[1]").send_keys("vamsikowluri934@gmail.com")
time.sleep(5)

driver.find_element(By.ID,"exampleInputPassword1").send_keys("8977@Dad")
time.sleep(5)
