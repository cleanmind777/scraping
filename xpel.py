from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from geopy.geocoders import Nominatim
from deep_translator import GoogleTranslator
translator = GoogleTranslator(source='auto', target='en')
# Set up the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

geolocator = Nominatim(user_agent="your_app_name")

def city_state_country(coord):
    try:
        a = coord.split(',')[0].strip()
        b = coord.split(",")[1].strip()
        location = geolocator.reverse(coord, exactly_one=True)
        address = location.raw['address']
        city = address.get('city', '')
        state = address.get('state', '')
        country = address.get('country', '')
        return city, state, country
    except Exception as e:
        print(f"Error geocoding {coord}: {e}")
        return '', '', ''

try:
    # Navigate to the website
    driver.get('https://www.xpel.com/installer-locator?srsltid=AfmBOoquw-8XwZFuZ2pE05Ir6DworTiMJBWwNmTi415uaxhkr3JhztxN')
    driver.implicitly_wait(10)

    buttons = driver.find_element(By.CLASS_NAME, 'pagination-load-more')
    index = 0
    while buttons is not None:
        buttons.click()
        driver.implicitly_wait(5)
        
        try:
            buttons = driver.find_element(By.CLASS_NAME, 'pagination-load-more')
        except:
            break
    installer_cards = driver.find_elements(By.CLASS_NAME, 'installer-card')
    for card in installer_cards:
        try :
            products_btn = card.find_element(By.CLASS_NAME, 'collapse-heading')
        except :
            print(card.text)
            continue
        # Scroll to the element and click using JavaScript
        driver.execute_script("arguments[0].scrollIntoView();", products_btn)
        driver.execute_script("arguments[0].click();", products_btn)

        driver.implicitly_wait(1)
        index += 1
        btns = card.find_elements(By.CLASS_NAME, 'button')
        lastbtn = btns[-1]
        href_value = lastbtn.get_attribute('href')
        coord = href_value[51:]
        location_name = card.find_element(By.CLASS_NAME, 'location-name').text.strip()
        labels = card.find_elements(By.CLASS_NAME, 'icon-before')
        if len(labels) == 2:
            phone = labels[0].text.strip()
            website = labels[1].get_attribute('href')
        elif len(labels) == 1:
            phone = labels[0].text.strip()
            website = ''
        else :
            phone = ''
            website = ''
        address = card.find_element(By.TAG_NAME, 'p').text
        products = card.find_elements(By.CLASS_NAME, 'theme-light')
        country = city_state_country(coord)
        country_name = translator.translate(country[2])
        location_name = translator.translate(location_name)
        address = translator.translate(address)
        new_data = [location_name, address, country_name, phone, website]
        for product in products:
            new_data.append(translator.translate(product.text))
        data = [new_data]
        file_name = 'result.csv'
        try:
            with open(file_name, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(data)
        except:
            print(data)
finally:
    # Close the WebDriver
    driver.quit()
