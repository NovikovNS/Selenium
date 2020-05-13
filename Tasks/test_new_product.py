import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import os
import random
import string

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver

def test_countries_admin(driver):
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()


    driver.find_element_by_xpath('//span[.="Catalog"]').click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//a[contains(.,"Add New Product")]').click()
#   заполнение вкладки General
    driver.find_element_by_css_selector('[name="status"][value="1"]').click()
    test_product = ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(5)) + '_duck'
    driver.find_element_by_name('name[en]').send_keys(test_product)
    driver.find_element_by_name('code').send_keys('test_code')
    driver.find_element_by_css_selector('input[type="checkbox"][value="1-1"]').click()
    driver.find_element_by_name('quantity').clear()
    driver.find_element_by_name('quantity').send_keys('100')
    Select(driver.find_element_by_name('quantity_unit_id')).select_by_value("1")
    Select(driver.find_element_by_name('delivery_status_id')).select_by_value("1")
    Select(driver.find_element_by_name('sold_out_status_id')).select_by_value("2")
    driver.find_element_by_name('new_images[]').send_keys(
        os.path.abspath(r"test_duck.jpg"))
    driver.find_element_by_name('date_valid_from').send_keys('12052020')
    driver.find_element_by_name('date_valid_to').send_keys('29052020')

    driver.find_element_by_xpath('//a[.="Information"]').click()

#   заполнение вкладки Information
    driver.implicitly_wait(5)
    Select(driver.find_element_by_name('manufacturer_id')).select_by_value("1")
    driver.find_element_by_name('keywords').send_keys('keywords_test')
    driver.find_element_by_name('short_description[en]').send_keys('short_test')
    driver.find_element_by_class_name('trumbowyg-editor').send_keys('Тестовый товар. Описание')
    driver.find_element_by_name('head_title[en]').send_keys('head_test')
    driver.find_element_by_name('meta_description[en]').send_keys('meta_test')

    driver.find_element_by_xpath('//a[.="Prices"]').click()

#   заполнение вкладки Prices
    driver.implicitly_wait(5)
    driver.find_element_by_name('purchase_price').clear()
    driver.find_element_by_name('purchase_price').send_keys('10')
    Select(driver.find_element_by_name('purchase_price_currency_code')).select_by_value("USD")
    driver.find_element_by_name('gross_prices[USD]').clear()
    driver.find_element_by_name('gross_prices[USD]').send_keys('5')
    driver.find_element_by_name('gross_prices[EUR]').clear()
    driver.find_element_by_name('gross_prices[EUR]').send_keys('5')

    driver.find_element_by_css_selector('button[name="save"]').click()

#   проверка появления товара
    driver.find_element_by_css_selector('input[name="query"]').send_keys(test_product + Keys.ENTER)
    driver.find_element_by_link_text(test_product).click()
