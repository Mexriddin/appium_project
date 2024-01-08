from midterm_project.steps.my_cart_steps import MyCartSteps


class TestMyCart:
    def test_empty_my_cart(self, app):
        my_cart_steps = MyCartSteps(app)
        my_cart_steps.open_empty_my_cart_page()
        my_cart_steps.check_empty_my_cart()

    def test_not_empty_my_cart(self, app):
        my_cart_steps = MyCartSteps(app)
        my_cart_steps.open_not_empty_my_cart_page()
        my_cart_steps.plus_counter()
        my_cart_steps.check_update_count()
        my_cart_steps.check_total_price()