import random

from appium.webdriver.common.appiumby import AppiumBy


class ProductsPage:
    """ Locators for Products Page """
    products_title = (AppiumBy.XPATH, '//android.widget.TextView[@text="Products"]')

    sort_title = (AppiumBy.XPATH, '//android.widget.TextView[@text="Sort by:"]')
    sort_button = (AppiumBy.ACCESSIBILITY_ID, 'sort button')

    sort_by_price_asc = (AppiumBy.ACCESSIBILITY_ID, 'priceAsc')
    sort_by_price_desc = (AppiumBy.ACCESSIBILITY_ID, 'priceDesc')
    product_prices = (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="store item price"]')

    sort_by_name_asc = (AppiumBy.ACCESSIBILITY_ID, 'nameAsc')
    sort_by_name_desc = (AppiumBy.ACCESSIBILITY_ID, 'nameDesc')
    product_names = (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="store item text"]')

    star_rating = (AppiumBy.XPATH, f'(//android.view.ViewGroup[@content-desc='
                                   f'"review star {random.randint(1, 5)}"])[{random.randint(1, 4)}]')
    review_title = (AppiumBy.XPATH, '//android.widget.TextView[@text="Thank you for submitting your review!"]')
    close_modal_btn = (AppiumBy.ACCESSIBILITY_ID, 'Close Modal button')
    first_product = (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="store item text" '
                                     'and @text="Sauce Labs Backpack"]')
    second_product = (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="store item text" '
                                      'and @text="Sauce Labs Bike Light"]')
