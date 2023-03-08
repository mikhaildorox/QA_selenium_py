from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"
link_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.PARTIAL_LINK_TEXT, link_text).click()
    browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
    browser.find_element(By.NAME, "last_name").send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
