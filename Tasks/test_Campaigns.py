import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    driver = webdriver.Ie()
    request.addfinalizer(driver.quit)
    return driver


def test_campaigns(driver):
    driver.get("http://localhost/litecart/")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((
        By.CLASS_NAME, 'campaign-price')))

    # обычная цена на главной странице
    main_regular_price = driver.find_element_by_css_selector('#box-campaigns s.regular-price').get_attribute(
        'innerText')
    # акционная цена на главной странице
    main_stock_price = driver.find_element_by_css_selector('#box-campaigns strong.campaign-price').get_attribute(
        "innerText")
    # название продукта на главной странице
    main_name_product = driver.find_element_by_css_selector('#box-campaigns div.name').get_attribute(
        "innerText")
    # цвет обычной цены товара на главной странице
    color_main_regular_price = [int(element.strip("'()rgba")) for element in driver.find_element_by_css_selector(
        '#box-campaigns s.regular-price').value_of_css_property("color").split(
        ", ")]
    # цвет акционной цены товара на главной странице
    color_main_stock_price = [int(element.strip("'()rgba")) for element in driver.find_element_by_css_selector(
        '#box-campaigns strong.campaign-price').value_of_css_property("color").split(", ")]
    # размер обычной цены
    main_size_regular_price = driver.find_element_by_css_selector(
        '#box-campaigns s.regular-price').value_of_css_property("font-size")
    # размер акционной цены
    main_size_stock_price = driver.find_element_by_css_selector(
        '#box-campaigns strong.campaign-price').value_of_css_property("font-size")

    # проверка, что обычная цена зачёркнутая и серая на главной странице
    assert(driver.find_element_by_css_selector(
        '#box-campaigns s.regular-price').value_of_css_property("text-decoration-line") == 'line-through')
    assert (color_main_regular_price[0] == color_main_regular_price[1] == color_main_regular_price[2])

    # проверка, что акционная цена жирная и красная на главной странице
    assert (driver.find_element_by_css_selector(
        '#box-campaigns strong.campaign-price').value_of_css_property("font-weight") == '900' or '700')
    assert (color_main_stock_price[1] == color_main_stock_price[2] == 0)

    # проверка, что акционная цена крупнее обычной на главной странице
    assert (main_size_regular_price < main_size_stock_price)

    product_page = driver.find_element_by_css_selector('#box-campaigns li.product>a')
    product_page.click()

    # обычная цена на странице продукта
    product_regular_price = driver.find_element_by_css_selector('s.regular-price').get_attribute('innerText')
    # цвет обычной цены на странице продукта
    color_product_regular_price = [int(element.strip("'()rgba")) for element in driver.find_element_by_css_selector(
        's.regular-price').value_of_css_property("color").split(", ")]
    # акционная цена на странице продукта
    product_stok_price = driver.find_element_by_css_selector('strong.campaign-price').get_attribute('innerText')
    # цвет акционной цены на странице продукта
    color_product_stok_price = [int(element.strip("'()rgba")) for element in driver.find_element_by_css_selector(
        'strong.campaign-price').value_of_css_property("color").split(", ")]
    # название продукта на странице продукта
    product_name_product = driver.find_element_by_css_selector('h1').get_attribute('innerText')

    # проверка, что обычная цена зачёркнутая и серая на странице продукта
    assert (driver.find_element_by_css_selector(
        's.regular-price').value_of_css_property("text-decoration-line") == 'line-through')
    assert (color_product_regular_price[0] == color_product_regular_price[1] == color_product_regular_price[2])

    # проверка, что акционная цена жирная и красная на странице продукта
    assert (driver.find_element_by_css_selector(
        'strong.campaign-price').value_of_css_property("font-weight") == '900' or '700')
    assert (color_product_stok_price[1] == color_product_stok_price[2] == 0)

    # размер обычной цены на странице продукта
    product_size_regular_price = driver.find_element_by_css_selector(
        's.regular-price').value_of_css_property("font-size")

    # размер акционной цены на странице продукта
    product_size_stock_price = driver.find_element_by_css_selector(
        'strong.campaign-price').value_of_css_property("font-size")

    # проверка что акционная цена крупнее обычной на странице продукта
    assert (product_size_regular_price < product_size_stock_price)

    # проверка соответствия обычной цены на главной странице и на странице продукта
    assert (main_regular_price == product_regular_price)

    # проверка соответствия названия продукта на главной странице и на странице продукта
    assert (main_name_product == product_name_product)

    # проверка соответствия акционной цены на главной странице и на странице продукта
    assert (main_stock_price == product_stok_price)
