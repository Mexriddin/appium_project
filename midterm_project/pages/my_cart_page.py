from appium.webdriver.common.appiumby import AppiumBy


class MyCartPage:
    """ Locators for My Cart Page """
    my_cart_title = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="container header"]'
                                     '/android.widget.TextView')
    counter_amount = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="counter amount"]'
                                      '/android.widget.TextView')
    total_number = (AppiumBy.ACCESSIBILITY_ID, 'total number')
    product_price = (AppiumBy.ACCESSIBILITY_ID, 'product price')
    total_price = (AppiumBy.ACCESSIBILITY_ID, 'total price')
    proceed_to_checkout = (AppiumBy.ACCESSIBILITY_ID, 'Proceed To Checkout button')