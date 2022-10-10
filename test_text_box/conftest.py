import pytest
from selene.support.shared import browser

@pytest.fixture(scope='function', autouse=True)
def browser_managment():
    # конфигурация браузера
    browser.config.timeout = 1  # меняем тайм аут для всех команд
    browser.config.base_url='https://demoqa.com'
    browser.config.browser_name='chrome'
    browser.config.window_height = 900
    browser.config.window_width = 1200


    #browser.config.driver=   #для настройки браузера

