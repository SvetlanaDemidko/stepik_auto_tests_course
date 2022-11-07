from selenium import webdriver
import math
import time
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
#time.sleep(10)
#browser.quit()

input = browser.find_element_by_id('answer')
input.send_keys(y)

checkbox = browser.find_element_by_id('robotCheckbox')
checkbox.click()
radio = browser.find_element_by_id('robotsRule')
browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
radio.click()
submit = browser.find_element_by_class_name('btn')
submit.click()

time.sleep(10)
browser.quit()


#Как вариант еще можно скрывать ненужный элемент

#browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)