from midterm_project.steps.base_step import BaseStep
from midterm_project.pages.base_page import BasePage
from midterm_project.pages.api_calls_page import ApiCallsPage
import allure



class ApiCallsSteps(BaseStep):
    """ Steps for api calls page """

    @allure.step("Open API Calls page")
    def open_api_calls_page(self):
        """ Step opening api calls page """
        self.open_menus()
        self.click_element(BasePage().menu_item_api_calls, name="Api Calls section")
        assert self.get_text(ApiCallsPage.api_calls_title) == "API calls", "The API calls page did not open"

    @allure.step("Call the devices")
    def call_devices(self):
        """ Step call the devices """
        self.wait_disappears_element(ApiCallsPage.loading_dc)
        self.click_element(ApiCallsPage.us_dc, name="Devices tab")

    @allure.step("Check the devices is visible")
    def check_devices(self):
        """ Step check the devices"""
        devices_gr = self.elements_are_visible(ApiCallsPage.devices_gr)
        assert len(devices_gr) > 0, "Devices were not displayed"

    @allure.step("Call the devices with error:{error_type}")
    def call_devices_error(self, error_type):
        """ Step call the devices with errors """
        self.wait_disappears_element(ApiCallsPage.loading_dc)
        if error_type == 'unauthorized':
            self.click_element(ApiCallsPage.unauthorized_btn, "Unauthorized tab")
        elif error_type == 'not_found':
            self.click_element(ApiCallsPage.not_found_btn, "Not found tab")

    @allure.step("Check call the devices with error:{error_type}")
    def check_devices_error(self, error_type):
        """ Step check call the devices with errors """
        if error_type == 'unauthorized':
            assert self.get_text(ApiCallsPage.unauthorized_msg) == 'Unauthorized', \
                "Unauthorized error message is not displayed"
        elif error_type == 'not_found':
            assert self.get_text(ApiCallsPage.not_found_msg) == 'Not found', \
                "Not found error message is not displayed"