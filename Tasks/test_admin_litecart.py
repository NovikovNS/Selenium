import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def are_elements_present(driver, *args):
    return len(driver.find_elements(*args)) > 0


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver


def test_admin_litecart(driver):
    driver.get("http://localhost/litecart/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "box-apps-menu")))
    all_parts_menu = driver.find_elements_by_css_selector("ul#box-apps-menu > li")
    for i in range(len(all_parts_menu)):
        part_main_menu = driver.find_elements_by_css_selector("ul#box-apps-menu > li")
        part_main_menu[i].click()
        are_elements_present(driver, By.TAG_NAME, "h1")
        sub_menu = driver.find_elements_by_css_selector(".docs>li>a")
        for j in range(len(sub_menu)):
            part_sub_menu = driver.find_elements_by_css_selector('.docs>li>a')
            part_sub_menu[j].click()
            are_elements_present(driver, By.TAG_NAME, "h1")
