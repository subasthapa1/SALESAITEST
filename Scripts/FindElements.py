from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import time

# Load .env file
load_dotenv(r"..\Data\.env")

user_id = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")
print(password, user_id)

driver = webdriver.Firefox()

# Open login page
driver.get("https://login.salesforce.com/")

# Wait for username field
WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.ID, "username"))
)

# Login
driver.find_element(By.NAME, "username").send_keys(user_id)
driver.find_element(By.NAME, "pw").send_keys(password)
driver.find_element(By.NAME, "Login").click()

# Wait for Salesforce to load fully
WebDriverWait(driver, 120).until(
    EC.visibility_of_element_located((By.ID, "oneHeader"))
)

# Navigate to the record page
driver.get("https://wolverhamptonuniversity-dev-ed.develop.lightning.force.com/lightning/r/Contact/003J7000004MuH9IAK/view")

# Wait for the page to load (Edit button appears)
WebDriverWait(driver, 120).until(
    EC.visibility_of_element_located((By.XPATH, "//button[@name='Edit']"))
)

# Get the HTML
html_content = driver.page_source

# Parse with BeautifulSoup
soup = BeautifulSoup(html_content, "lxml")

# Example: print all div tags
tags = soup.find_all("div")
print(html_content)

driver.quit()
