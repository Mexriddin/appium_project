from appium.webdriver.common.appiumby import AppiumBy


class ApiCallsPage:
    """Locators for Api Calls Page"""
    api_calls_title = (AppiumBy.XPATH, '//android.widget.TextView[@text="API calls"]')
    us_dc = (AppiumBy.XPATH, '//android.widget.TextView[@text="US-DC"]')
    devices = (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'
                               '/android.view.ViewGroup')
    unauthorized_btn = (AppiumBy.XPATH, '//android.widget.TextView[@text="401"]')
    unauthorized_msg = (AppiumBy.XPATH, '//android.widget.TextView[@text="Unauthorized"]')
    not_found_btn = (AppiumBy.XPATH, '//android.widget.TextView[@text="404"]')
    not_found_msg = (AppiumBy.XPATH, '//android.widget.TextView[@text="Not found"]')
