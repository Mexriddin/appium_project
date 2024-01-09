from appium.webdriver.common.appiumby import AppiumBy


class CheckoutPage:
    """ Locators for Checkout Page """
    full_name_input = (AppiumBy.ACCESSIBILITY_ID, 'Full Name* input field')
    address_line_1_input = (AppiumBy.ACCESSIBILITY_ID, 'Address Line 1* input field')
    city_input = (AppiumBy.ACCESSIBILITY_ID, 'City* input field')
    zip_code_input = (AppiumBy.ACCESSIBILITY_ID, 'Zip Code* input field')
    country_input = (AppiumBy.ACCESSIBILITY_ID, 'Country* input field')
    to_payment_btn = (AppiumBy.ACCESSIBILITY_ID, 'To Payment button')

    card_full_name_input = (AppiumBy.ACCESSIBILITY_ID, 'Full Name* input field')
    card_number_input = (AppiumBy.ACCESSIBILITY_ID, 'Card Number* input field')
    expiry_date_input = (AppiumBy.ACCESSIBILITY_ID, 'Expiration Date* input field')
    security_code_input = (AppiumBy.ACCESSIBILITY_ID, 'Security Code* input field')
    review_order_btn = (AppiumBy.ACCESSIBILITY_ID, 'Review Order button')
    place_order_btn = (AppiumBy.ACCESSIBILITY_ID, 'Place Order button')
    complete_title = (AppiumBy.XPATH, '//android.widget.TextView[@text="Checkout Complete"]')