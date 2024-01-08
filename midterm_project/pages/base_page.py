from appium.webdriver.common.appiumby import AppiumBy


class BasePage:
    """ Locators for Base Page """
    open_menu_btn = (AppiumBy.ACCESSIBILITY_ID, 'open menu')
    menu_item_login = (AppiumBy.ACCESSIBILITY_ID, 'menu item log in')
    menu_item_logout = (AppiumBy.ACCESSIBILITY_ID, 'menu item log out')
    menu_item_catalog = (AppiumBy.ACCESSIBILITY_ID, 'menu item catalog')
    menu_item_api_calls = (AppiumBy.ACCESSIBILITY_ID, 'menu item api calls')

    cart_badge = (AppiumBy.ACCESSIBILITY_ID, 'cart badge')
    cart_item_count = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="cart badge"]'
                                       '/android.widget.TextView')
