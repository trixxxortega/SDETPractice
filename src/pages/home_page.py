from selenium.webdriver.common.by import By

from core.Config import Config
from core.browser import Browser

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.logo = (By.XPATH, '//*[@id="container-bca776d573"]/div[1]/div[2]/div[1]/div[1]/a/img')

    def is_logo_displayed(self):
        return self.driver.find_element(*self.logo).is_displayed()

    def click_logo(self):
        self.driver.find_element(*self.logo).click()

    def is_logo_clickable(self):
        return self.driver.find_element(*self.logo).is_clickable()


