from selenium import webdriver
from selenium.webdriver.common.by import By

import time

my_email = ''
my_password = ''

try:
    link = 'https://stepik.org/lesson/236895/step/1'
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(3)
    browser.find_element(By.XPATH, '/html/body/header/nav/a[contains(@class, "navbar__auth_login")]').click()
    # browser.find_element(By.CSS_SELECTOR, '//div[contains(@class, "modal-dialog")]/input[@name="login"]').send_keys(my_email)
    browser.find_element(By.ID, 'id_login_email').send_keys(my_email)
    browser.find_element(By.ID, 'id_login_password').send_keys(my_password)

    button = browser.find_element(By.CLASS_NAME, "sign-form__btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(300)
    # закрываем браузер после всех манипуляций
    browser.quit()
