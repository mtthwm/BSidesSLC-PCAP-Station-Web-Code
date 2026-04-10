from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random

# --- Configuration ---
URL = "http://businesscorp.com/"
USERNAME = "admin"
PASSWORD = "commend-obsolete-bullhorn"
# ---------------------

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    while True:
        driver.get(URL)

        sleep(2)

        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        username_field.clear()
        username_field.send_keys(USERNAME)

        sleep(0.75)

        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(PASSWORD)

        sleep(1.3)

        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        sleep(10)

        # Click the logout button
        logout_btn = driver.find_element(By.CSS_SELECTOR, "a[href='/logout']")
        logout_btn.click()
        sleep(random.randint(2, 5))

finally:
    driver.quit()