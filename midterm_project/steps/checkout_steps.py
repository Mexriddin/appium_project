from pytest_check import check
from midterm_project.steps.base_step import BaseStep
from midterm_project.pages.my_cart_page import MyCartPage
from midterm_project.pages.checkout_page import CheckoutPage


class CheckOutSteps(BaseStep):
    """ Steps for Checkout Page """

    def open_checkout_page(self):
        """ Step opening empty my cart page """
        self.click_element(MyCartPage.proceed_to_checkout)

    def enter_shipping_address(self, address_data):
        """ Step entering shipping address"""
        self.fill(CheckoutPage.full_name_input, address_data.full_name)
        self.fill(CheckoutPage.address_line_1_input, address_data.address_line1)
        self.fill(CheckoutPage.city_input, address_data.city)
        self.fill(CheckoutPage.zip_code_input, address_data.zip_code)
        self.fill(CheckoutPage.country_input, address_data.country)

    def click_to_payment(self):
        """ Step clicking payment button"""
        self.click_element(CheckoutPage.to_payment_btn)

    def enter_card_data(self, card_data):
        """ Step entering card data"""
        self.fill(CheckoutPage.card_full_name_input, card_data.full_name)
        self.fill(CheckoutPage.card_number_input, card_data.card_number)
        self.fill(CheckoutPage.expiry_date_input, card_data.expiration_date)
        self.fill(CheckoutPage.security_code_input, card_data.cvv)

    def click_review_order(self):
        """ Step clicking review order"""
        self.click_element(CheckoutPage.review_order_btn)

    def review_delivery_address(self, delivery_address):
        """ Step reviews delivery address"""
        with check:
            assert delivery_address.full_name == self.get_text(CheckoutPage.full_name), (
                "Delivery full name is incorrect")
            assert delivery_address.address_line1 == self.get_text(CheckoutPage.address_line_1), (
                "Delivery address is incorrect")
            assert delivery_address.city == self.get_text(CheckoutPage.city), "City is incorrect"
            assert delivery_address.country in self.get_text(CheckoutPage.country_and_zip_code), "Country is incorrect"
            assert delivery_address.zip_code in self.get_text(CheckoutPage.country_and_zip_code), (
                "Zip code is incorrect")

    def review_payment_method(self, card_data):
        """ Step reviews payment method"""
        self.swipe_to_bottom_until_element_is_displayed(CheckoutPage.expiry_date)
        with check:
            assert card_data.full_name == self.get_text(CheckoutPage.card_full_name), "Card full name is incorrect"
            assert card_data.card_number == "".join(
                self.get_text(CheckoutPage.card_number).split(" ")), "Card number is incorrect"
            assert card_data.expiration_date in "".join(
                self.get_text(CheckoutPage.expiry_date).split("/")), "Expiry date is incorrect"

    def review_order_total_price(self):
        """ Step reviews order total price"""
        self.swipe_to_bottom_until_element_is_displayed(CheckoutPage.delivery_price)
        delivery_price = float(self.get_text(CheckoutPage.delivery_price).replace("$", ""))
        self.swipe_to_top_until_element_is_displayed(CheckoutPage.checkout_title)
        total_price = round(((float(self.get_text(CheckoutPage.product_price).replace("$", "")) *
                              int(self.get_text(CheckoutPage.total_number).split(" ")[0])) + delivery_price), 2)
        actual_total_price = float(self.get_text(CheckoutPage.total_price).replace("$", ""))
        assert total_price == actual_total_price, \
            f"Order total price is not calculated correctly\nExpected:{total_price} Actual:{actual_total_price}"

    def click_place_order(self):
        """ Step clicking place order"""
        self.click_element(CheckoutPage.place_order_btn)

    def check_complete(self):
        """ Check complete"""
        assert self.get_text(CheckoutPage.complete_title) == 'Checkout Complete', "The order is not completed"
