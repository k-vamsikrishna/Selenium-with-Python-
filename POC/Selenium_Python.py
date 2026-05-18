from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()
driver.implicitly_wait(5)

# Open the practice website
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# Print page title and URL (basic validation)
print(driver.title)
print(driver.current_url)

# Find all Radio buttons for selection
radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")

# Select first radio button and verify it is selected
radiobuttons[0].click()
assert radiobuttons[0].is_selected()

# Auto-Suggestion dropdown type 'ind' to trigger suggestions
driver.find_element(By.ID, 'autocomplete').send_keys('ind')


# Get all suggestion options
countries = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item-wrapper")

print(len(countries))  # print number of suggestions

# Select 'India' from suggestions
for country in countries:
    if country.text == 'India':
        country.click()
        break

# Select dropdown option2
driver.find_element(By.XPATH, "//option[@value='option2']").click()


# Get all checkboxes
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

# Select checkbox with value 'option3' and verify
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option3":
        checkbox.click()
        assert checkbox.is_selected()
        break

# Window handling click button to open new window
driver.find_element(By.ID, "openwindow").click()

# Store parent window
parent_window = driver.current_window_handle

# Switch to child window
for window in driver.window_handles:
    if window != parent_window:
        driver.switch_to.window(window)
        break

driver.maximize_window()

# Interact child window to find text input fields
elements = driver.find_elements(By.XPATH, "//input[@type='text']")

# Enter text 
if elements:
    ele = elements[0]
    ele.send_keys("Playwright with AI")
    driver.execute_script("arguments[0].scrollIntoView();", ele)
else:
    print("No input box found in new window")

# Click submit button
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Switch back to parent
driver.switch_to.window(parent_window)

# Open new tab
driver.find_element(By.XPATH, "//a[@class='btn-style class1 class2']").click()

# Switch to new tab
for window in driver.window_handles:
    if window != parent_window:
        driver.switch_to.window(window)
        break

# Close child tab
driver.close()

# Switch back to parent window
driver.switch_to.window(parent_window)

# ALERT HANDLING
driver.find_element(By.ID, 'name').send_keys('Vamsi Krishna')

# Click alert button
driver.find_element(By.ID, 'alertbtn').click()

# Switch to alert and accept it (click OK)
alert = driver.switch_to.alert
alert.accept()

# Navigate to the "Element Displayed Example" section on the page
text = driver.find_element(By.XPATH, "//legend[contains(.,'Web Table Example')]")
# Scroll to the section so it is visible on the screen
driver.execute_script("arguments[0].scrollIntoView();", text)
text.click()

# Enter a sample name into the input field, hide and show field
driver.find_element(By.CSS_SELECTOR, "input[id='displayed-text']").send_keys('Vamsi')
driver.find_element(By.XPATH, "//input[@class='btn-style class2']").click()
driver.find_element(By.CSS_SELECTOR, "input[value='Show']").click()
driver.quit()