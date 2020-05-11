import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import string
import random


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver


def test_registration(driver):
    driver.get("https://localhost/litecart")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((
        By.NAME, 'login_form')))
    driver.find_element_by_css_selector("[name=login_form] a").click()

    email = ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(10)) + '@mail.ru'

    list_of_data = [
        ['firstname', 'test'],
        ['lastname', 'test'],
        ['address1', 'test'],
        ['postcode', '12345'],
        ['city', 'test'],
        ['email', email],
        ['phone', '+79990009900'],
        ['password', 'test'],
        ['confirmed_password', 'test']
    ]

    for i in list_of_data:
        driver.find_element_by_name(i[0]).send_keys(i[1])

    Select(driver.find_element_by_name('country_code')).select_by_value("US")
    driver.implicitly_wait(5)
    Select(driver.find_element_by_css_selector('select[name = zone_code]')).select_by_value('AK')

    driver.find_element_by_css_selector('[name = create_account]').click()
    driver.implicitly_wait(5)
    driver.find_element_by_css_selector('#box-account li:last-of-type a').click()

    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('password').send_keys('test' + Keys.ENTER)
    driver.implicitly_wait(5)
    driver.find_element_by_css_selector('#box-account li:last-of-type a').click()