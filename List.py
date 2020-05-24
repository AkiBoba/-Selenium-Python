from selenium import webdriver
from selenium.webdriver.support.ui import Select

sum = 0
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")
x = browser.find_elements_by_css_selector("[id*='num']")
for i in x:
    sum += int(i.text)

# list = browser.find_elements_by_xpath('//select/option')
select = Select(browser.find_element_by_tag_name("select"))
# for i in list:
#     if i.text.isdigit():
#         if int(i.text) == sum:
#             print(i.text)
#             select.select_by_value(i.text)
            # break
select.select_by_value(str(sum))
press1 = browser.find_element_by_xpath('//button')
press1.click()
print(browser.switch_to.alert.text)

browser.quit()
