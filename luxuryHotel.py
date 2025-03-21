from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, re
from urllib.parse import urlparse, parse_qs, unquote, urlunparse
import json
import csv
driver = webdriver.Chrome()
# Open a webpage
driver.get("https://superiorhotels.info/luxusurlaub")

# Scroll until no more content is loaded
wait = WebDriverWait(driver, 100)
file_name = 'luxuryHotel.csv'
while True:
    time.sleep(1)
    try :
        cancelBtn = driver.find_element(By.CLASS_NAME,'cc_b_dc')
        driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", cancelBtn)
        driver.execute_script("arguments[0].click();", cancelBtn)
        break
    except :
        continue
while True :
    try :
        hotels = driver.find_elements(By.CSS_SELECTOR, ".sp11.jq-result-list-item.hit-on-map")
        driver.implicitly_wait(100)
        for hotel in hotels:
            try :
                driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", hotel)
                driver.implicitly_wait(5)
                driver.execute_script("arguments[0].click();", hotel)
                driver.implicitly_wait(5)
                driver.switch_to.window(driver.window_handles[1])
                driver.implicitly_wait(5)
                nameElement = driver.find_element(By.ID, 'EntryPage')
                driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", nameElement)
                name = nameElement.text
                addressElements = driver.find_elements(By.CLASS_NAME, 'ep8201')
                for addressElement in addressElements:
                    driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", addressElement)
                    driver.implicitly_wait(5)
                    address = addressElement.text
                    break
                try :
                    telephoneTag = driver.find_element(By.CLASS_NAME, 'ep85')
                    driver.implicitly_wait(5)
                    driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", telephoneTag)
                    driver.implicitly_wait(5)
                    showBtn = telephoneTag.find_element(By.CSS_SELECTOR, ".ep852.jq-show-phone")
                    driver.implicitly_wait(5)
                    driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", showBtn)
                    telephoneElement = telephoneTag.find_element(By.CSS_SELECTOR,'.ep851.jq-phone-complete')
                    driver.implicitly_wait(5)
                    driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", telephoneElement)
                    telephoneNumber = telephoneElement.get_attribute("href")
                except :
                    telephoneNumber = None
                try :
                    websiteElement = driver.find_element(By.CSS_SELECTOR,'.ep89.jq-link-to-website')
                    driver.implicitly_wait(5)
                    driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", websiteElement)
                    website = websiteElement.get_attribute('href')
                except:
                    website = None
                new_data = [name, address, telephoneNumber, website]
                # for product in products:
                #     new_data.append(translator.translate(product.text))
                data = [new_data]
                try:
                    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        writer.writerows(data)
                except:
                    print(data)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            except:
                continue
    except :
        continue
    nextelement = driver.find_element(By.CSS_SELECTOR, "[rel='next']")
    className = nextelement.get_attribute("class")
    if className == "" :
        driver.execute_script("arguments[0].click();", nextelement)
        continue
    else :
        break