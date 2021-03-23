import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CarsHomePage:
    URL = "https://cars.com"

    STOCK_TYPE = (By.NAME, "stockType")
    MAKE_TYPE = (By.NAME, "makeId")
    MODEL_TYPE = (By.NAME, "modelId")
    PRICE_MAX = (By.NAME, "priceMax")
    RADIUS = (By.NAME, "radius")
    ZIP_CODE = (By.NAME, "zip")
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[data-linkname^="Search "]')

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def select_dropdown_by_text(self, locator, text):
        select = Select(self.driver.find_element(*locator))
        select.select_by_visible_text(text)

    def fill_value(self, locator, value):
        el = self.driver.find_element(*locator)
        el.clear()
        el.send_keys(value)

    def submit(self):
        self.driver.find_element(*self.SEARCH_BUTTON).click()

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
