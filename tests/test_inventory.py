from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from page.inventory_page import InventoryPage
from page.login_page import LoginPage

@pytest.fixture
def driver_logged(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user","secret_sauce")

    return InventoryPage(driver)

def test_inventory_title(driver_logged):
    titulo = driver_logged.obtener_titulo()
    assert titulo == "Swag Labs", "El título de la página no es correcto."

def test_productos_visibles(driver_logged):
    productos = driver_logged.obtener_productos()
    assert len(productos) > 0, "No se encontraron productos en el inventario."

def test_ui_elements(driver_logged):
    assert driver_logged.menu_visible(), "El menú no está visible."
    assert driver_logged.filtro_visible(), "El filtro no está visible."

