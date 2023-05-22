from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

# Path to your WebDriver executable
webdriver_path = "path/to/chromedriver"

# LinkedIn credentials
username = "your_username"
password = "your_password"

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode without opening a browser window

# Pushover credentials
pushover_user_token = "your_pushover_user_token"
pushover_app_token = "your_pushover_app_token"

# Launch the browser
driver = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)

# Access LinkedIn and log in
driver.get("https://www.linkedin.com/")
driver.find_element_by_id("session_key").send_keys(username)  # Locate the input field for the username and enter the value
driver.find_element_by_id("session_password").send_keys(password)  # Locate the input field for the password and enter the value
driver.find_element_by_xpath('//button[text()="Sign in"]').click()  # Locate the "Sign in" button and click it

# Wait for the homepage to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "feed-tab-icon")))

# Go to Jobs
driver.get("https://www.linkedin.com/jobs/")

# Perform a search for remote QA jobs
search_input = driver.find_element_by_xpath('//input[contains(@placeholder, "Search jobs")]')  # Locate the search input field
search_input.clear()  # Clear any existing text in the search input field
search_input.send_keys("Remote QA")  # Enter the search query "Remote QA" in the search input field
search_input.send_keys(Keys.RETURN)  # Press Enter to perform the search

# Wait for job results to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results__list")))

# Check if there are new job listings
new_jobs = driver.find_elements_by_xpath('//span[contains(@class, "jobs-search-results__new-job-indicator")]')

if new_jobs:
    # Send a push notification
    message = "New remote QA jobs available!"
    payload = {
        "token": pushover_app_token,
        "user": pushover_user_token,
        "message": message
    }
    requests.post("https://api.pushover.net/1/messages.json", data=payload)

# Close the browser
driver.quit()
