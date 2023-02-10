from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#Snq for your time, collegue ;)

link_passed = "http://suninjuly.github.io/registration1.html"
link_assert = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link_assert)
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, '.first_block input.form-control.third')
    input3.send_keys("mail@mail.com")

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    time.sleep(2)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
    
finally:
    time.sleep(2)
    browser.quit()
