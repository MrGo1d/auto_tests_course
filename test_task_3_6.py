import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from .env import config

link = 'https://stepik.org/lesson/236895/step/1'


@pytest.mark.parametrize('login', [config.login])
@pytest.mark.parametrize('password', [config.password])
def test_authorixation_checking(browser, login, password):
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element(By.ID, 'ember33').click()

    browser.find_element(By.ID, 'id_login_email').send_keys(login)
    browser.find_element(By.ID, 'id_login_password').send_keys(password)
    browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn ').click()
    time.sleep(5)
