import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver

def test_cart(driver):
    driver.get("https://localhost/litecart")
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 5)
#   количество продуктов, добавляемых в корзину
    quantity_product = 3

#   добавление продуктов в корзину
    for i in range(quantity_product):
        driver.find_element_by_css_selector('.listing-wrapper.products li:first-child').click()
        quantity = int(driver.find_element_by_css_selector('span.quantity').get_attribute('innerText'))
        try:
            driver.implicitly_wait(0)
            driver.find_element_by_name("options[Size]")
            Select(driver.find_element_by_name('options[Size]')).select_by_value('Small')
        except NoSuchElementException:
            pass
        driver.implicitly_wait(5)
        driver.find_element_by_css_selector('[value="Add To Cart"]').click()
        wait.until(
            lambda a: int(driver.find_element_by_css_selector('span.quantity').get_attribute('innerText')) == quantity+1)
        quantity = driver.find_element_by_css_selector('span.quantity')
        driver.back()

#   удаление продуктов из корзины
    driver.find_element_by_css_selector('#cart > a.link').click()

    quantity_products_cart = len(driver.find_elements_by_css_selector('.dataTable td.item'))
    time.sleep(2)
    driver.find_element_by_css_selector(".shortcut").click()

    while quantity_products_cart > 0:
        driver.find_element_by_name("remove_cart_item").click()
        driver.implicitly_wait(0)
        wait.until(
            lambda a: len(a.find_elements_by_css_selector('.dataTable td.item')) == quantity_products_cart-1)
        quantity_products_cart = len(driver.find_elements_by_css_selector(".dataTable td.item"))




