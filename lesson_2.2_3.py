from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_1 = browser.find_element(By.NAME, "firstname")
    input_1.send_keys("Vadim")

    input_2 = browser.find_element(By.NAME, "lastname")
    input_2.send_keys("Moskalenko")

    input_2 = browser.find_element(By.NAME, "email")
    input_2.send_keys("s.demidko@ukr.net")

#создаем скриптом файл в текущей директории
    #with open('test1.txt', 'w') as file:
     #   file.write('test1 for mls 228')

#открываем файл
    import os

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test1.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    #print(file_path)

    #file_path = os.path.join(current_dir, 'test1.txt')



    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()