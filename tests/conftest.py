from pip._internal.operations.build import wheel_editable
from selenium import webdriver
import pytest

@pytest.fixture(autouse=True,scope='session')
def fixture_func():
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('detach', True)
    opt.add_argument('--disable-notifications')
    driver = webdriver.Chrome(options=opt)
    driver.maximize_window()
    driver.get("https://www.tatacliq.com/")
    yield driver
    driver.quit()