from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link='http://suninjuly.github.io/explicit_wait2.html'

try:
    browser=webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    button=WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    button2=browser.find_element_by_id('book')
    button2.click()
    input=browser.find_element_by_id('input_value')
    x=input.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y=calc(x)
    input2=browser.find_element_by_id('answer')
    input2.send_keys(y)
    button3 = browser.find_element_by_id('solve')
    button3.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


