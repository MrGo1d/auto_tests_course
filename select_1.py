from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, '#num1')
    num2 = browser.find_element(By.CSS_SELECTOR, '#num2')
    sum = str(int(num1.text) + int(num2.text))

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(sum)

    btn = browser.find_element(By.CSS_SELECTOR, 'button')
    btn.click()


finally:
    time.sleep(5)
    browser.quit()