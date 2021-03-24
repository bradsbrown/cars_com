import json

from selenium.webdriver.common.by import By

from .base import BasePage


class CarsResultsPage(BasePage):
    NEW_BUTTON = (By.ID, "stkTypId-28880")
    TOURING_8_PASS = (By.ID, "trId-36434822")

    FILTERS_CONTAINER = (By.CLASS_NAME, "breadcrumbs")
    FILTERS = (By.CLASS_NAME, "breadcrumb")

    RESULT_LISTINGS = (By.CLASS_NAME, "listings")
    RESULT_ENTRIES = (By.CLASS_NAME, "shop-srp-listings__listing-container")
    RESULT_IMAGE = (By.CLASS_NAME, "listing-row__photo-container")

    def get_filters(self):
        container = self.driver.find_element(*self.FILTERS_CONTAINER)
        filters = container.find_elements(*self.FILTERS)
        filter_data = list(
            map(lambda f: json.loads(f.get_attribute("data-dtm")), filters)
        )
        return filter_data

    def find_filter_value_by_name(self, name):
        filters = self.get_filters()
        filter = [f for f in filters if f["name"] == name]
        assert filter, f'No "{name}" filter found!'
        filter_value = filter[0]["value"]
        return filter_value

    def get_results(self):
        listing_container = self.driver.find_element(*self.RESULT_LISTINGS)
        results = listing_container.find_elements(*self.RESULT_ENTRIES)
        return results

    def select_result(self, index):
        results = self.get_results()
        results[index].find_element(*self.RESULT_IMAGE).click()
