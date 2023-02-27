import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#Snq for your time, collegue ;)
from parameterized import parameterized
link_passed = "http://suninjuly.github.io/registration1.html"
link_assert = "http://suninjuly.github.io/registration2.html"



class TestAbs(unittest.TestCase):
    @parameterized.expand([
    (link_passed,),
    (link_assert),
])
    def test_elem_search(self, link):
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
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        return browser.quit()

    


if __name__ == "__main__":
    unittest.main()