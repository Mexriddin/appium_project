import pytest
from midterm_project.steps.api_calls_steps import ApiCallsSteps
import allure


@allure.epic("Api calls")
class TestApiCalls:
    @allure.title("The test call all devices")
    @allure.description(" A test calling all devices from the API")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_api_call_devices(self, app):
        api_calls_steps = ApiCallsSteps(app)
        api_calls_steps.open_api_calls_page()
        api_calls_steps.call_devices()
        api_calls_steps.check_devices()

    @allure.title("The test is an negative call:{error}")
    @allure.description("A negative test that calls all devices")
    @pytest.mark.negative
    @pytest.mark.parametrize('error', ['unauthorized', 'not_found'])
    def test_api_call_with_error(self, app, error):
        api_calls_steps = ApiCallsSteps(app)
        api_calls_steps.open_api_calls_page()
        api_calls_steps.call_devices_error(error)
        api_calls_steps.check_devices_error(error)