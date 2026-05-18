from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\Vamsi Kowluri\\PycharmProjects\\SeleniumPython\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# locators -  id, name, cssselector, xpath, Classname, linktext

driver.find_element(By.NAME, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//input[@id='login-button']").click()
driver.implicitly_wait(10)
driver.close()
