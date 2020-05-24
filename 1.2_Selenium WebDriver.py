import time
from selenium.webdriver.common.by import By
from selenium import webdriver

# инициализируем драйвер браузера.
# После этой команды мы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()


# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что надо открыть сайт по куазанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# Метод find_element_by_css_selector позволяет найти нужный элемент, указав путь к нему.
# Ищем поле для ввода текста
textar = driver.find_element_by_css_selector(".textarea")

# Напишем текст ответа в найденное поле
textar.send_keys("get()")

time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть
# сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()
