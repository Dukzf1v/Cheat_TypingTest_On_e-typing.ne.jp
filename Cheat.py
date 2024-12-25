import pyautogui
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://www.e-typing.ne.jp/member/'
username = "Duy.DD225828@sis.hust.edu.vn" 
password = "Duy080205" 

service = Service('msedgedriver.exe')  
browser = webdriver.Edge(service=service)
browser.set_window_size(1580, 800)

try:
    browser.get(url)

    username_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "mail"))
    )
    username_field.send_keys(username)

    password_field = browser.find_element(By.ID, "password")
    password_field.send_keys(password)

    password_field.send_keys(Keys.ENTER)

    check_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@title="腕試しレベルチェック"]'))
    )
    check_button.click()

    time.sleep(3)

    iframe = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "typing_content"))
    )
    browser.switch_to.frame("typing_content")

    time.sleep(4)

    check_button_2 = WebDriverWait(browser,10).until(
        EC.presence_of_element_located((By.ID, "start_btn"))
    )
    check_button_2.click()

    time.sleep(5) 

    pyautogui.press('space')

    time.sleep(4)

    while True:
        html = browser.page_source
        bs = BeautifulSoup(html, 'html.parser')
        namelist = bs.find_all('div', {'id': 'sentenceText'})
        if not namelist:
            break
        charList = []
        for name in namelist:
            txt = name.get_text()
            charList.append(txt)
        string = str(charList[0])
        if charList:
            string = str(charList[0])  
            for char in string:
                pyautogui.press(char) 
                time.sleep(0.12)

    time.sleep(50)

except Exception as e:
    print(e)
finally:
    print("Quit")
    browser.quit()
