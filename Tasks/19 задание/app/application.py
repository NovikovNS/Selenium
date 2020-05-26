from selenium import webdriver
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage

class Application():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.product_page = ProductPage(self.driver)

    def quit(self):
        self.driver.quit()

    def add_products_to_cart(self, quantity_product):
        self.main_page.open()
        for i in range(quantity_product):
            self.main_page.open_product_page()
            self.product_page.add_product_to_cart()
            self.product_page.back_to_main_page()

    def delete_all_products_at_cart(self):
        self.main_page.open_cart()
        self.cart_page.del_all_product_at_cart()




