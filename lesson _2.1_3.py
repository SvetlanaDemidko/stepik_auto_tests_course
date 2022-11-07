from selenium import webdriver
import math
import time
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
time.sleep(10)
browser.quit()

input = browser.find_element_by_id('answer')
input.send_keys(y)

checkbox = browser.find_element_by_id('robotCheckbox')
checkbox.click()
radio = browser.find_element_by_id('robotsRule')
radio.click()
submit = browser.find_element_by_class_name('btn')
submit.click()


