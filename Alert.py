from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")
press1 = browser.find_element_by_xpath('//form//button')
press1.click()
alert = browser.switch_to.alert
alert.accept()
var_x = browser.find_element_by_id('input_value')
x = var_x.text
input = browser.find_element_by_xpath('//input')
input.send_keys(f'{calc(x)}')
button = browser.find_element_by_xpath('//button')
button.click()
print(browser.switch_to.alert.text)
browser.quit()