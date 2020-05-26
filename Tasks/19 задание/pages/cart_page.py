from selenium.webdriver.support.wait import WebDriverWait
import time


class CartPage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/en/checkout")
        return self

    def del_all_product_at_cart(self):
        quantity_products_cart = len(self.driver.find_elements_by_css_selector('.dataTable td.item'))
        time.sleep(2)
        self.driver.find_element_by_css_selector(".shortcut").click()

        while quantity_products_cart > 0:
            self.driver.find_element_by_name("remove_cart_item").click()
            self.driver.implicitly_wait(0)
            WebDriverWait(self.driver, 5).until(
                lambda a: len(a.find_elements_by_css_selector('.dataTable td.item')) == quantity_products_cart - 1)
            quantity_products_cart = len(self.driver.find_elements_by_css_selector(".dataTable td.item"))



