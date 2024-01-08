from appium.webdriver.common.appiumby import AppiumBy


class LoginPage:
    """ Locators for Login Page"""
    login_title = (AppiumBy.XPATH, '(//android.widget.TextView[@text="Login"])[1]')
    input_username = (AppiumBy.ACCESSIBILITY_ID, 'Username input field')
    input_password = (AppiumBy.ACCESSIBILITY_ID, 'Password input field')
    login_button = (AppiumBy.ACCESSIBILITY_ID, 'Login button')
    generic_err_msg = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="generic-error-message"]'
                                       '/android.widget.TextView')
    username_err_msg = (AppiumBy.XPATH, '//android.widget.TextView[@text="Username is required"]')
    password_err_msg = (AppiumBy.XPATH, '//android.widget.TextView[@text="Password is required"]')