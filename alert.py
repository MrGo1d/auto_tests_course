from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = 'http://suninjuly.github.io/alert_accept.html'
stepik = 'https://stepik.org/lesson/184253/step/4?after_pass_reset=true&auth=login&unit=158843'


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def get_num(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.TAG_NAME, 'button').click()
        browser.switch_to.alert.accept()

        x = browser.find_element(By.ID, 'input_value')
        answer = browser.find_element(By.ID, 'answer')
        answer.send_keys(calc(x.text))

        browser.find_element(By.TAG_NAME, 'button').click()

        allert_info = browser.switch_to.alert
        allert_text = allert_info.text
        time.sleep(5)
        return allert_text[allert_text.find('quiz:') + 6:]
    finally:
        time.sleep(5)
        browser.quit()    


def set_num(link, text):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(5)
        #auth
        browser.find_element(By.ID, 'id_login_email').send_keys('YOUR E-MAIL ADDRESS')
        browser.find_element(By.ID, 'id_login_password').send_keys('YOUR PASSWORD')

        browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn').click()
        time.sleep(5)

        browser.get('https://stepik.org/lesson/184253/step/4?unit=158843')
        time.sleep(5)

        text_area = browser.find_element(By.CSS_SELECTOR, 'textarea').clear()
        text_area.send_keys(text)

        browser.find_element(By.CLASS_NAME, 'submit-submission').click()
    finally:
        time.sleep(5)
        browser.quit()


set_num(stepik, get_num(link))
