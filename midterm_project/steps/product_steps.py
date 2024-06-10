import allure

from midterm_project.pages.product_page import ProductPage
from midterm_project.steps.base_step import BaseStep
from midterm_project.pages.base_page import BasePage
from midterm_project.pages.products_page import ProductsPage


class ProductSteps(BaseStep):
    """ Steps for Product Page """

    @allure.step("Open product page")
    def open_product_page(self):
        """ Step opening product page """
        product_name = self.get_text(ProductsPage.first_product)
        self.click_element(ProductsPage.first_product)
        assert self.get_text(ProductPage.product_title) == product_name, "The Product page did not open"

    @allure.step("Choose product color")
    def choose_color(self, color_name):
        """ Step choosing color product """
        colors = self.elements_are_visible(ProductPage.color_checkboxes)
        for color in colors:
            if color_name in color.get_attribute("content-desc"):
                color.click()

    @allure.step("Plus product counter")
    def plus_counter(self, count=1):
        """ Step plus counter product """
        for _ in range(count):
            self.click_element(ProductPage.counter_plus_btn)
        assert self.get_text(ProductPage.counter_amount) == str(1+count), "Counter amount was not added"

    @allure.step("Click Add to cart")
    def add_to_cart(self):
        """ Step adding to cart"""
        self.click_element(ProductPage.add_to_cart_button)

    @allure.step("Check to see if item is added to cart")
    def check_added_to_cart(self):
        """ Step checking to see if item is added to cart"""
        assert int(self.get_text(BasePage.cart_item_count)) >= int(self.get_text(ProductPage.counter_amount)), \
            "Item was not added to cart"



