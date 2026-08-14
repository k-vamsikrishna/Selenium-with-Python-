from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time

# 1. Common Pause Function

def pause():
    
# Pause execution for 2 seconds so each automation step can be observed clearly.

    time.sleep(2)


# 2. Download Folder Setup

download_folder = os.path.join(os.getcwd(), "downloads")

os.makedirs(download_folder, exist_ok=True)


# Remove old PDF files before starting the test
for file in os.listdir(download_folder):
    if file.lower().endswith(".pdf"):
        os.remove(os.path.join(download_folder, file))


# 3. Chrome Setup

options = webdriver.ChromeOptions()

options.add_experimental_option(
    "prefs",
    {
        # Disable Chrome password warnings
        "credentials_enable_service": False,
        "profile.password_manager_leak_detection": False,

        # PDF download settings
        "download.default_directory": download_folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
    }
)

driver = webdriver.Chrome(options=options)

driver.maximize_window()

# Explicit Wait - maximum 10 seconds
wait = WebDriverWait(driver, 10)


# 4. Open SauceDemo

driver.get("https://www.saucedemo.com/")

print("Website opened")

pause()


# 5. Login

username = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "user-name")
    )
)

username.send_keys("visual_user")

print("Username entered")

pause()


password = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "password")
    )
)

password.send_keys("secret_sauce")

print("Password entered")

pause()


login_button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "login-button")
    )
)

login_button.click()

print("Login button clicked")

pause()

print("Login successful")


# 6. Verify Products Page

products_title = wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "title")
    )
)

print("Page:", products_title.text)

assert products_title.text == "Products"

print("Products page displayed")

pause()


# 7. Add Product 1 - Backpack

backpack = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-backpack")
    )
)

backpack.click()

print("Backpack added")

pause()


# 8. Add Product 2 - Bike Light

bike_light = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-bike-light")
    )
)

bike_light.click()

print("Bike Light added")

pause()


# 9. Add Product 3 - Bolt T-Shirt

bolt_tshirt = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    )
)

bolt_tshirt.click()

print("Bolt T-Shirt added")

pause()


# 10. Verify Cart Badge

cart_badge = wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "shopping_cart_badge")
    )
)

print("Cart count:", cart_badge.text)

assert cart_badge.text == "3"

print("Three products successfully added")

pause()


# 11. Open Cart

cart = wait.until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME, "shopping_cart_link")
    )
)

cart.click()

print("Cart opened")

pause()


# 12. Verify Cart Contains 3 Products

cart_items = wait.until(
    EC.presence_of_all_elements_located(
        (By.CLASS_NAME, "cart_item")
    )
)

print("Number of cart items:", len(cart_items))

assert len(cart_items) == 3

print("Cart contains 3 products")

pause()


# 13. Click Checkout

checkout_button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "checkout")
    )
)

checkout_button.click()

print("Checkout button clicked")

pause()

print("Checkout page opened")


# 14. Enter Checkout Information

first_name = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "first-name")
    )
)

first_name.send_keys("Vamsi")

print("First name entered")

pause()


last_name = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "last-name")
    )
)

last_name.send_keys("Kowluri")

print("Last name entered")

pause()


postal_code = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "postal-code")
    )
)

postal_code.send_keys("500083")

print("Postal code entered")

pause()

print("Checkout information entered")


# 15. Click Continue

continue_button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "continue")
    )
)

continue_button.click()

print("Continue button clicked")

pause()


# 16. Verify Checkout Overview

overview_title = wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "title")
    )
)

print("Page:", overview_title.text)

assert overview_title.text == "Checkout: Overview"

print("Checkout overview displayed")

pause()


# 17. Verify 3 Products on Overview

checkout_items = wait.until(
    EC.presence_of_all_elements_located(
        (By.CLASS_NAME, "cart_item")
    )
)

print(
    "Products in checkout overview:",
    len(checkout_items)
)

assert len(checkout_items) == 3

print("Three products verified in checkout")

pause()


# 18. Click Finish

finish_button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "finish")
    )
)

finish_button.click()

print("Finish button clicked")

pause()


# 19. Verify Order Completed

confirmation = wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "complete-header")
    )
)

print("Confirmation:", confirmation.text)

assert confirmation.text == "Thank you for your order!"

print("====================================")
print("ORDER COMPLETED SUCCESSFULLY")
print("====================================")

pause()


# 20. Generate PDF Order

generate_pdf_button = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//button[contains(., 'Generate PDF order')]"
        )
    )
)

generate_pdf_button.click()

print("Generate PDF order clicked")

pause()


# 21. Wait for PDF Download

def pdf_downloaded(driver):
    """
    Returns True when a PDF file appears
    in the download folder.
    """

    pdf_files = [
        file
        for file in os.listdir(download_folder)
        if file.lower().endswith(".pdf")
    ]

    return len(pdf_files) > 0


wait.until(pdf_downloaded)

pause()


# 22. Verify PDF Download

pdf_files = [
    file
    for file in os.listdir(download_folder)
    if file.lower().endswith(".pdf")
]

assert pdf_files, "PDF was not downloaded"

pdf_file = pdf_files[0]

pdf_path = os.path.join(
    download_folder,
    pdf_file
)

print("====================================")
print("PDF DOWNLOADED SUCCESSFULLY")
print("====================================")

print("PDF file:", pdf_file)
print("PDF location:", pdf_path)

pause()


# 23. Test Completed

print("====================================")
print("TEST EXECUTION COMPLETED")
print("====================================")

input(
    "\nTest completed successfully. "
    "Browser will remain open.\n"
    "Press Enter to close the browser..."
)


# 24. Close Browser

driver.quit()

print("Browser closed")
