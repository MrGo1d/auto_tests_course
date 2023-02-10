from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os 


link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    names = ['firstname', 'lastname', 'email']
    for name in names:
        element = browser.find_element(By.NAME, name)
        element.send_keys('Something')

    send_file = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'bio.txt')  # добавляем к этому пути имя файла 
    send_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, 'button')
    button.click()

finally:
    time.sleep(5)
    browser.quit()
    
