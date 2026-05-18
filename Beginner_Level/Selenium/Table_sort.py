import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browerSortedVeggies = []
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/offers")

time.sleep(5)
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggiesWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")

for ele in veggiesWebElements:
    browerSortedVeggies.append(ele.text)

time.sleep(5)
orginalBrowerSortedList = browerSortedVeggies.copy()
browerSortedVeggies.sort()
assert browerSortedVeggies == orginalBrowerSortedList
