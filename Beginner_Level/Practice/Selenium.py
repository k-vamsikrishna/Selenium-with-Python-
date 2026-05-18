import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
# action.double_click()
# action.context_click()
# action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()