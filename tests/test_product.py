from midterm_project.steps.product_steps import ProductSteps


class TestProduct:

    def test_add_to_cart(self, app):
        product_steps = ProductSteps(app)
        product_steps.open_product_page()
        product_steps.choose_color("red")
        product_steps.plus_counter()
        product_steps.add_to_cart()