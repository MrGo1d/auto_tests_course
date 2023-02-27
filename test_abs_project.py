from selenium import webdriver
from selenium.webdriver.common.by import By
#Snq for your time, collegue ;)

link_passed = "http://suninjuly.github.io/registration1.html"
link_assert = "http://suninjuly.github.io/registration2.html"

def test_elem_search(link):
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, '.first_block input.form-control.third')
    input3.send_keys("mail@mail.com")

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
    return browser.quit()

if __name__ == "__main__":
    test_elem_search(link_passed)
    test_elem_search(link_assert)
    