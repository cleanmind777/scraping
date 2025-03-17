from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from urllib.parse import urlparse, parse_qs, unquote
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

# Scroll until no more content is loaded
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

mobiles = driver.find_element(By.CLASS_NAME,'sortOptionsPortalContainer')
driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", mobiles)
mobileGroups = mobiles.find_elements(By.CLASS_NAME,'ProductGroup_group___f4Kx')
index = 0
productList = []
for group in mobileGroups:
    mobiles = group.find_elements(By.CSS_SELECTOR, 'a[rel="noopener noreferrer"]')
    for mobile in mobiles:
        mobile = wait.until(EC.element_to_be_clickable(mobile))
        driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", mobile)
        mobile = wait.until(EC.element_to_be_clickable(mobile))
        driver.execute_script("arguments[0].click();", mobile)
        driver.implicitly_wait(5)
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[1])
        # print(href_value)
        # newdriver = webdriver.Chrome()
        # newdriver.get(href_value)
        index = index + 1
        
        name = driver.find_element(By.TAG_NAME, 'h1').text
        print(name)
        # moreBtn = driver.find_element(By.CLASS_NAME, 'Description_showMore__FPUOc')
        # wait.until(EC.element_to_be_clickable(moreBtn))
        # moreBtn.click()
        description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".Description_wrapper__klRfB.MainInfo_description__aMDzK"))
        )
        description1 = description.find_element(By.TAG_NAME, 'p').text
        print(description1)

        price = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".AddToCart_header__w7zoG"))
        )
        discountPrice = price.find_element(By.TAG_NAME, 'h3').text
        try:
            mainPrice = price.find_element(By.TAG_NAME, 'p').text
        except:
            mainPrice = discountPrice
            discountPrice = mainPrice
        print("price:",mainPrice)
        print("discountPrice:", discountPrice)
        image = []
        try : 
            # imageDivs = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.CSS_SELECTOR, ".ProductSlider_gallery__oxbnr"))
            # )
            # print(imageDivs.tag_name)
            # imageTAGs = imageDivs.find_elements(By.CSS_SELECTOR, 'img[data-nimg="intrinsic"]')
            # for imageTAG in imageTAGs:
            #     image.append(parseURL(imageTAG.get_attribute("src")))
            #     print(parseURL(imageTAG.get_attribute("src")))
            imageDivs = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='keen-slider']"))
            )
            imageTAGs = imageDivs.find_elements(By.CSS_SELECTOR, 'div[data-test-id="slider-main-image"]')
            for imagTAG in imageTAGs:
                driver.execute_script("arguments[0].scrollIntoView();", imagTAG)
                image.append(parseURL(imagTAG.find_element(By.TAG_NAME, 'img').get_attribute('src')))
                print(parseURL(imagTAG.find_element(By.TAG_NAME, 'img').get_attribute('src')))
            
            # image.append(parseURL(imageTAG.get_attribute("src")))
            # print(parseURL(imageTAG.get_attribute("src")))   
        except :
            # imageDivs = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.CSS_SELECTOR, ".ProductSlider_imageWrapper__YWU9q"))
            # )
            # imageTAG = imageDivs.find_element(By.TAG_NAME, 'img')
            # image.append(parseURL(imageTAG.get_attribute("src")))
            # print(parseURL(imageTAG.get_attribute("src")))   
            print("IMG error")
        # imageTAGs = imageDivs.find_elements(By.XPATH, 'data-nimg="intrinsic')
        # imageTAGs = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, 'img[data-nimg="intrinsic"]'))
        # )
        # newdriver.quit()
        try :
            shop = driver.find_element(By.CSS_SELECTOR, "p[class='Typography_p6__xuxGw AddToCart_merchantName__lT1Cu']").text
            print(shop)
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
                
            }
        }

        driver.close()
        driver.switch_to.window(window_handles[0])
    break
print(index)
time.sleep(20)