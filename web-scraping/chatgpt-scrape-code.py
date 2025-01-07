import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Setup Selenium WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is in your PATH or provide its location
url = "https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Hyderabad&category=B&parameter=rel&hideviewed=N&ListingsType=I&filterCount=3&incSrc=Y&fromSrc=homeSrc"
driver.get(url)

# Initialize an empty list to store property data
properties = []

# Scroll and scrape data
SCROLL_PAUSE_TIME = 3
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)  # Wait for new data to load

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    # Find all property cards
    cards = soup.find_all("div", class_="mb-srp__card__summary")
    
    # Extract data from each card
    for card in cards:
        try:
            title = card.find_previous("h2", class_="mb-srp__card--title").get("title")
            details = card.find_all("div", class_="mb-srp__card__summary__list--item")
            
            # Extract specific details
            property_data = {"Title": title}
            for detail in details:
                label = detail.find("div", class_="mb-srp__card__summary--label").get_text(strip=True)
                value = detail.find("div", class_="mb-srp__card__summary--value").get_text(strip=True)
                property_data[label] = value
            
            properties.append(property_data)
        except AttributeError:
            continue  # Skip if any detail is missing

    # Check if we've reached the bottom of the page
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Close the WebDriver
driver.quit()

# Save data to a Pandas DataFrame
df = pd.DataFrame(properties)
df.to_csv("magicbricks_data.csv", index=False)

print("Scraping completed. Data saved to 'magicbricks_data.csv'.")
