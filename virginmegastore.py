from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, re
from urllib.parse import urlparse, parse_qs, unquote, urlunparse
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
driver.get("https://www.virginmegastore.qa/en/electronics-accessories/mobiles-accessories/mobile-phones/c/n010301")

# Scroll until no more content is loaded
wait = WebDriverWait(driver, 100)

next_element = 1
while next_element is not None:
    mobileGroup = driver.find_element(By.CSS_SELECTOR,'ul[class="product-list__item-wrapper grid g-row__4"]')
    # print(mobileGroup.tag_name)
    mobiles= mobileGroup.find_elements(By.TAG_NAME,'li')
    index = 0
    productList = []
    for mobile in mobiles:
        attributes = {}
        mobile = wait.until(EC.element_to_be_clickable(mobile))
        driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", mobile)
        brand = mobile.find_element(By.CLASS_NAME, 'product-list__brand').text
        print(brand)
        attributes['Brand']=brand
        link = mobile.find_element(By.CLASS_NAME, "product-list__thumb")
        new_url = link.get_attribute("href")  # Get the URL from the element (e.g., <a> tag)
        script = """
            // Prevent the default click behavior
            arguments[0].addEventListener('click', function(event) {
                event.preventDefault();
            });

            // Open the new URL in a new tab
            window.open(arguments[1], '_blank');
        """
        driver.execute_script(script, link, new_url)
        driver.implicitly_wait(100)
        link.click()

        driver.switch_to.window(driver.window_handles[1])
        index = index + 1
        driver.implicitly_wait(300)
        while True:
            time.sleep(3)
            try :
                prepare = driver.find_element(By.CSS_SELECTOR, ".container.page-productDetails")
                break
            except :
                continue
        driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", prepare)
        title = prepare.find_element(By.CLASS_NAME, 'productDetail__descriptionTitle')
        driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", title)
        name = title.text
        print(name)
        price = prepare.find_element(By.CLASS_NAME, 'price__value ')
        driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", price)
        mainPrice = price.text
        print(mainPrice)
        detail = driver.find_element(By.CSS_SELECTOR, '.pdp-tabs.container.js-pdpTabs.ui-tabs.ui-corner-all.ui-widget.ui-widget-content')

        descriptionTag = detail.find_element(By.CSS_SELECTOR, '.tabContent__paragraph.tabsDescription__longDescription.js-details-long-description')
        descriptionBtn = descriptionTag.find_element(By.CSS_SELECTOR, '.tabContent__viewMore.js-view-full-description.js-truncate.show')
        driver.execute_script("arguments[0].scrollIntoView();", descriptionBtn)
        wait.until(EC.element_to_be_clickable(descriptionBtn))
        time.sleep(3)
        driver.execute_script("arguments[0].click();", descriptionBtn)
        time.sleep(3)
        description = descriptionTag.find_element(By.CSS_SELECTOR, '.tabContent__paragraph.tabsDescription__longDescription__inner')
        print(description.text)
        descriptionResult = description.text
        print(descriptionResult)
        try : 
            attributeTag = WebDriverWait(detail, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.pdp-tabs__tab.details-tab.ui-tabs-panel.ui-corner-bottom.ui-widget-content'))
            )
            attributeTag = detail.find_element(By.CSS_SELECTOR, '.pdp-tabs__tab.details-tab.ui-tabs-panel.ui-corner-bottom.ui-widget-content')
            attributeBtn = attributeTag.find_element(By.CSS_SELECTOR, '.tabContent__viewMore.js-truncate.show')
            driver.execute_script("arguments[0].scrollIntoView();", attributeBtn)
            wait.until(EC.element_to_be_clickable(attributeBtn))
            driver.execute_script("arguments[0].click();", attributeBtn)
            elementAttribute = attributeTag.find_elements(By.CLASS_NAME, 'tabsSpecification__table__row')
            i = 0
            for element in elementAttribute:
                print(i)
                i = i + 1
                driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", element)
                key = element.find_element(By.CSS_SELECTOR, '.tabsSpecification__table__cell-head')
                keytext = key.text
                driver.implicitly_wait(5)
                # value = element.find_element(By.XPATH, "//*[@class='tabsSpecification__table__cell']")
                value = key.find_element(By.XPATH, "following-sibling::div[1]")
                driver.implicitly_wait(5)
                driver.execute_script("arguments[0].scrollIntoView();", value)
                driver.implicitly_wait(5)
                attributes[keytext] = value.text
        except :
            try : 
                print(driver.page_source)
                elements = detail.find_elements(By.TAG_NAME,'tr')
                for element in elements:
                    print(i)
                    i = i + 1
                    driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", element)
                    key = element.find_element(By.TAG_NAME,'th')
                    keytext = key.text
                    driver.implicitly_wait(5)
                    # value = element.find_element(By.XPATH, "//*[@class='tabsSpecification__table__cell']")
                    value = key.find_element(By.XPATH, "following-sibling::td[1]")
                    driver.implicitly_wait(5)
                    driver.execute_script("arguments[0].scrollIntoView();", value)
                    driver.implicitly_wait(5)
                    attributes[keytext] = value.text
            except :
                attributes ={None}
                print(attributes)
        print(attributes)
        image = []
        imagtags = prepare.find_element(By.CLASS_NAME, 'pdp_image-carousel.swiper-container.swiper-container-initialized.swiper-container-horizontal')
        driver.execute_script("arguments[0].scrollIntoView();", imagtags)
        images = imagtags.find_elements(By.CSS_SELECTOR, '.swiper-slide')
        for imageElement in images:
            driver.execute_script("arguments[0].scrollIntoView();", imageElement)
            imagetag = imageElement.find_element(By.CSS_SELECTOR,'.pdp_image-carousel-image.js-zoomImage.c-pointer')
            # preURL = re.search(r"url\('([^']+)'\)", imagetag.get_attribute('style'))
            # preURL = preURL.group(1)
            url = f"https://www.virginmegastore.qa/{imagetag.get_attribute('style')[18:-3]}"
            image.append(url)
        print(image)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        product = {
            'Name' : name,
            'Description' : descriptionResult,
            'Images' : image,
            'Prices' : {
                'main' : mainPrice,
                'discount' : None
            },
            "Availability" : None,
            "Attribute" : attributes
        }
        productList.append(product)
        with open("vir.json", "w") as json_file:
            json.dump(productList, json_file, indent=4)  # `indent=4` for pretty-printing
    next_element.click()
    
    driver.implicitly_wait(5)

print(index)
with open("vir.json", "w") as json_file:
    json.dump(productList, json_file, indent=4)  # `indent=4` for pretty-printing

print("Data written to data.json")
