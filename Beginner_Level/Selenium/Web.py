import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_web = Service()
driver = webdriver.Chrome(service=service_web)
driver.get("https://www.hyrtutorials.com")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[.='Selenium Practice']").click()
time.sleep(5)
driver.find_element(By.PARTIAL_LINK_TEXT, "XPath Practice").click()
time.sleep(5)

# alert = driver.switch_to.alert
# print(alert.text)
# alert.accept()
# alert.dismiss()

driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()
driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]").click()

time.sleep(5)

driver.find_element(By.CSS_SELECTOR, "")

