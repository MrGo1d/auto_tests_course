from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = 'http://suninjuly.github.io/redirect_page.html?'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_clk = browser.find_element(By.TAG_NAME, 'button').click()
    x = browser.find_element(By.ID, 'input_value').text
    answer = browser.find_element(By.ID, 'answer').send_keys(calc(x))
    btn = browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(5)
    browser.quit()


    """browser.switch_to.window(window_name)
Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок. Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:

new_window = browser.window_handles[1]
Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:

first_window = browser.window_handles[0]
После переключения на новую вкладку поиск и взаимодействие с элементами будут происходить уже на новой странице."""