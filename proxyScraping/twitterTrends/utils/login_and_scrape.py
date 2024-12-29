from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import random
import pickle

def login_and_scrape(username,password):
    try:
        # Random delay for human-like behavior
        random_wait_time = random.randint(5,10)
        
        # Set up Chrome options
        chrome_options = Options()

        # initialize webdriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        
        # Step 1: Navigate to login page
        print("Navigating to login page...")
        driver.get("https://x.com/i/flow/login")
        time.sleep(random_wait_time)

        # Step 2: Enter username and password
        # :: username ::
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        username_field.send_keys(username)
        print("Entered Username")

        # Click the "Next" button
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Next"]'))
        )
        time.sleep(random_wait_time)
        next_button.click()
        print("clicked next button")
        time.sleep(random_wait_time)

        # :: passowrd ::
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_field.send_keys(password)
        print("Entered Password")

        # Click the "Log in" button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Log in"]'))
        )
        time.sleep(random_wait_time)
        login_button.click()
        print("Logged In")

        # Step 3: Save cookies
        with open("cookies.pkl", "wb") as file:
            pickle.dump(driver.get_cookies(), file)
        print("Cookies saved successfully!")

        with open("cookies.pkl", "rb") as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                print('Cookies => ', cookies)
                driver.add_cookie(cookie)

        # Step 4: Navigate to homepage
        print("Navigating to homepage...")
        driver.get("https://x.com/home")
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@data-testid="SearchBox_Search_Input"]'))
        )
        time.sleep(random_wait_time)

        # Step 5: Print a random heading or element
        print("Checking homepage content...")
        search_box.send_keys('rabi')
        print(f"Filled search box with: {'rabi'}")
        time.sleep(random_wait_time)
        
        return {
            search_box
        }

    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        if 'driver' in locals() and driver:
            driver.quit()
