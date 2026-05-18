import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

name = 'Vamsi'
x = 5
email_id = 'hello@gmail.com'
password = '123456'

driver.get("https://www.rahulshettyacademy.com/angularpractice/")

time.sleep(x)

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys(name)
driver.find_element(By.NAME, "email").send_keys(email_id)
driver.find_element(By.ID, "exampleInputPassword1").send_keys(password)
time.sleep(x)

drop_down = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
drop_down.select_by_index(1)

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert "Success" in message

driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys(name)

driver.find_element(By.PARTIAL_LINK_TEXT, "Shop").click()
time.sleep(x)

Products = ["iphone X", "Samsung Note 8", "Nokia Edge", "Blackberry"]

if Products[3] == 'Blackberry':
    driver.find_element(By.XPATH, "(//button[@class='btn btn-info'])[3]").click()
    driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()
    time.sleep(x)
    driver.find_element(By.XPATH, "//button[@class='btn btn-danger']").click()
    driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
    time.sleep(x)
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    driver.find_element(By.CSS_SELECTOR, "input[class$='btn btn-success btn-lg']").click()
    time.sleep(x)
    driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").click()
    message = driver.find_element(By.CLASS_NAME, "alert-success").text
    print(message)

else:
    driver.find_element(By.XPATH, "(//button[@class='btn btn-info'])[3]").click()
    driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()
    time.sleep(x)

