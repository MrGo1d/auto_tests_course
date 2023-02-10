from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/get_attribute.html'


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    box = browser.find_element(By.CSS_SELECTOR, "img")
    x = box.get_attribute('valuex')
    

    set_answer = browser.find_element(By.CSS_SELECTOR, '#answer') 
    set_answer.send_keys(calc(x))

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radiobox = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobox.click()

    btn = browser.find_element(By.CSS_SELECTOR, "button")
    btn.click()

finally:
    time.sleep(5)
    browser.quit()

