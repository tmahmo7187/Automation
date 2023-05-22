from selenium import webdriver  # Library for automating web browsers
from selenium.webdriver.chrome.options import Options  # Class for configuring Chrome options
from selenium.webdriver.common.by import By  # Enum for locating elements using different strategies
from selenium.webdriver.support.ui import WebDriverWait  # Class for implementing waits
from selenium.webdriver.support import expected_conditions as EC  # Class for defining expected conditions
from datetime import datetime  # Module for working with dates and times
import time  # Module for adding delays in the script

# Path to your ChromeDriver executable
webdriver_path = "path/to/chromedriver"

# WhatsApp group name and message
group_name = "KCC cricket"
message = "Please join KCC cricket on every Sunday at 8 AM"

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode without opening a browser window

# Launch the browser
driver = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)

# Access WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Wait for QR code scan
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-ref]")))

# Wait for user to scan the QR code
WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='main']")))

# Find the group by name
search_input = driver.find_element_by_xpath("//div[@role='button'][@title='Search or start new chat']")
search_input.click()
search_input.send_keys(group_name)
time.sleep(2)  # Add a small delay for search results to populate

group_element = driver.find_element_by_xpath(f"//span[@title='{group_name}']")
group_element.click()

# Wait for the chat to load,.until() is a method provided by the WebDriverWait class in Selenium. It is used to wait for a specific condition to be met before proceeding with the script execution.
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-tab='6']")))

# Get the current day and time
current_day = datetime.now().strftime("%A")
current_time = datetime.now().strftime("%H:%M")

# Check if it's Wednesday and 9 AM
if current_day.lower() == "wednesday" and current_time == "09:00":
    # Find the input field and send the message
    input_field = driver.find_element_by_xpath("//div[@contenteditable='true'][@data-tab='6']")
    input_field.send_keys(message)
    input_field.send_keys(Keys.RETURN)

# Close the browser
driver.quit()
