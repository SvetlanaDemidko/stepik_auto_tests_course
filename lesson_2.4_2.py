from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
#browser.implicitly_wait(5)
submit = browser.find_element(By.ID, 'book')
submit.click()

browser.execute_script("window.scrollBy(0, 400);")


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)

input = browser.find_element(By.ID, 'answer')
input.send_keys(y)

submit = browser.find_element(By.ID, 'solve')
submit.click()

time.sleep(10)
browser.quit()