from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'https://stepik.org/lesson/25969/step/8'

try:
    driver = webdriver.Firefox()
    driver.get(link)
finally:
    driver.close()