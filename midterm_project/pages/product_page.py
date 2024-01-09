from appium.webdriver.common.appiumby import AppiumBy


class ProductPage:
    """ Locators for Product Page """
    product_title = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="container header"]'
                                     '/android.widget.TextView')
    color_checkboxes = (AppiumBy.XPATH, '//android.view.ViewGroup[contains(@content-desc,"circle")]')
    counter_plus_btn = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="counter plus button"]')
    counter_minus_btn = (AppiumBy.ACCESSIBILITY_ID, 'counter minus button')
    counter_amount = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="counter amount"]'
                                      '/android.widget.TextView')
    add_to_cart_button = (AppiumBy.ACCESSIBILITY_ID, 'Add To Cart button')

