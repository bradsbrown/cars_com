import pytest
from selenium.webdriver import Chrome

from pages.car_display import CarDisplayPage
from pages.cars_home import CarsHomePage
from pages.cars_results import CarsResultsPage


@pytest.fixture
def driver():
    driver = Chrome()
    driver.set_window_size(1600, 1200)
    return driver


@pytest.fixture
def expected_filters():
    return [
        {"name": "Max Price", "value": "$50,000"},
        {"name": "Make", "value": "Honda"},
        {"name": "Model", "value": "Pilot"},
        {"name": "New/Used", "value": "Used"},
    ]


def test_results_page(driver, expected_filters):
    """Complete validation on search results page."""
    # Load home page and fill out search
    home = CarsHomePage(driver)
    home.load()
    home.place_search(
        stock_type="Used Cars",
        make_type="Honda",
        model_type="Pilot",
        price_max="$50,000",
        radius="100 Miles from",
        zip_code="60008",
    )

    results = CarsResultsPage(driver)

    # Check Filters to ensure expected count and values
    filters = results.get_filters()
    assert len(filters) == 4
    assert all((f in filters for f in expected_filters))

    # Select New radio button and verify New is displayed
    results.click(results.NEW_BUTTON)
    new_used_value = results.find_filter_value_by_name("New/Used")
    failure_msg = f'Expected "New/Used" value: "New", Actual: {new_used_value}'
    assert new_used_value == "New", failure_msg

    # Select Touring 8-Passenger from Trim and validate filter
    results.click(results.TOURING_8_PASS)
    trim_value = results.find_filter_value_by_name("Trim")
    failure_msg = f'Expected "Trim" value: "Touring 8-Passenger", Actual: {trim_value}'
    assert trim_value == "Touring 8-Passenger", failure_msg

    # Select the 2nd entry
    results.select_result(1)
    car_page = CarDisplayPage(driver)

    # Validate car title
    title = car_page.listing_title()
    expected = "Honda Pilot 8-Passenger For Sale"
    failure_msg = f"Title mismatch -- Expected: {expected}, Actual: {title}"
    assert title == expected, failure_msg

    # validate check availability button
    avail_button = car_page.driver.find_element(*car_page.CHECK_AVAILABILITY)
    assert avail_button, "Check Availability button not found!"

    # Fill in Contact Seller section
    car_page.fill_contact(
        first_name="Car", last_name="Owner", email="carowner@yahoo.com"
    )

    # Scroll to Payment Calculator and screenshot
    car_page.scroll_to(car_page.PRICING_CALC)
    car_page.driver.save_screenshot("screenshot.png")
