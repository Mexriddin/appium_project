import allure

from midterm_project.steps.my_cart_steps import MyCartSteps


@allure.epic("My Cart")
class TestMyCart:

    @allure.title("Empty cart test")
    @allure.description("The cart test without added items")
    def test_empty_my_cart(self, app):
        my_cart_steps = MyCartSteps(app)
        my_cart_steps.open_my_cart_page()
        my_cart_steps.check_empty_my_cart()

    @allure.title("The test updates the number of items in the cart")
    @allure.description("Test increasing the quantity of items in the cart")
    def test_update_count_item_in_my_cart(self, app):
        my_cart_steps = MyCartSteps(app)
        my_cart_steps.open_not_empty_my_cart_page()
        my_cart_steps.plus_counter()
        my_cart_steps.check_update_count()
        my_cart_steps.check_total_price()