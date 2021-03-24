from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base import BasePage


class CarsHomePage(BasePage):
    URL = "https://cars.com"

    STOCK_TYPE = (By.NAME, "stockType")
    MAKE_TYPE = (By.NAME, "makeId")
    MODEL_TYPE = (By.NAME, "modelId")
    PRICE_MAX = (By.NAME, "priceMax")
    RADIUS = (By.NAME, "radius")
    ZIP_CODE = (By.NAME, "zip")
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[data-linkname^="Search "]')

    def load(self):
        self.driver.get(self.URL)

    def submit(self):
        current_url = self.driver.current_url
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        WebDriverWait(self.driver, 10).until(EC.url_changes(current_url))

    def place_search(
        self, stock_type, make_type, model_type, price_max, radius, zip_code
    ):
        self.select_dropdown_by_text(self.STOCK_TYPE, stock_type)
        self.select_dropdown_by_text(self.MAKE_TYPE, make_type)
        self.select_dropdown_by_text(self.MODEL_TYPE, model_type)
        self.select_dropdown_by_text(self.PRICE_MAX, price_max)
        self.select_dropdown_by_text(self.RADIUS, radius)
        self.fill_value(self.ZIP_CODE, zip_code)
        self.submit()
