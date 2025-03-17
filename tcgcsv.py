from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    # Initialize the WebDriver
    driver = webdriver.Chrome()

    # Open the webpage
    driver.get('https://tcgcsv.com/')

    # Wait for page to load
    wait = WebDriverWait(driver, 10)

    # Click elements with error handling
    for text in ['Magic (419)', 'Pokemon (201)', 'Pokemon Japan (417)']:
        try:
            # Wait for element to be clickable
            element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//summary[text()='{text}']")))

            # Scroll element into view with more reliable method
            driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", element)
            time.sleep(0.5)  # Small delay after scrolling

            # Click using JavaScript to avoid move target out of bounds
            driver.execute_script("arguments[0].click();", element)

            # Wait for files to load
            time.sleep(1)

            # Find the parent element again to search within its context
            parent_element = driver.find_element(By.XPATH, f"//summary[text()='{text}']/..")

            # Find and click the CSV files within the parent element
            files = parent_element.find_elements(By.XPATH, ".//a[text()='ProductsAndPrices.csv']")
            for file in files:
                # Scroll file into view
                driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", file)
                time.sleep(0.5)
                # Click using JavaScript
                driver.execute_script("arguments[0].click();", file)

            # Small delay between sections
            time.sleep(1)

        except Exception as e:
            print(f"Error clicking element with text '{text}': {str(e)}")

    time.sleep(10)

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser
    driver.quit()
