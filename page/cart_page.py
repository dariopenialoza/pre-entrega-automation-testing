from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

        # Selectores
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.cart_items_name = (By.CLASS_NAME, "inventory_item_name")
        self.cart_items_price = (By.CLASS_NAME, "inventory_item_price")
        #self.checkout_button = (By.ID, "checkout")

    def obtener_productos_carrito(self):
        items = self.driver.find_elements(*self.cart_items)
        productos = []
        for item in items:
            nombre = item.find_element(*self.cart_items_name).text
            precio = item.find_element(*self.cart_items_price).text
            productos.append(
                    {
                        "nombre": nombre, 
                        "precio": precio
                    }
            )
        return productos

