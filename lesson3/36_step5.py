import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

uncorrected_results = []

my_email = ''
my_password = ''

list_of_subpages = ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905']


def get_time_fun():
    return math.log(int(time.time()))  # вычисляет и возвращает время


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()  # запуск до каждой test_* функции
    browser.implicitly_wait(10)  # WebDriver Ждет ответ каждые 10s и пытается найти элемент каждые 500ms
    yield browser
    print("\nquit browser..")
    browser.quit()  # выполняется после каждой test_* функции
    print(''.join(uncorrected_results))


@pytest.mark.parametrize('page_num', list_of_subpages)
def test_solving_task(browser, page_num):  # запуск каждой страницы из списка
    link = "https://stepik.org/lesson/{}/step/1".format(page_num)
    browser.get(link)
    browser.find_element(By.XPATH, '/html/body/header/nav/a[contains(@class, "navbar__auth_login")]').click()
    browser.find_element(By.ID, 'id_login_email').send_keys(my_email)
    browser.find_element(By.ID, 'id_login_password').send_keys(my_password)
    WebDriverWait(browser, 55).until(EC.visibility_of_element_located((By.CLASS_NAME, "sign-form__btn"))).click()

    time.sleep(5)

    if browser.find_element(By.CLASS_NAME, 'again-btn'):
        browser.find_element(By.CLASS_NAME, 'again-btn').click()
        time.sleep(1)
    quiz_textarea = WebDriverWait(browser, 55) \
        .until(EC.visibility_of_element_located((By.CLASS_NAME, 'string-quiz__textarea')))
    quiz_textarea.clear()

    quiz_textarea.send_keys(str(get_time_fun()))
    WebDriverWait(browser, 55).until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission'))).click()
    option_text = WebDriverWait(browser, 55) \
        .until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="smart-hints__hint"]'))).text
    if option_text != "Correct!":
        uncorrected_results.append(option_text)
    assert "Correct!" == option_text, f'Error: {option_text}'


if __name__ == "__main__":
    pytest.main()
