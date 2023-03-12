from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(int(num1)))
    browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()

    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()
