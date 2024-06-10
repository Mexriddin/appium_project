import allure
from selenium.common import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.webelement import WebElement as MobileElement
from selenium.webdriver.support import expected_conditions as EC
from midterm_project.pages.base_page import BasePage


class BaseStep:
    """Base common steps"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5, poll_frequency=1)

    @allure.step("Open the menu section")
    def open_menus(self):
        """ Step to open the menu section """
        self.click_element(BasePage.open_menu_btn)

    @allure.step("Click an element")
    def click_element(self, locator):
        """ Step to click an element """
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Fill an element")
    def fill(self, locator, text):
        """ Step fills element with text """
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def alert_is_present(self):
        """ Step returns alert if present """
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        return alert

    def elements_are_visible(self, locator):
        """ Step returns list elements visible """
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def is_element_present(self, locator):
        """ Steps returns true if element is present """
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_disappears_element(self, locator):
        """ Step wait disappears element """
        self.wait.until_not(EC.visibility_of_element_located(locator))

    def get_text(self, locator):
        """ Step returns text from element visible """
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    def get_center_of_element(self, element: MobileElement):
        location = element.location
        size = element.size

        center_x = location['x'] + size['width'] / 2
        center_y = location['y'] + size['height'] / 2

        return tuple((int(center_x), int(center_y)))

    @allure.step("Swipe to bottom until element")
    def swipe_to_bottom_until_element_is_displayed(self, locator):
        """ Step swipes to bottom until element is displayed"""
        while True:
            try:
                if self.driver.find_element(*locator).is_displayed():
                    break
            except NoSuchElementException:
                self.driver.swipe(100, 800, 100, 200, 300)

    @allure.step("Swipe to top until element")
    def swipe_to_top_until_element_is_displayed(self, locator):
        """ Step swipes to top until element is displayed"""
        while True:
            try:
                if self.driver.find_element(*locator).is_displayed():
                    break
            except NoSuchElementException:
                self.driver.swipe(100, 400, 100, 1000, 300)
