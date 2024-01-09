from midterm_project.pages.product_page import ProductPage
from midterm_project.pages.products_page import ProductsPage
from midterm_project.steps.base_step import BaseStep
from midterm_project.pages.base_page import BasePage
from midterm_project.pages.my_cart_page import MyCartPage


class MyCartSteps(BaseStep):
    """ Steps for My Cart Page """

    def open_my_cart_page(self):
        """ Step opening empty my cart page """
        self.click_element(BasePage.cart_badge)

    def check_empty_my_cart(self):
        """ Step checking empty My cart"""
        assert self.get_text(MyCartPage.my_cart_title) == "No Items"

    def open_not_empty_my_cart_page(self):
        """ Step opening not empty My cart """
        self.click_element(ProductsPage.first_product)
        self.click_element(ProductPage.add_to_cart_button)
        self.click_element(BasePage.cart_badge)

    def plus_counter(self, plus=1):
        """ Step plus counter product """
        for _ in range(plus):
            self.click_element(ProductPage.counter_plus_btn)
            print(self.get_text(ProductPage.counter_amount))
        assert self.get_text(ProductPage.counter_amount) == str(1+plus)

    def check_update_count(self):
        """ Step checking update counter product """
        assert self.get_text(MyCartPage.counter_amount) == self.get_text(MyCartPage.total_number).split(" ")[0]

    def check_total_price(self):
        """ Step checking total price """
        count = int(self.get_text(MyCartPage.counter_amount))
        cost = float(self.get_text(MyCartPage.product_price).replace("$", ""))
        assert count * cost == float(self.get_text(MyCartPage.total_price).replace("$", ""))