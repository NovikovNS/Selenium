import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver

def test_new_windows(driver):
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    wait = WebDriverWait (driver, 5)

    driver.find_element_by_css_selector(".row a").click()
    main_window = driver.current_window_handle
    all_links = driver.find_elements_by_css_selector('form [target="_blank"]')

    for link in all_links:
        link.click()
        new_window = [i for i in driver.window_handles if i != main_window]
        wait.until(EC.new_window_is_opened(new_window))

        driver.switch_to.window(new_window[0])
        driver.close()
        driver.switch_to.window(main_window)