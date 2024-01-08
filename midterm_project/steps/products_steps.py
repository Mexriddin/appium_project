from midterm_project.pages.product_page import ProductPage
from midterm_project.steps.base_step import BaseStep
from midterm_project.pages.base_page import BasePage
from midterm_project.pages.products_page import ProductsPage


class ProductsSteps(BaseStep):
    """ Steps for Products Page """

    def open_products_page(self):
        """ Step opening products page """
        self.open_menus()
        self.click_element(BasePage().menu_item_catalog)
        assert self.get_text(ProductsPage.products_title) == "Products"

    def open_sort_tab(self):
        """ Step opening sort tab"""
        self.click_element(ProductsPage.sort_button)
        assert self.get_text(ProductsPage.sort_title) == "Sort by:"

    def choose_sort(self, sort_name, sort_by):
        """ Step choosing sort"""
        if sort_by == 'price':
            if sort_name == "asc":
                self.click_element(ProductsPage.sort_by_price_asc)
            elif sort_name == "desc":
                self.click_element(ProductsPage.sort_by_price_desc)
        elif sort_by == 'name':
            if sort_name == "asc":
                self.click_element(ProductsPage.sort_by_name_asc)
            elif sort_name == "desc":
                self.click_element(ProductsPage.sort_by_name_desc)

    def check_sorted(self, sort_name, sort_by):
        """ Step checking sort """
        if sort_by == 'name':
            if sort_name == "asc":
                product_names = self.elements_are_visible(ProductsPage.product_names)
                name_list = [name.text for name in product_names]
                assert name_list == sorted(name_list)
            elif sort_name == "desc":
                product_names = self.elements_are_visible(ProductsPage.product_names)
                name_list = [name.text for name in product_names]
                assert name_list == sorted(name_list, reverse=True)
        elif sort_by == 'price':
            if sort_name == "asc":
                prices = self.elements_are_visible(ProductsPage.product_prices)
                prices_list = [float(price.text.replace("$", "")) for price in prices]
                assert prices_list == sorted(prices_list)
            elif sort_name == "desc":
                prices = self.elements_are_visible(ProductsPage.product_prices)
                prices_list = [float(price.text.replace("$", "")) for price in prices]
                assert prices_list == sorted(prices_list, reverse=True)

    def review_product(self):
        """ Step review the product"""
        self.click_element(ProductsPage.star_rating)

    def check_review(self):
        """ Step check the review """
        assert self.get_text(ProductsPage.review_title) == "Thank you for submitting your review!"
        self.click_element(ProductsPage.close_modal_btn)

