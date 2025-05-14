import pytest
from selenium.webdriver.support.wait import WebDriverWait

from core.browser import Browser

from pages.home_page import HomePage

from core.Config import Config

from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def setup():
    browser = Browser()
    browser.open(Config.BASE_URL)
    yield browser.driver
    browser.quit()


@pytest.mark.smoke
def test_logo_is_displayed(setup):
    home_page = HomePage(setup)
    assert home_page.is_logo_displayed() is True


@pytest.mark.smoke
def test_logo_is_clickable(setup):
    home_page = HomePage(setup)
    logo = WebDriverWait(setup, 10).until(
        EC.element_to_be_clickable(home_page.logo))
    logo.click()
