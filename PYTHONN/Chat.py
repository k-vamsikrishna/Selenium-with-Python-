from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

print(driver.title)
print(driver.current_url)

# RADIO BUTTONS
radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

# AUTOSUGGEST
driver.find_element(By.ID, 'autocomplete').send_keys('ind')
time.sleep(5)

countries = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item-wrapper")

for country in countries:
    if country.text == 'India':
        country.click()
        break

# DROPDOWN
driver.find_element(By.XPATH, "//option[@value='option2']").click()

# CHECKBOX
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

time.sleep(5)

# WINDOW HANDLING
driver.find_element(By.ID, "openwindow").click()
time.sleep(5)

parent_window = driver.current_window_handle

for window in driver.window_handles:
    if window != parent_window:
        driver.switch_to.window(window)
        break

driver.maximize_window()
time.sleep(5)

ele = driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Playwright with AI")
time.sleep(5)
driver.execute_script("arguments[0].scrollIntoView();", ele)

time.sleep(5)

driver.quit()