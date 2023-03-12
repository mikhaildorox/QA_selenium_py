from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '1.txt')
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('first')
    browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('last')
    browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('email')

    browser.find_element(By.CSS_SELECTOR, '[type="file"]').send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(6)
    browser.quit()
