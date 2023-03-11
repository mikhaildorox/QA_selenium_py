from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)
    summ = num2 + num1
    print(summ)
    Select(browser.find_element(By.TAG_NAME, 'select')).select_by_value(str(summ))

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()