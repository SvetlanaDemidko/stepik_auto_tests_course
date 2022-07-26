from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    input_1.send_keys("Vadim")

    input_2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    input_2.send_keys("Moskalenko")

    input_3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
    input_3.send_keys("www-leningrad.spb.ru")

    input_4 = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.first")
    input_4.send_keys("22345")

    input_5 = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.second")
    input_5.send_keys("Когда переехал не помню, наверное был я бухой")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()