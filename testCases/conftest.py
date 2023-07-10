
import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    print("Launched in Chrome browser")
    return driver
