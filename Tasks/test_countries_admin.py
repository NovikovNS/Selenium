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

def test_countries_admin(driver):
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "content")))
    list_countries = [i.get_attribute('innerText') for i in driver.find_elements_by_css_selector(
        'tr.row a:not([title = Edit])')]
    assert (list_countries == sorted(list_countries))

    list_countries_zones = [i.get_attribute('outerText') for i in driver.find_elements_by_css_selector('td:nth-child(6)')]
    list_index_countries_zones = [list_countries_zones.index(i) for i in list_countries_zones if i != '0']

    for index_country_zones in list_index_countries_zones:
        country_with_zones = driver.find_elements_by_css_selector('tr.row a:not([title = Edit])')
        country_with_zones[index_country_zones].click()
        list_zones = [i.get_attribute('textContent') for i in driver.find_elements_by_css_selector(
            '#table-zones tr>td:nth-child(3)') if i.get_attribute('textContent') != '']
        assert (list_zones == sorted(list_zones))
        driver.back()


def test_zones_admin(driver):
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    WebDriverWait(driver, 5).until(
       EC.presence_of_element_located((By.CLASS_NAME, "row")))

    countries_list = len(driver.find_elements_by_css_selector('tr.row'))

    while countries_list:
        countries_list -= 1
        country_zones = driver.find_elements_by_css_selector('td:nth-child(3)>a')
        country_zones[countries_list].click()
        zone_lists = [i.get_attribute('textContent') for i in driver.find_elements_by_css_selector('td:nth-child(3)>select option[selected]')]
        assert (zone_lists == sorted(zone_lists))
        driver.back()