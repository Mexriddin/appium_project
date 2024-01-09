import pytest
from midterm_project.steps.api_calls_steps import ApiCallsSteps


class TestApiCalls:
    def test_api_devices(self, app):
        api_calls_steps = ApiCallsSteps(app)
        api_calls_steps.open_api_calls_page()
        api_calls_steps.call_devices()
        api_calls_steps.check_devices()

    @pytest.mark.negative
    @pytest.mark.parametrize('error', ['unauthorized', 'not_found'])
    def test_api_error(self, app, error):
        api_calls_steps = ApiCallsSteps(app)
        api_calls_steps.open_api_calls_page()
        api_calls_steps.call_devices_error(error)
        api_calls_steps.check_devices_error(error)