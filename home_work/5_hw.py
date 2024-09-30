from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# поиск элементов username, password, submit/login
username = driver.find_element(By.CSS_SELECTOR, '#user-name')
password = driver.find_element(By.CSS_SELECTOR, '#password')
submit = driver.find_element(By.CSS_SELECTOR, '#login-button')
if username is None or password is None or submit is None:
    print('Элемент(-ы) не найден(-ы)')
else:
    print('Элементы найдены')
