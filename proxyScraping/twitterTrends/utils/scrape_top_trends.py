from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time

def scrape_top_trends_from_X(driver):
    try:
        # Load cookies for session persistence
        try:
            with open("cookies.pkl", "rb") as file:
                cookies = pickle.load(file)
                for cookie in cookies:
                    driver.add_cookie(cookie)
        except FileNotFoundError:
            print("Cookies file not found. Make sure to log in and save cookies first.")

        # Open trending page
        driver.get("https://x.com/explore/tabs/trending")
        
        # Wait for the page to load and ensure you're logged in
        time.sleep(5)  # Optional: allow page animations to settle
        
        # Ensure login status
        if "login" in driver.current_url or "signup" in driver.page_source:
            raise Exception("Not logged in. Please ensure cookies are loaded correctly.")

        # Wait for the trending elements to load
        WebDriverWait(driver, 50).until(
            EC.presence_of_all_elements_located((By.XPATH, '//span[contains(text(), "#")]'))
        )

        # Locate trend elements
        trend_elements = driver.find_elements(By.XPATH, '//span[contains(text(), "#")]')

        # Extract text for each trend (limit to top 5)
        top_trends = []
        for trend in trend_elements[:5]:
            # Extract visible text
            trend_text = trend.text.strip()
            if trend_text:
                top_trends.append(trend_text)

        print("Top 5 trends:", top_trends)
        return top_trends

    except Exception as e:
        print(f"An error occurred: {e}")
        return None