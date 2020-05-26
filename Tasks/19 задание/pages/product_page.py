from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

class ProductPage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_to_cart(self):
        count_of_product = int(self.driver.find_element_by_css_selector('span.quantity').get_attribute('innerText'))
        try:
            self.driver.implicitly_wait(0)
            self.driver.find_element_by_name("options[Size]")
            Select(self.driver.find_element_by_name('options[Size]')).select_by_value('Small')
        except NoSuchElementException:
            pass
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_css_selector('[value="Add To Cart"]').click()
        WebDriverWait(self.driver, 5).until(
            lambda a: int(
                self.driver.find_element_by_css_selector(
                    'span.quantity').get_attribute('innerText')) == count_of_product + 1)
        count_of_product = self.driver.find_element_by_css_selector('span.quantity')

    def back_to_main_page(self):
        self.driver.get("http://localhost/litecart/en/")
