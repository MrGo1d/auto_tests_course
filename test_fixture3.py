import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()

# addfinalizer:  it's work, but may incorrect
# @pytest.fixture
# def browser(request):
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     #этот код выполнится после завершения теста
#     def browser_teardown():
#         print("\nquit browser..")
#         browser.quit()
#     request.addfinalizer(browser_teardown)



class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")


    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
