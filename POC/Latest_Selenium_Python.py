from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from array import array

# 1. Variables and Data Types

name = "Vamsi Krishna"
age = 30
experience = 4
is_qa_engineer = True

print("Name:", name)
print("Age:", age)
print("Experience:", experience)
print("QA Engineer:", is_qa_engineer)

# 2. Print and Input

print("\n--- Print and Input ---")

user_name = input("Enter your name: ")
print("Welcome:", user_name)

print("Starting Selenium Automation POC...")

# 3. Basic Operators

print("\n--- Basic Operators ---")

a = 20
b = 10

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Power:", a ** 2)

# 4. Comments

# This is a single-line comment.
"""
This is a multi-line comment.It explains the purpose of the code block.
"""

# 5. Conditional Statements - if / else

print("\n--- If Else ---")

if age >= 18:
    print("User is an adult")
else:
    print("User is a minor")

# 6. Conditional Statement - elif

print("\n--- If Elif Else ---")

if experience < 2:
    print("Beginner")
elif experience < 5:
    print("Intermediate")
else:
    print("Experienced")

# 7. Lists

print("\n--- Lists ---")

browsers = ["Chrome", "Firefox", "Edge"]

print("Browsers:", browsers)
print("First Browser:", browsers[0])

browsers.append("Safari")
print("After Append:", browsers)

browsers.remove("Firefox")
print("After Remove:", browsers)

# 8. Dictionaries

print("\n--- Dictionary ---")

user_details = {
    "name": "Vamsi Krishna",
    "role": "QA Engineer",
    "experience": 4
}

print("User Name:", user_details["name"])
print("Role:", user_details["role"])

user_details["skill"] = "Selenium with Python"

print("User Details:", user_details)

# 9. Tuples

print("\n--- Tuple ---")

browser_details = ("Chrome", "Windows", "Python")

print("Browser:", browser_details[0])
print("OS:", browser_details[1])
print("Language:", browser_details[2])

# 10. Sets

print("\n--- Set ---")

skills = {"Selenium", "Python", "API", "SQL", "Python"}

print("Skills:", skills)

# 11. Nested Lists and Dictionaries

print("\n--- Nested List ---")

test_cases = [
    ["TC001", "Login Test", "Pass"],
    ["TC002", "Search Test", "Pass"],
    ["TC003", "Logout Test", "Fail"]
]

for test_case in test_cases:
    print(
        "Test ID:", test_case[0],
        "| Test Name:", test_case[1],
        "| Status:", test_case[2]
    )

print("\n--- Nested Dictionary ---")

employee = {
    "name": "Vamsi",
    "details": {
        "role": "QA Engineer",
        "experience": 5,
        "skills": ["Python", "Selenium", "SQL"]
    }
}

print("Employee Name:", employee["name"])
print("Role:", employee["details"]["role"])
print("Skills:", employee["details"]["skills"])

# 12. Basic String Operations

print("\n--- String Operations ---")

message = "Selenium Automation with Python"

print("Original:", message)
print("Upper:", message.upper())
print("Lower:", message.lower())
print("Length:", len(message))
print("Replace:", message.replace("Python", "AI"))
print("Contains Selenium:", "Selenium" in message)

words = message.split(" ")
print("Split:", words)

# 13. Defining Functions

def print_test_information():
    print("\nExecuting Selenium Automation Test")

print_test_information()

# 14. Function Parameters and Return Values

def add_numbers(number1, number2):
    return number1 + number2

result = add_numbers(10, 20)

print("Function Result:", result)

def get_test_status(status):
    return "Test Status: " + status

print(get_test_status("PASS"))

# 15. Scope and Lifetime of Variables

global_variable = "Global Variable"

def scope_example():
    local_variable = "Local Variable"

    print("Inside Function:", global_variable)
    print("Inside Function:", local_variable)

scope_example()

print("Outside Function:", global_variable)

# 16. Handling Errors - try / except / finally

print("\n--- Exception Handling ---")

try:
    number = int("100")
    print("Converted Number:", number)

except ValueError:
    print("Invalid number format")

finally:
    print("Exception handling block completed")

# 17. Common Exceptions

print("\n--- Common Exceptions ---")

# ValueError

try:
    value = int("ABC")

except ValueError:
    print("ValueError handled: ABC cannot be converted to integer")

# IndexError

try:
    numbers = [10, 20, 30]
    print(numbers[5])

except IndexError:
    print("IndexError handled: Index does not exist")

# 18. Arrays

print("\n--- Array ---")

numbers_array = array('i', [10, 20, 30, 40])

numbers_array.append(50)

for number in numbers_array:
    print("Array Value:", number)

# 19. Loops - for loop

print("\n--- For Loop ---")

for browser in browsers:
    print("Browser:", browser)

# 20. Loops - while loop

print("\n--- While Loop ---")

counter = 1

while counter <= 3:
    print("Counter:", counter)
    counter += 1

# 21. Break Statement

print("\n--- Break Statement ---")

for number in range(1, 6):

    if number == 4:
        break

    print("Number:", number)

# 22. Continue Statement

print("\n--- Continue Statement ---")

for number in range(1, 6):

    if number == 3:
        continue

    print("Number:", number)

# 23. Selenium WebDriver Setup

print("\nStarting Selenium Automation")

driver = webdriver.Chrome()

try:

    # Open Practice Website

    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()

    # Print Page Title and URL

    print("\nPage Title:", driver.title)
    print("Current URL:", driver.current_url)

    assert "Practice" in driver.title

    # Radio Button Selection

    print("\n--- Radio Button Test ---")

    radio_buttons = driver.find_elements(By.CSS_SELECTOR,".radioButton")

    for index, radio_button in enumerate(radio_buttons):

        print("Radio Button", index + 1)

        if index == 0:
            radio_button.click()

            if radio_button.is_selected():
                print("First radio button selected successfully")

    # Auto Suggestion Dropdown

    print("\n--- Auto Suggestion Test ---")

    autocomplete = driver.find_element(By.ID,"autocomplete")

    autocomplete.send_keys("ind")

    time.sleep(2)

    countries = driver.find_elements(By.CSS_SELECTOR,".ui-menu-item-wrapper")

    print("Number of Suggestions:", len(countries))

    country_found = False

    for country in countries:

        print("Suggestion:", country.text)

        if country.text == "India":
            country.click()
            country_found = True
            break

    if country_found:
        print("India selected successfully")
    else:
        print("India was not found")

    # Dropdown Selection

    print("\n--- Dropdown Test ---")

    dropdown_option = driver.find_element(By.XPATH,"//option[@value='option2']")

    dropdown_option.click()

    print("Option 2 selected successfully")

    # Checkbox Selection

    print("\n--- Checkbox Test ---")

    checkboxes = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")

    for checkbox in checkboxes:

        checkbox_value = checkbox.get_attribute("value")

        if checkbox_value == "option3":

            checkbox.click()

            if checkbox.is_selected():
                print("Option 3 checkbox selected successfully")

            break

    # Window Handling

    print("\n--- Window Handling ---")

    parent_window = driver.current_window_handle

    driver.find_element(By.ID,"openwindow").click()

    time.sleep(2)

    for window in driver.window_handles:

        if window != parent_window:
            driver.switch_to.window(window)
            break

    print("Switched to child window")

    driver.maximize_window()

    time.sleep(2)

    # Interact with Child Window

    elements = driver.find_elements(By.XPATH,"//input[@type='text']")

    if elements:

        element = elements[0]

        element.send_keys("Playwright with AI")

        driver.execute_script("arguments[0].scrollIntoView();",element)

        print("Text entered successfully")

    else:

        print("No text input found")

    # Submit Button

    try:

        submit_button = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")

        submit_button.click()

        print("Submit button clicked")

    except Exception as e:

        print("Submit button was not available:", e)

    # Switch Back to Parent Window

    driver.switch_to.window(parent_window)

    print("Switched back to parent window")

    # Open New Tab

    driver.find_element(By.XPATH,"//a[@class='btn-style class1 class2']").click()

    time.sleep(2)

    # Switch to New Tab

    for window in driver.window_handles:

        if window != parent_window:

            driver.switch_to.window(window)

            print("Switched to new tab")

            break

    # Close Child Tab

    driver.close()

    print("Child tab closed")

    # Switch Back to Parent

    driver.switch_to.window(parent_window)

    print("Returned to parent window")

    # Alert Handling

    print("\n--- Alert Handling ---")

    name_field = driver.find_element(By.ID,"name")

    name_field.send_keys(name)

    driver.find_element(By.ID,"alertbtn").click()

    time.sleep(1)

    alert = driver.switch_to.alert

    print("Alert Message:", alert.text)

    alert.accept()

    print("Alert accepted successfully")

    # Element Displayed Example

    print("\n--- Element Displayed Example ---")

    text_section = driver.find_element(By.XPATH,"//legend[contains(.,'Element Displayed Example')]")

    driver.execute_script("arguments[0].scrollIntoView();",text_section)

    text_section.click()

    # Enter Text

    displayed_text = driver.find_element(By.CSS_SELECTOR,"input[id='displayed-text']")

    displayed_text.send_keys("Vamsi")

    print("Text entered successfully")

    # Hide Element

    hide_button = driver.find_element(By.XPATH,"//input[@class='btn-style class2']")

    hide_button.click()

    print("Text field hidden")

    # Show Element

    show_button = driver.find_element(By.CSS_SELECTOR,"input[value='Show']")

    show_button.click()

    print("Text field displayed again")

    # Final Validation

    assert displayed_text.is_displayed()

    print("\nPOC EXECUTION COMPLETED SUCCESSFULLY")

except Exception as e:

    print("\nSelenium Test Failed")
    print("Error:", e)

finally:

    time.sleep(2)

    driver.quit()

    print("\nBrowser closed successfully")