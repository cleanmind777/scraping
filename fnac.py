from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, re
from urllib.parse import urlparse, parse_qs, unquote, urlunparse
import json
from selenium.webdriver.common.action_chains import ActionChains
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
wait = WebDriverWait(driver, 10)
# Open a webpage
driver.get("https://fnac.qa/english/mobility/smartphones.html")
# pageTitle = driver.find_element(By.CLASS_NAME,'page-title-wrapper')
# driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", pageTitle)
# wait.until(EC.element_to_be_clickable(pageTitle))
# pageTitle.click()
time.sleep(10)
actions = ActionChains(driver)
actions.move_by_offset(1, 1).click().perform()
# Scroll until no more content is loaded


mainboard = driver.find_element(By.ID,'amasty-shopby-product-list')
# print(mobileGroup.tag_name)
mobiles= mainboard.find_elements(By.CSS_SELECTOR,'.products.list.items.product-items')
index = 0
productList = []

prevtoolbar = mainboard.find_element(By.CSS_SELECTOR,'products.wrapper.list.products-list')
driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", prevtoolbar)
toolbar = prevtoolbar.find_element(By.XPATH, "following-sibling::div[class=['toolbar toolbar-products']]")
driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", toolbar)
nextBtn = 1
while nextBtn is not None:
    for mobile in mobiles:
        attributes = {}
        # print('111111111111111111111111111111111111111111111111111111111111111111111')
        mobile = wait.until(EC.element_to_be_clickable(mobile))
        driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", mobile)
        linkprepare = mobile.find_element(By.CLASS_NAME, "product-item-info")
        link = linkprepare.find_element(By.CLASS_NAME, "product.photo.product-item-photo")
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

        # Click the element to trigger the new tab


        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[1])
        # mobile = wait.until(EC.element_to_be_clickable(mobile))
        # driver.execute_script("arguments[0].click();", mobile)
        driver.implicitly_wait(5)
        # window_handles = driver.window_handles
        # driver.switch_to.window(window_handles[1])
        # print(href_value)
        # newdriver = webdriver.Chrome()
        # newdriver.get(href_value)
        index = index + 1
        mainTag = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "maincontent"))
        )
        title = mainTag.find_element(By.CSS_SELECTOR, '.page-title-wrapper.product')
        driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", title)
        name = title.text
        print(name)
        price = mainTag.find_element(By.CLASS_NAME, 'price ')
        driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", price)
        mainPrice = price.text
        print(mainPrice)

        detail = mainTag.find_element(By.ID, 'product-attribute-specs-table')
        trs = detail.find_elements(By.TAG_NAME,'tr')
        i = 0
        for element in trs:
            print(i)
            i = i + 1
            driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", element)
            key = element.find_element(By.TAG_NAME, 'th')
            driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", key)
            keytext = key.text
            driver.implicitly_wait(5)
            # value = element.find_element(By.XPATH, "//*[@class='tabsSpecification__table__cell']")
            value = element.find_element(By.TAG_NAME, "td")
            driver.implicitly_wait(5)
            driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", value)
            driver.implicitly_wait(5)
            attributes[keytext] = value.text
        print(attributes)
        images = mainTag.find_elements(By.CSS_SELECTOR,'.fotorama__nav__frame.fotorama__nav__frame--thumb')
        image = []
        for imageElement in images:
            driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", imageElement)
            imageTag = imageElement.find_element(By.TAG_NAME,'img')
            driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", imageTag)
            imageURL = imageTag.get_attribute("src")
            image.append(imageURL)
        print(image)
    prevtoolbar = mainboard.find_element(By.CSS_SELECTOR,'products.wrapper.list.products-list')
    driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", prevtoolbar)
    toolbar = prevtoolbar.find_element(By.XPATH, "following-sibling::div[class=['toolbar toolbar-products']]")
    driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", toolbar)
    nextBtn = toolbar.find_element(By.CSS_SELECTOR,'.action.next')
    driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", nextBtn)
    nextBtn.click()
print(index)
with open("data.json", "w") as json_file:
    json.dump(productList, json_file, indent=4)  # `indent=4` for pretty-printing

print("Data written to data.json")
