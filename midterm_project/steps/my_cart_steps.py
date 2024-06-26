import allure

from midterm_project.pages.product_page import ProductPage
from midterm_project.pages.products_page import ProductsPage
from midterm_project.steps.base_step import BaseStep
from midterm_project.pages.base_page import BasePage
from midterm_project.pages.my_cart_page import MyCartPage


class MyCartSteps(BaseStep):
    """ Steps for My Cart Page """

    @allure.step("Open empty my cart page")
    def open_my_cart_page(self):
        """ Step opening empty my cart page """
        self.click_element(BasePage.cart_badge, "Card badge icon")

    @allure.step("Check empty My cart")
    def check_empty_my_cart(self):
        """ Step checking empty My cart"""
        assert self.get_text(MyCartPage.my_cart_title) == "No Items", "The My Cart page didn't open"

    @allure.step("Open not empty My cart")
    def open_not_empty_my_cart_page(self):
        """ Step opening not empty My cart """
        self.click_element(ProductsPage.first_product, "First product")
        self.click_element(ProductPage.add_to_cart_button, "Add To Cart button")

        # self.driver.back()
        # self.click_element(ProductsPage.second_product)
        # self.click_element(ProductPage.add_to_cart_button)
        self.click_element(BasePage.cart_badge, "Card badge icon")

    @allure.step("Plus counter product")
    def plus_counter(self, count=1):
        """ Step plus counter product """
        for _ in range(count):
            self.elements_are_visible(ProductPage.counter_plus_btn)[0].click()
        assert self.elements_are_visible(ProductPage.counter_amount)[0].text == str(1+count), \
            "Counter amount was not added"

    @allure.step("Check update counter product")
    def check_update_count(self):
        """ Step checking update counter product """
        assert self.get_text(BasePage.cart_item_count) == self.get_text(MyCartPage.total_number).split(" ")[0], \
            "The count of the items has not been updated"

    @allure.step("Check total price")
    def check_total_price(self):
        """ Step checking total price """
        counts = self.elements_are_visible(MyCartPage.counter_amount)
        prices = self.elements_are_visible(MyCartPage.product_price)
        total_price = 0
        for i in range(len(counts)):
            total_price += int(counts[i].text) * float(prices[i].text.replace("$", ""))
        assert total_price == float(self.get_text(MyCartPage.total_price).replace("$", "")), \
            "Cart total price is not calculated correctly"










