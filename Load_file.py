import os
from selenium import webdriver
import time

current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
# element.send_keys(file_path)
# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")
input1 = browser.find_elements_by_css_selector("[type='text']")

for i in input1:
    i.send_keys("Ivan")
    # time.sleep(2)
element = browser.find_element_by_id('file')
element.send_keys(current_dir)
press1 = browser.find_element_by_xpath('//button')
press1.click()
print(browser.switch_to.alert.text)
browser.quit()

