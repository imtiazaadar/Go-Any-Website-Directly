# Go Any Website Automation
# Imtiaz Adar

import pyautogui as auto
from time import sleep
sleep(3)
auto.moveTo(254, 1058)
auto.click()
sleep(2)
auto.write('Crome')
sleep(2)
auto.press('enter')
sleep(4)
auto.moveTo(740, 559)
auto.click()
website = input('Enter Which Website You Want To Go : ').lower()
sleep(6)
auto.write(f'www.{website}.com')
auto.press('enter')
