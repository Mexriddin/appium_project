import allure

from midterm_project.steps.base_step import BaseStep
from midterm_project.pages.base_page import BasePage


class LogoutSteps(BaseStep):
    """ Steps for log out"""

    @allure.step("Logout user")
    def logout(self):
        """ Step logout"""
        self.open_menus()
        self.click_element(BasePage.menu_item_logout)
        self.alert_is_present().accept()

    @allure.step("Check logout")
    def check_logout(self):
        """ Step check logout"""
        msg = self.alert_is_present().text
        assert msg == 'You are successfully logged out.', "User is not logged"
