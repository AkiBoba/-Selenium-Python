from selenium import webdriver

link = "http://suninjuly.github.io/registration1.html"

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)

try:
    input_first = browser.find_elements_by_xpath('//form//div/div/input')
    for i in range(1, len(input_first)-1):
        input1 = browser.find_element_by_xpath(f'//form//div[{i}]/input')
        input1.send_keys("first")
except Exception as e:
    print('Test first Fail', e)
try:
    input_second = browser.find_elements_by_css_selector('.second_block input')
    for i in range(1, len(input_second)+1):
        input_second = browser.find_element_by_css_selector(f'.second_block :nth-child({i}) input')
        input_second.send_keys("second")
except Exception as e:
    print('Test second Fail', e)
try:
    button = browser.find_element_by_tag_name("button")
    button.click()
except Exception as e:
    print('Test submit Fail', e)
#


browser.quit()
