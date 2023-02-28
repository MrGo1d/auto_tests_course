import pytest
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"



def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_basket_link_on_the_main_page(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_should_see_search_button_on_the_main_page(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")