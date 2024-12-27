from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_to_X(username,password):
    try:
        # set up Chrome
        chrome_options = Options()

        # initialize webdriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        
        # navigate to login page
        driver.get("https://x.com/i/flow/login")
        time.sleep(5)

        # Find the username field and enter the username
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        username_field.send_keys(username)

        # Click the "Next" button
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Next"]'))
        )
        next_button.click()

        # Wait for the password field and enter the password
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_field.send_keys(password)

        # Click the "Log in" button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Log in"]'))
        )
        login_button.click()

        current_url = driver.current_url
        print("Logged in succesfully", current_url)

        # return the url
        return driver
    
    except Exception as e:
        print(f"An error occured during login: {e}")
        if driver:
            driver.quit()  # Close if an error occurs
        return None