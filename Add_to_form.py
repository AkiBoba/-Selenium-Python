from selenium.webdriver.common.by import By
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/registration2.html")
input1 = browser.find_elements_by_css_selector('input[required]')

print(len(input1))
for i in input1:
    i.send_keys("Ivan")
    time.sleep(2)

button = browser.find_element_by_css_selector("button.btn")
button.click()
time.sleep(5)
browser.quit()