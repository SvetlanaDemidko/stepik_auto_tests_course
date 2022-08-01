from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

submit = browser.find_element(By.CLASS_NAME, 'btn')
submit.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
#link = "http://suninjuly.github.io/redirect_page.html?"
#browser = webdriver.Chrome()
#browser.get(link)
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)

input = browser.find_element(By.ID, 'answer')
input.send_keys(y)

submit = browser.find_element(By.CLASS_NAME, 'btn')
submit.click()

time.sleep(10)
browser.quit()