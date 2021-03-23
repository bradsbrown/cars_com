import json

from selenium.webdriver.common.by import By


class CarsResultsPage:
    FILTERS_CONTAINER = (By.CLASS_NAME, "breadcrumbs")
    FILTERS = (By.CLASS_NAME, "breadcrumb")

    def __init__(self, driver):
        self.driver = driver

    def get_filters(self):
        container = self.driver.find_element(*self.FILTERS_CONTAINER)
        filters = container.find_elements(*self.FILTERS)
        filter_data = list(
            map(lambda f: json.loads(f.get_attribute("data-dtm")), filters)
        )
        return filter_data
