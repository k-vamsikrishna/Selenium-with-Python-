from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open browser
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

print(driver.title)
print(driver.current_url)

# WAIT OBJECT (used instead of sleep)
wait = WebDriverWait(driver, 10)

# ---------------- RADIO BUTTON ----------------
radio = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radio[0].click()
assert radio[0].is_selected()

# ---------------- AUTO SUGGEST ----------------
driver.find_element(By.ID, "autocomplete").send_keys("ind")

countries = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ui-menu-item-wrapper"))
)

for country in countries:
    if country.text == "India":
        country.click()
        break

# ---------------- DROPDOWN ----------------
driver.find_element(By.XPATH, "//option[@value='option2']").click()

# ---------------- CHECKBOX ----------------
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

for box in checkboxes:
    if box.get_attribute("value") == "option3":
        box.click()
        assert box.is_selected()
        break

# ---------------- WINDOW HANDLING ----------------
parent = driver.current_window_handle

driver.find_element(By.ID, "openwindow").click()

wait.until(lambda d: len(d.window_handles) > 1)

for handle in driver.window_handles:
    if handle != parent:
        driver.switch_to.window(handle)
        break

driver.maximize_window()

# ENTER TEXT IN NEW WINDOW
wait.until(EC.presence_of_element_located((By.ID, "name"))).send_keys(
    "Vamsi krishna Kowluri"
)

# CLOSE BROWSER
driver.quit()