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

def capture_screenshot():
    driver = driver.get_webdriver_instance()
    driver.set_window_size(500, 325) 
    canvas_element = driver.find_element_by_xpath("//canvas")
    result = canvas_element.screenshot_as_png
    with open('save.png', 'wb') as f:
        f.write(result)

driver = webdriver.Chrome()

# Open a webpage
driver.get("https://roobet.com/casino/game/evolution:craps")

# Scroll until no more content is loaded
time.sleep(20)
lgBtn = WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedTertiary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-colorTertiary.MuiButton-root.MuiButton-contained.MuiButton-containedTertiary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-colorTertiary.css-8irxk2"))
)
driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", lgBtn)
lgBtn.click()
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
        notificationCancel = driver.find_element(By.ID,"onesignal-slidedown-cancel-button")
        driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", notificationCancel)
        notificationCancel.click()
        break
    except :
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
im1 = im.crop((550, 0, 600, 100)) # defines crop points
im1.save('screenshot1.png')
print("sssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
while True:
    time.sleep(5)
    try :
        viewBtn = driver.find_element(By.XPATH, "//button[@data-role='video-button']")
        driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", viewBtn)
        viewBtn.click()
        break
    except :
        continue
time.sleep(15)