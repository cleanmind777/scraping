from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, re
from urllib.parse import urlparse, parse_qs, unquote, urlunparse
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from io import BytesIO
from selenium.webdriver.chrome.options import Options
import cv2
import pytesseract
import numpy as np
chrome_options = Options()

# Disable GPU acceleration
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")
    

driver = webdriver.Chrome(options=chrome_options)

# Open a webpage
driver.get("https://roobet.com/casino/game/evolution:craps?modal=auth&tab=login")

# Scroll until no more content is loaded
time.sleep(20)
# lgBtn = WebDriverWait(driver, 100).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedTertiary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-colorTertiary.MuiButton-root.MuiButton-contained.MuiButton-containedTertiary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-colorTertiary.css-8irxk2"))
# )
# driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", lgBtn)
# lgBtn.click()
time.sleep(5)
username = driver.find_element(By.ID, 'auth-dialog-username')
driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", username)
username.clear()
        # Input a new value
username.send_keys("hasachkhi@gmail.com")
password = driver.find_element(By.ID,'auth-dialog-current-password')
time.sleep(2)
driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", password)
password.send_keys("123!@#QWErty")
password.send_keys(Keys.ENTER)
time.sleep(10)
while True:
    time.sleep(5)
    try : 
        notificationCancel = driver.find_element(By.CSS_SELECTOR,".MuiButtonBase-root.MuiIconButton-root.MuiIconButton-sizeMedium.css-1os5k11")
        driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", notificationCancel)
        notificationCancel.click()
        break
    except :
        # try:
        #     notificationCancel = driver.find_element(By.CSS_SELECTOR,".MuiButtonBase-root.MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton-sizeMedium.MuiButton.textSizeMedium.MuiButton-colorPrimary.MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton-sizeMedium.MuiButton-textSizeMedium.MuiButton-colorPrimary.css-1shvv6o")
        #     driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", notificationCancel)
        #     driver.implicitly_wait(5)
        #     notificationCancel.click()
        #     break
        # except:
            # 
            # MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-colorPrimary MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-colorPrimary css-1shvv6o
        # MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-colorPrimary MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-colorPrimary css-1shvv6o
        continue


while True:
    time.sleep(5)
    try :
        videoTag = driver.find_element(By.TAG_NAME, "iframe")
        driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", videoTag)
        link = videoTag.get_attribute('src')
        break
    except :
        print("yet")
        continue
print(link)
driver.execute_script(f"window.open('{link}', '_blank');")

# Switch to the new tab
# Get the list of all window handles
window_handles = driver.window_handles

# Switch to the last handle (the new tab)
driver.switch_to.window(window_handles[-1])
while True:
    time.sleep(5)
    try :
        videoTag = driver.find_element(By.TAG_NAME, "iframe")
        driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", videoTag)
        link = videoTag.get_attribute('src')
        break
    except :
        print("yet")
        continue
driver.switch_to.frame(videoTag)
driver.set_window_size(800,600)
time.sleep(10)
png = driver.get_screenshot_as_png()
im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
im1 = im.crop((im.width / 760 * 610, im.height * 10 / 440, im.width / 760 * 620, im.height * 20 / 440)) # defines crop points
im1.save('screenshot1.png')
print("sssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
time.sleep(5)

# pyautogui.moveTo(x, y)
# pyautogui.click()
width = driver.execute_script("return window.innerWidth")
height = driver.execute_script("return window.innerHeight")
x = width / 760 * 615
y = height * 15 / 440
actions = ActionChains(driver)
actions.move_by_offset(x, y).click().perform()
print("---------------------------------------------------------")
z = 0
x1 = 494 / 984 * 800
y1 = 139 / 569 * 600
list = ['0','0','0','0']
count7 = 0
while z < 1000:
    z = z + 1
    actions.reset_actions()
    actions.move_by_offset(x1, y1).click().perform()
    png = driver.get_screenshot_as_png()
    im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
    im1 = im.crop((im.width / 784 * 410, im.height * 223 / 453, im.width / 784 * 423, im.height * 235 / 423)) # defines crop points
    # im.save(f'full{z}.png')
    im1 = im1.resize((im1.width*2, im1.height*2), Image.Resampling.LANCZOS)
    im1.save(f'screenshot.png')
    time.sleep(0.5)
    image = cv2.imread(f'screenshot.png', 0)
    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    # thresh = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY_INV)
    data = pytesseract.image_to_string(thresh, lang='eng',config='--psm 6')
    data = data.strip()
    # print(data)
    if data == '2' or data == '3' or data == '4' or data == '5' or data == '6' or data == '7' or data == '8' or data == '9' or data == '10' or data == '11' or data == '12':
        list.pop(0)
        list.append(data)
        print(list)
        if data == '7':
            count7 = count7 + 1
            if count7 == 4:
                print('Plz bet!!!!!!!!!!!!!')
        else :
            count7 = 0
        print(f'count:{count7}')
        time.sleep(3)
    # kernel = np.ones((2,2), np.uint8)
    # thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    # data = pytesseract.image_to_string(thresh, lang='eng',config='--psm 6')
    time.sleep(0.5)