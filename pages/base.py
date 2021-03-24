from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def select_dropdown_by_text(self, locator, text):
        select = Select(
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        )
        select.select_by_visible_text(text)

    def fill_value(self, locator, value):
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        el.clear()
        el.send_keys(value)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def scroll_to(self, locator):
        el = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(el)
        actions.perform()
