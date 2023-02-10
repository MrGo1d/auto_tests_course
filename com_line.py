from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = 'https://www.pythonanywhere.com/login/'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element(By.NAME, 'auth-username').send_keys('MrGo1d')
    browser.find_element(By.NAME, 'auth-password').send_keys('80447416246')
    browser.find_element(By.ID, 'id_next').click()
    browser.find_element(By.CLASS_NAME, 'dashboard_recent_console').click()
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, 'iframe#id_console').send_keys('python3.10 bot.py\n')

finally:
    time.sleep(3)
    browser.quit()
