from selenium.webdriver.support.wait import WebDriverWait


class MainPage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/en/")
        return self

    def open_product_page(self):
        self.driver.find_element_by_css_selector('.listing-wrapper.products li:first-child').click()
        return self

    def open_cart(self):
        self.driver.find_element_by_css_selector('#cart > a.link').click()
        return self






