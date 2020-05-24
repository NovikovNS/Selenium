import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver


def test_log(driver):
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    wait = WebDriverWait(driver, 5)

    len_products = len(driver.find_elements_by_xpath('//td[./img and ./a]/a'))

    while len_products > 0:
        len_products -= 1
        product = driver.find_elements_by_xpath('//td[./img and ./a]/a')
        product[len_products].click()
        for l in driver.get_log("browser"):
            print(l)
        driver.back()
