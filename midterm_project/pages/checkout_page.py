from appium.webdriver.common.appiumby import AppiumBy


class CheckoutPage:
    """ Locators for Checkout Page """
    checkout_title = (AppiumBy.XPATH, '//android.widget.TextView[@text="Checkout"]')

    # Shipping address form
    full_name_input = (AppiumBy.ACCESSIBILITY_ID, 'Full Name* input field')
    address_line_1_input = (AppiumBy.ACCESSIBILITY_ID, 'Address Line 1* input field')
    city_input = (AppiumBy.ACCESSIBILITY_ID, 'City* input field')
    zip_code_input = (AppiumBy.ACCESSIBILITY_ID, 'Zip Code* input field')
    country_input = (AppiumBy.ACCESSIBILITY_ID, 'Country* input field')
    to_payment_btn = (AppiumBy.ACCESSIBILITY_ID, 'To Payment button')

    # Payment method form
    card_full_name_input = (AppiumBy.ACCESSIBILITY_ID, 'Full Name* input field')
    card_number_input = (AppiumBy.ACCESSIBILITY_ID, 'Card Number* input field')
    expiry_date_input = (AppiumBy.ACCESSIBILITY_ID, 'Expiration Date* input field')
    security_code_input = (AppiumBy.ACCESSIBILITY_ID, 'Security Code* input field')
    review_order_btn = (AppiumBy.ACCESSIBILITY_ID, 'Review Order button')

    # Shipping address checkout texts
    full_name = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="checkout delivery address"]'
                                 '/android.widget.TextView[2]')
    address_line_1 = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="checkout delivery address"]'
                                      '/android.widget.TextView[3]')
    city = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="checkout delivery address"]'
                            '/android.widget.TextView[4]')
    country_and_zip_code = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="checkout delivery address"]'
                                            '/android.widget.TextView[5]')

    # Payment method checkout texts
    card_full_name = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="checkout payment info"]'
                                      '/android.widget.TextView[2]')
    card_number = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="checkout payment info"]'
                                   '/android.widget.TextView[3]')
    expiry_date = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="checkout payment info"]'
                                   '/android.widget.TextView[4]')

    product_price = (AppiumBy.ACCESSIBILITY_ID, 'product price')
    total_number = (AppiumBy.ACCESSIBILITY_ID, 'total number')
    delivery_price = (AppiumBy.XPATH, '//android.widget.TextView[@text="$5.99"]')
    total_price = (AppiumBy.ACCESSIBILITY_ID, 'total price')

    place_order_btn = (AppiumBy.ACCESSIBILITY_ID, 'Place Order button')
    complete_title = (AppiumBy.XPATH, '//android.widget.TextView[@text="Checkout Complete"]')
