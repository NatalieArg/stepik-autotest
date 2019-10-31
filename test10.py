from selenium import webdriver
import time
import math

link='http://suninjuly.github.io/redirect_accept.html'

try:
    browser=webdriver.Chrome()
    browser.get(link)
    button1=browser.find_element_by_tag_name('button')
    button1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    input=browser.find_element_by_id('input_value')
    x=input.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y=calc(x)
    input2=browser.find_element_by_id('answer')
    input2.send_keys(y)
    button2 = browser.find_element_by_tag_name('button')
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

