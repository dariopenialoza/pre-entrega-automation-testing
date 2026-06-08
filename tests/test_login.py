#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

from page.login_page import LoginPage
from utils.logger import logger

def test_login_ok(driver):
    logger.info("Inicializando el driver para test_login_ok")

    login_page = LoginPage(driver)

    logger.info("Ingresando los datos de entrada para la prueba")
    login_page.login("standard_user","secret_sauce")

    logger.info("Iniciando sesion ...")
    
    assert "/inventory.html" in driver.current_url, "No se redirigío al inventario."
    logger.info("Sesion iniciada correctamente.")

def test_login_error(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user","123456")
    error_message = login_page.get_error_password()
    #assert "Epic sadface: Username and password do not match any user in this service" in error_message
    assert error_message == "hola"