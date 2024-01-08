import pytest

from midterm_project.steps.base_step import BaseStep
from midterm_project.pages.base_page import BasePage
from midterm_project.pages.api_calls_page import ApiCallsPage


class ApiCallsSteps(BaseStep):
    """ Steps for api calls page """

    def open_api_calls_page(self):
        """ Step opening api calls page """
        self.open_menus()
        self.click_element(BasePage().menu_item_api_calls)
        assert self.get_text(ApiCallsPage.api_calls_title) == "API calls"

    def call_devices(self):
        """ Step call the devices """
        self.click_element(ApiCallsPage.us_dc)

    def check_devices(self):
        """ Step check the devices"""
        devices_gr = self.elements_are_visible(ApiCallsPage.devices_gr)
        assert len(devices_gr) > 0

    def call_devices_error(self, error_type):
        """ Step call the devices with errors """
        if error_type == 'unauthorized':
            self.click_element(ApiCallsPage.unauthorized_btn)
        elif error_type == 'not_found':
            self.click_element(ApiCallsPage.not_found_btn)

    def check_devices_error(self, error_type):
        """ Step check call the devices with errors """
        if error_type == 'unauthorized':
            assert self.get_text(ApiCallsPage.unauthorized_msg) == 'Unauthorized'
        elif error_type == 'not_found':
            assert self.get_text(ApiCallsPage.not_found_msg) == 'Not found'


