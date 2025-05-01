from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up the Chrome WebDriver with the correct path to the chromedriver executable
chrome_driver_path = r"C:\Users\KIIT\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"  # Replace with your actual path
service = Service(chrome_driver_path)
options = Options()

# Optionally, you can set headless mode if you don't want a browser window to open
# options.add_argument('--headless')

while True:
	# Prompt the user to enter the search term
	search_term = input("Enter the search term for Google: ")

	# Initialize the Chrome WebDriver
	driver = webdriver.Chrome(service=service, options=options)

	# Step 1: Open Google
	driver.get('https://www.google.com')

	# Step 2: Find the search input box using its name attribute
	search_box = driver.find_element('name', 'q')

	# Step 3: Enter the user-provided search term and submit it
	search_box.send_keys(search_term)
	search_box.send_keys(Keys.RETURN)  # Press Enter to submit the search

	# Step 4: Wait for a few seconds to allow the page to load
	time.sleep(2)

	# Step 5: Retrieve the titles of the first few search results
	search_results = driver.find_elements('css selector', 'h3')

	print(f"Top search results for '{search_term}':")
	for idx, result in enumerate(search_results[:5], start=1):
		print(f"{idx}. {result.text}")





