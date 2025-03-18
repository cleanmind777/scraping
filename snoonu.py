from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from urllib.parse import urlparse, parse_qs, unquote
import json
def parseURL(url):
    # Parse the URL
    parsed_url = urlparse(url)

    # Extract the query parameters
    query_params = parse_qs(parsed_url.query)

    # Get the 'url' parameter (it's a list, so take the first element)
    encoded_image_url = query_params.get("url", [""])[0]

    # Decode the URL-encoded image URL
    decoded_image_url = unquote(encoded_image_url)
    return decoded_image_url
# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()
# Open a webpage
driver.get("https://snoonu.com/snoonu-market/electronics/mobiles")
time.sleep(5)
sortShow = driver.find_element(By.CSS_SELECTOR,'.SortBy_container__WBAER.SortBy_filter__rAekA')
driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", sortShow)
sortShow.click()
time.sleep(2)
SortTag = driver.find_element(By.CLASS_NAME, "SortBy_options__srzG_")
# driver.execute_script("arguments[0].scrollIntoView();", SortTag)
driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", SortTag)
highSort = driver.find_element(By.XPATH, "//div[@class='SortBy_options__srzG_']/p[last()]")
driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", highSort)
highSort.click()
time.sleep(5)
index = 0
productList = []
# Scroll until no more content is loaded
x = 7000
while True:
    last_height = driver.execute_script("return document.body.scrollHeight")
    wait = WebDriverWait(driver, 10)
    while True:
        # Scroll down to the bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for new content to load
        time.sleep(2)  # Adjust the sleep time as needed

        # Calculate new scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            driver.execute_script("window.scrollTo(0, 0);")  # No more content loaded
            break
        last_height = new_height

    
    mobilesTag = driver.find_element(By.CSS_SELECTOR,'.sortOptionsPortalContainer')
    
    # driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", mobilesTag)
    # mobileGroups = mobilesTag.find_elements(By.CSS_SELECTOR,'.ProductGroup_group___f4Kx')
    # for group in mobileGroups:
        # driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", group)
    time.sleep(3)
    mobiles = mobilesTag.find_elements(By.CSS_SELECTOR, '[rel="noopener noreferrer"]')
    for mobile in mobiles:
        # mobile = wait.until(EC.element_to_be_clickable(mobile))
        driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", mobile)
        mobile = wait.until(EC.element_to_be_clickable(mobile))
        driver.execute_script("arguments[0].click();", mobile)
        driver.implicitly_wait(5)
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[1])

        index = index + 1
        prepare = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".ProductDetail_wrapper__r4szG"))
        )
        name = prepare.find_element(By.TAG_NAME, 'h1').text
        # print(name)      
        try : 
            price = prepare.find_element(By.CSS_SELECTOR, ".AddToCart_header__w7zoG")
            driver.execute_script("arguments[0].scrollIntoView();", price)
            discountPrice = price.find_element(By.TAG_NAME, 'h3').text
            try:
                mainPrice = price.find_element(By.TAG_NAME, 'p').text
            except:
                mainPrice = discountPrice
                discountPrice = None
        except :
            mainPrice = None
            discountPrice = None
        # print("price:",mainPrice)
        # print("discountPrice:", discountPrice)
        image = []
        try : 

            imageDivs = prepare.find_element(By.CSS_SELECTOR, "div[class='Gallery_wrapper__lb5TV']")
            driver.execute_script("arguments[0].scrollIntoView();", imageDivs)
            imageTAGs = imageDivs.find_elements(By.CSS_SELECTOR, 'div[data-test-id="slider-main-image"]')
            for imagTAG in imageTAGs:
                driver.execute_script("arguments[0].scrollIntoView();", imagTAG)
                image.append(parseURL(imagTAG.find_element(By.TAG_NAME, 'img').get_attribute('src')))
                # print(parseURL(imagTAG.find_element(By.TAG_NAME, 'img').get_attribute('src')))
                
        except :

            print("IMG error")

        try :
            
            # description = imageDivs.find_element(By.XPATH, "following-sibling::*[1]")
            description = prepare.find_element(By.CSS_SELECTOR, ".Description_wrapper__klRfB.MainInfo_description__aMDzK")
            driver.execute_script("arguments[0].scrollIntoView();", description)
            description1 = description.find_element(By.TAG_NAME, 'p').text
            # print(description1)
        except :
            description1 =''
        try :
            shop = driver.find_element(By.CSS_SELECTOR, "p[class='Typography_p6__xuxGw AddToCart_merchantName__lT1Cu']").text
            # print(shop)
        except :
            print("Shop Error")
        try :
            availableDiv = driver.find_element(By.CSS_SELECTOR, 'p[class="Typography_p12__ERAzo Tag_tag__7Yjwu Tag_gray__b7ASa"]')
            available = True
        except :
            available = False
        product = {
            'Name' : name,
            'Description' : description1,
            'Images' : image,
            'Prices' : {
                'main' : mainPrice,
                'discount' : discountPrice
            },
            "Availability" : available,
            "Attribute" : {

            },
            'shop' : shop,
        }
        productList.append(product)
        driver.close()
        driver.switch_to.window(window_handles[0])
        if discountPrice == None:
            x = mainPrice
        else :
            x = discountPrice
        x = x.replace(",", "").replace("QR", "").strip()
        x = int(x)
        with open("snoonu.json", "w") as json_file:
            json.dump(productList, json_file, indent=4)  # `indent=4` for pretty-printing
        print(index)

    if x == 8:
        break
    input_element = driver.find_element(By.NAME, "maxPrice")
    driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", input_element)
    # Clear the existing value
    input_element.clear()
        # Input a new value
    input_element.send_keys(f"{x}")
    print(x)
    time.sleep(3)
    # except :
    #     break

time.sleep(3)

with open("snoonu.json", "w") as json_file:
    json.dump(productList, json_file, indent=4)  # `indent=4` for pretty-printing

print("Data written to data.json")
