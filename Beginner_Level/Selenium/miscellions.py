import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

service_obj = Service()
driver = webdriver.Chrome(service=service_obj,options=chrome_options)
time.sleep(5)
driver.maximize_window()

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.get_screenshot_as_file("mis.png")
time.sleep(4)
