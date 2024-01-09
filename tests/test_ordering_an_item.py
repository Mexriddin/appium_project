import pytest

from midterm_project.steps.products_steps import ProductsSteps
from midterm_project.steps.product_steps import ProductSteps
from midterm_project.steps.my_cart_steps import MyCartSteps
from midterm_project.steps.login_steps import LoginSteps
from midterm_project.steps.checkout_steps import CheckOutSteps
from midterm_project.utils.utils import generate_shipping_address, generate_card_data, get_valid_login_data


class TestBuyProduct:
    @pytest.mark.smoke
    def test_ordering_an_item(self, app):
        products_step = ProductsSteps(app)
        products_step.open_products_page()

        product_steps = ProductSteps(app)
        product_steps.open_product_page()
        product_steps.choose_color('black')
        product_steps.plus_counter()
        product_steps.add_to_cart()

        my_cart_steps = MyCartSteps(app)
        my_cart_steps.open_my_cart_page()

        checkout_steps = CheckOutSteps(app)
        checkout_steps.open_checkout_page()

        login_steps = LoginSteps(app)
        login_data = get_valid_login_data()
        login_steps.login(login_data.username, login_data.password)

        shipping_address = generate_shipping_address()
        checkout_steps.enter_shipping_address(shipping_address)
        checkout_steps.click_to_payment()

        card_data = generate_card_data()
        checkout_steps.enter_card_data(card_data)
        checkout_steps.click_review_order()

        checkout_steps.review_delivery_address(shipping_address)
        checkout_steps.review_payment_method(card_data)
        checkout_steps.review_order_total_price()

        checkout_steps.click_place_order()
        checkout_steps.check_complete()



