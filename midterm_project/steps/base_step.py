from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from midterm_project.pages.base_page import BasePage


class BaseStep:
    """Base steps"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5, poll_frequency=1)

    def open_menus(self):
        """ Step to open the menu section """
        self.click_element(BasePage.open_menu_btn)

    def click_element(self, locator):
        """ Step to click an element """
        self.wait.until(EC.element_to_be_clickable(locator)).click()

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
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def element_is_disappear(self, locator):
        """ Step wait disappears element """
        self.wait.until_not(EC.visibility_of_element_located(locator))

    def get_text(self, locator):
        """ Step returns text from element visible """
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text
