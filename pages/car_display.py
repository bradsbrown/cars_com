from selenium.webdriver.common.by import By

from .base import BasePage


class CarDisplayPage(BasePage):
    CAR_TITLE = (By.CLASS_NAME, "vehicle-info__title")
    CHECK_AVAILABILITY = (By.CSS_SELECTOR, '[data-linkname="submit-email-lead"]')

    CONTACT_FIRST = (By.NAME, "fname")
    CONTACT_LAST = (By.NAME, "lname")
    CONTACT_EMAIL = (By.NAME, "email")

    PRICING_CALC = (By.CLASS_NAME, "vdp=pricing__container")

    def __init__(self, driver):
        self.driver = driver

    def listing_title(self):
        title = self.driver.find_element(*self.CAR_TITLE)
        return title.text

    def fill_contact(self, first_name, last_name, email):
        self.fill_value(self.CONTACT_FIRST, first_name)
        self.fill_value(self.CONTACT_LAST, last_name)
        self.fill_value(self.CONTACT_EMAIL, email)
