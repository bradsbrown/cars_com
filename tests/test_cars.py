import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Safari

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
        {"name": "New/Used", "value": "Used"}
    ]


def test_case(driver, expected_filters):
    # Place Search
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
    filters = results.get_filters()
    assert len(filters) == 4
    assert all((f in filters for f in expected_filters))

    breakpoint()
