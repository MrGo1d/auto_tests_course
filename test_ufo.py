import pytest
from selenium.webdriver.common.by import By
import math
import time
from .env import config  

answer = math.log(int(time.time()))
print(answer)



@pytest.mark.parametrize('login', [config.login])
@pytest.mark.parametrize('password', [config.password])
@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                   'https://stepik.org/lesson/236896/step/1',
                                   'https://stepik.org/lesson/236897/step/1',
                                   'https://stepik.org/lesson/236898/step/1',
                                   'https://stepik.org/lesson/236899/step/1',
                                   'https://stepik.org/lesson/236903/step/1',
                                   'https://stepik.org/lesson/236904/step/1',
                                   'https://stepik.org/lesson/236905/step/1'
                                ])
def test_auto_auth(browser, link, login, password):
    browser.get(link)
    browser.implicitly_wait(30)
    browser.find_element(By.ID, 'ember33').click()
    browser.find_element(By.ID, 'id_login_email').send_keys(login)
    browser.find_element(By.ID, 'id_login_password').send_keys(password)
    browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn ').click()

    # if browser.find_elements(By.CSS_SELECTOR, 'button.again-btn'): browser.find_elements(By.CSS_SELECTOR, 'button.again-btn').click()

    # if browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text != 'Correct!':
    #     browser.find_element(By.CSS_SELECTOR, 'button.again-btn').click()
    #     browser.find_element(By.CSS_SELECTOR,'footer.modal-popup__footer button:nth-child(1)').click()
    time.sleep(10)
    browser.find_element(By.TAG_NAME, 'textarea').clear()
    browser.find_element(By.TAG_NAME, 'textarea').send_keys(answer)
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, 'button.submit-submission').click()
    time.sleep(2)
    assert browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text == 'Correct!'

