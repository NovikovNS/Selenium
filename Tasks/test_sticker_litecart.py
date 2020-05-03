import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver

def test_sticker_litecart(driver):
    driver.get("http://localhost/litecart/")
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "li.product")))
    driver.find_element_by_css_selector("li.product")
    products = driver.find_elements_by_css_selector("li.product")
    for product in products:
        stickers = product.find_elements_by_css_selector(".sticker")
        assert (len(stickers) == 1)