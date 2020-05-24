from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_xpath('//input')
input1.send_keys("Ivan")
input2 = browser.find_element_by_xpath('//form/div[2]/input')
input2.send_keys("Petrov")
input3 = browser.find_element_by_xpath('//form/div[3]/input')
input3.send_keys("Smolensk")
input4 = browser.find_element(By.XPATH, '//form/div[4]/input')
input4.send_keys("Russia")
button = browser.find_element_by_xpath("//form/div[6]/button[3]")
button.click()


    # успеваем скопировать код за 30 секунд
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()
