from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pickle
import time

def scrape_top_trends_from_X(driver):
    try:
        # Load cookies
        with open("cookies.pkl", "rb") as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                print('Cookies => ', cookies)
                driver.add_cookie(cookie)

        # Navigate to the trending page
        test = driver.get("https://x.com/home")
        # driver.get("https://x.com/explore/tabs/trending")
        time.sleep(10)

        # # Ensure the page has loaded
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//div[contains(@aria-label, "Timeline: Trending now")]'))
        # )

        # # Parse the page source with BeautifulSoup
        # soup = BeautifulSoup(driver.page_source, "html.parser")

        # # Locate the trending section container
        # trending_section = soup.find("div", attrs={"aria-label": "Timeline: Trending now"})

        # if not trending_section:
        #     raise Exception("Trending section not found.")
        
        # with open("debug_page_source.html", "w", encoding="utf-8") as file:
        #     file.write(driver.page_source)

        # # Extract all topic text from within the trending section
        # trends = []
        # for element in trending_section.find_all("span"):
        #     text = element.get_text(strip=True)
        #     if text:  # Ensure it's not empty
        #         trends.append(text)

        # # Deduplicate and limit to top 5 (if needed)
        # unique_trends = list(dict.fromkeys(trends))  # Removes duplicates while preserving order
        # top_trends = unique_trends[:5]

        # print("Top 5 trends:", top_trends)
        return test

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
