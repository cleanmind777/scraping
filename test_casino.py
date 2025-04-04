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
import soundfile
import speech_recognition as sr
import os
import urllib
chrome_options = Options()

# Disable GPU acceleration
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")
    



# Open a webpage
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
xx = 0
field4 = Point(315 / 784, 356 / 553)
field5 = Point(360 / 784, 356 / 553)
field6 = Point(404 / 784, 356 / 553)
field8 = Point(447 / 784, 356 / 553)
field9 = Point(492 / 784, 356 / 553)
field10 = Point(538 / 784, 356 / 553)
fieldAll = Point(458 / 784, 402 / 553)
dollar05 = Point(367 / 784, 467 / 553)
dollar1 = Point(391 / 784, 467 / 553)
dollar2 = Point(414 / 784, 467 / 553)
dollar5 = Point(438 / 784, 467 / 553)
dollar25 = Point(462 / 784, 467 / 553)
dollar100 = Point(485 / 784, 467 / 553)
cancelNoti = Point(216 / 784, 177 / 553)
fullmode = Point(641 / 784, 497 / 553)
view = Point(650 / 784, 97 / 553)
Result1 = Point(440 / 784, 287 / 553)
Result2 = Point(454 / 784, 298 / 553)
while True:
    xx = xx + 1
    driver = webdriver.Chrome(options=chrome_options)
    if xx == 1:
        driver.get("https://roobet.com/casino/game/evolution:craps?modal=auth&tab=login")
    else :
        driver.get("https://roobet.com/casino/game/evolution:craps")
    # Scroll until no more content is loaded
    # lgBtn = WebDriverWait(driver, 100).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, ".MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedTertiary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-colorTertiary.MuiButton-root.MuiButton-contained.MuiButton-containedTertiary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-colorTertiary.css-8irxk2"))
    # )
    # driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", lgBtn)
    # lgBtn.click()
    time.sleep(20)
    username = driver.find_element(By.ID, 'auth-dialog-username')
    driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", username)
    username.clear()
            # Input a new value
    username.send_keys("cleanmindUA")
    password = driver.find_element(By.ID,'auth-dialog-current-password')
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", password)
    password.send_keys("hpscks0518")
    password.send_keys(Keys.ENTER)
    try :
        time.sleep(20)
        driver.switch_to.default_content()
        frames = driver.find_element(By.CSS_SELECTOR, "iframe[title='recaptcha challenge expires in two minutes']")
        driver.switch_to.frame(frames)
        driver.find_element(By.ID, "recaptcha-audio-button").click()

        # Click the play button
        driver.switch_to.default_content()   
        frames= driver.find_elements(By.TAG_NAME, "iframe")
        driver.switch_to.frame(frames[-1])
        time.sleep(2)
        driver.find_element(By.XPATH, "//div/div//div[3]/div/button").click()

        #get the mp3 audio file
        src = driver.find_element(By.ID, "audio-source").get_attribute("src")
        print("[INFO] Audio src: %s"%src)

        #download the mp3 audio file from the source
        file_path = os.path.join(os.getcwd(), "captcha1.wav")
        print(file_path)
        urllib.request.urlretrieve(src, file_path)

        data,samplerate=soundfile.read('captcha1.wav')
        soundfile.write('rmt.wav',data,samplerate, subtype='PCM_16')
        r=sr.Recognizer()
        with sr.AudioFile("rmt.wav") as source:
            audio_data=r.record(source)
            text=r.recognize_google(audio_data)
            print(text)
        time.sleep(5)

        # Click the verify button
        driver.find_element(By.ID, "audio-response").send_keys(text)
        time.sleep(2)
        driver.find_element(By.ID, "recaptcha-verify-button").click()    
    except :
        print("None Captcha")
    driver.switch_to.default_content()
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


    # while True:
    #     time.sleep(5)
    #     try :
    #         videoTag = driver.find_element(By.TAG_NAME, "iframe")
    #         driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", videoTag)
    #         link = videoTag.get_attribute('src')
    #         break
    #     except :
    #         print("yet")
    #         continue
    # print(link)
    # driver.execute_script(f"window.open('{link}', '_blank');")

    # # Switch to the new tab
    # # Get the list of all window handles
    # window_handles = driver.window_handles

    # # Switch to the last handle (the new tab)
    # driver.switch_to.window(window_handles[-1])
    print("Preparing.............")
    # while True:
    #     time.sleep(5)
    #     try :
    #         videoTag = driver.find_element(By.TAG_NAME, "iframe")
    #         driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top - (window.innerHeight / 2));", videoTag)
    #         link = videoTag.get_attribute('src')
    #         break
    #     except :
    #         print("yet")
    #         continue
    # driver.switch_to.frame(videoTag)
    driver.set_window_size(800,700)
    time.sleep(10)
    # png = driver.get_screenshot_as_png()
    # im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
    # # im.save(f'full{z}')
    # im1 = im.crop((im.width / 760 * 610, im.height * 10 / 440, im.width / 760 * 620, im.height * 20 / 440)) # defines crop points
    
    # # print("sssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
    # time.sleep(5)

    # pyautogui.moveTo(x, y)
    # pyautogui.click()
    #cancel notification
    width = driver.execute_script("return window.innerWidth")
    height = driver.execute_script("return window.innerHeight")
    x = width * cancelNoti.x
    y = height * cancelNoti.y
    actions = ActionChains(driver)
    actions.move_by_offset(x, y).click().perform()
    time.sleep(0.5)
    # click full mode
    actions.reset_actions()
    actions.move_by_offset(width * fullmode.x, height * fullmode.y).click().perform()
    # click view mode
    actions.reset_actions()
    actions.move_by_offset(width * view.x, height * view.y).click().perform()
    print("Casino Start....")
    z = 0
    # x1 = 433 / 784 * 800
    # y1 = 276 / 463 * 600
    list = ['0','0','0','0']
    count7 = 0
    while z < 5000:
        z = z + 1
        print(f'----------------{z}')
        # actions.reset_actions()
        # actions.move_by_offset(x1, y1).click().perform()
        png = driver.get_screenshot_as_png()
        im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
        im1 = im.crop((im.width * Result1.x, im.height * Result1.y, im.width * Result2.x, im.height * Result2.y)) # defines crop points
        im.save(f'full{z}.png')
        im1 = im1.resize((im1.width*2, im1.height*2), Image.Resampling.LANCZOS)
        im1.save(f'screenshot{z}.png')
        time.sleep(0.5)
        image = cv2.imread(f'screenshot{z}.png', 0)
        thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        # thresh = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY_INV)
        data = pytesseract.image_to_string(thresh, lang='eng',config='--psm 6')
        data = data.strip()
        # print(data)
        if data == '2' or data == '3' or data == '4' or data == '5' or data == '6' or data == '7' or data == '8' or data == '9' or data == '10' or data == '11' or data == '12':
            list.pop(0)
            list.append(data)
            print(f'Roll history: {list}')
            viewport_width = driver.execute_script("return document.documentElement.clientWidth;")
            viewport_height = driver.execute_script("return document.documentElement.clientHeight;")
            if list[2] == '7':
                time.sleep(4)
                actions.reset_actions()
                actions.move_by_offset(field5.x * viewport_width, field5.y * viewport_height).click_and_hold().move_by_offset(viewport_width * 706 / 784 - field5.x * viewport_width, viewport_height * 426 / 553 - field5.y * viewport_height).release().perform()
                actions.reset_actions()
                actions.move_by_offset(field6.x * viewport_width, field6.y * viewport_height).click_and_hold().move_by_offset(viewport_width * 706 / 784 - field6.x * viewport_width, viewport_height * 426 / 553 - field6.y * viewport_height).release().perform()
                actions.reset_actions()
                actions.move_by_offset(field8.x * viewport_width, field8.y * viewport_height).click_and_hold().move_by_offset(viewport_width * 706 / 784 - field8.x * viewport_width, viewport_height * 426 / 553 - field8.y * viewport_height).release().perform()
                actions.reset_actions()
                actions.move_by_offset(fieldAll.x * viewport_width, fieldAll.y * viewport_height).click_and_hold().move_by_offset(viewport_width * 706 / 784 - fieldAll.x * viewport_width, viewport_height * 426 / 553 - fieldAll.y * viewport_height).release().perform()
            if data == '7':
                count7 = count7 + 1
                if count7 >= 1:
                    print('Plz bet!!!!!!!!!!!!!')
                    time.sleep(5)
                    # driver.execute_script("window.scrollTo({}, {});".format(dollar05.x * 800, dollar05.y * 600))
                    actions.reset_actions()
                    actions.move_by_offset(dollar05.x * viewport_width, dollar05.y * viewport_height).click().perform()
                    actions.reset_actions()
                    actions.move_by_offset(field5.x * viewport_width, field5.y * viewport_height).click().perform()
                    actions.reset_actions()
                    actions.move_by_offset(field6.x * viewport_width, field6.y * viewport_height).click().perform()
                    actions.reset_actions()
                    actions.move_by_offset(field8.x * viewport_width, field8.y * viewport_height).click().perform()
                    actions.reset_actions()
                    actions.move_by_offset(fieldAll.x * viewport_width, fieldAll.y * viewport_height).click().perform()
            else :
                count7 = 0
            print(f'count:{count7}')
            time.sleep(3)
        # kernel = np.ones((2,2), np.uint8)
        # thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        # data = pytesseract.image_to_string(thresh, lang='eng',config='--psm 6')
        time.sleep(0.5)