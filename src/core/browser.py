from selenium import webdriver
from src.core.Config import Config

class Browser:
    #
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open(self, url=Config.BASE_URL):
        self.driver.get(url)

    def close(self):
        self.driver.quit()

    def quit(self):
        """Cierra el navegador."""
        if self.driver:
            self.driver.quit()