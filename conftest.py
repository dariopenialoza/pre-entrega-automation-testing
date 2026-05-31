import pytest
from selenium import webdriver
from page.login_page import LoginPage
from utils.data_reader import read_users_csv

#Configuración global para tener un usuario valido
# para todas la pruebas, evitando repetir el proceso de login en cada test.
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options= options)

    yield driver

    driver.quit()

@pytest.fixture
def driver_logged(driver):
    login_page = LoginPage(driver)
    user = read_users_csv()[0] # Obtener el primer usuario del CSV
    login_page.login(user["username"], user["password"])
    return driver