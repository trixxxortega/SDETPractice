from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from core.Config import Config

class Browser:
    #
    def __init__(self):
        options = Options()
        options.binary_location = "/usr/bin/chromium"
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')  # si no necesitás ver la ventana

        self.driver = webdriver.Chrome(
            service=Service("/usr/bin/chromedriver"),
            options=options
        )

    def open(self, url=Config.BASE_URL):
        self.driver.get(url)

    def close(self):
        self.driver.quit()

    def quit(self):
        """Cierra el navegador."""
        if self.driver:
            self.driver.quit()