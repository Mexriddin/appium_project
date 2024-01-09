from midterm_project.steps.base_step import BaseStep
from midterm_project.pages.base_page import BasePage


class LogoutSteps(BaseStep):
    """ Steps for log out"""

    def logout(self):
        """ Step logout"""
        self.open_menus()
        self.click_element(BasePage.menu_item_logout)
        self.alert_is_present().accept()

    def check_logout(self):
        """ Step check logout"""
        msg = self.alert_is_present().text
        assert msg == 'You are successfully logged out.', "User is not logged"
