from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

driver = webdriver.Firefox()

# Open a webpage
driver.get('https://login.salesforce.com/')
try:
    element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
except:
    driver.quit()
elem = driver.find_element(By.NAME, "username")
elem.clear()
elem.send_keys("s.thapa19@wlv.ac.uk")
elem = driver.find_element(By.NAME, "pw")
elem.clear()
elem.send_keys("ambarkaar@2")
elem = driver.find_element(By.NAME, "Login")
elem.click()

try:
    element = WebDriverWait(driver, 120).until(
        EC.visibility_of_element_located((By.ID, "oneHeader"))
    )
except:
    driver.quit()

# Get the current HTML content
driver.get('https://wolverhamptonuniversity-dev-ed.develop.lightning.force.com/lightning/r/Contact/003J7000004MuH9IAK/view')
WebDriverWait(driver, 120).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@name='Edit']"))


# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'lxml')
tags = soup.find_all('div')
print(html_content)



driver.close()