from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = 'http://SunInJuly.github.io/execute_script.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)   
    x_value = browser.find_element(By.CSS_SELECTOR, '#input_value')
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(calc(x_value.text))

    checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    checkbox.click()

    rad_button = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", rad_button)
    rad_button.click()

    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(5)
    browser.quit()
