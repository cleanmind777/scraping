from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # Import By for locating elements
from webdriver_manager.chrome import ChromeDriverManager
import time
# Set up the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the desired URL
driver.get("https://www.riocan.com/English/our-properties/leasing/all-properties/")

time.sleep(10)
# Find an element by its ID
element = driver.find_element(By.ID, "all-properties-container")  # Replace "your_element_id" with the actual ID
with open("riocan.txt", "w") as file:
            file.write("Response Text:\n")
            file.write(element.text) 
# Print the text or other attributes of the element
print(element)  # Example: Print the text content of the element

# Close the browser
driver.quit()