from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Replace these with your actual Google account credentials
email = "your-email@gmail.com"
password = "your-password"

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

try:
    # Open Google Chat login page
    driver.get("https://chat.google.com/")

    # Wait for the page to load
    time.sleep(2)

    # Enter the email
    email_input = driver.find_element(By.ID, "identifierId")
    email_input.send_keys(email)
    email_input.send_keys(Keys.RETURN)

    # Wait for the password input to appear
    time.sleep(2)

    # Enter the password
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    # Wait for the login process to complete
    time.sleep(5)

    # Now you are authenticated and can interact with Google Chat
    print("Logged in successfully!")

finally:
    # Close the WebDriver
    driver.quit()