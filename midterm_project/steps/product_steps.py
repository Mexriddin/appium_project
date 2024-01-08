from midterm_project.pages.product_page import ProductPage
from midterm_project.steps.base_step import BaseStep
from midterm_project.pages.base_page import BasePage
from midterm_project.pages.products_page import ProductsPage


class ProductSteps(BaseStep):
    """ Steps for Product Page """

    def open_product_page(self):
        """ Step opening product page """
        self.open_menus()
        self.click_element(BasePage().menu_item_catalog)
        product_name = self.get_text(ProductsPage.first_product)
        self.click_element(ProductsPage.first_product)
        assert self.get_text(ProductPage.product_title) == product_name

    def choose_color(self, color_name):
        """ Step choosing color product """
        colors = self.elements_are_visible(ProductPage.color_checkboxes)
        for color in colors:
            if color_name in color.get_attribute("content-desc"):
                color.click()

    def plus_counter(self):
        """ Step plus counter product """
        self.click_element(ProductPage.counter_plus_btn)
        print(self.get_text(ProductPage.counter_amount))
        assert self.get_text(ProductPage.counter_amount) == '2'

    def add_to_cart(self):
        """ Step adding to cart"""
        self.click_element(ProductPage.add_to_cart_button)
        assert self.get_text(BasePage.cart_item_count) == '2'








