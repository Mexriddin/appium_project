from midterm_project.steps.product_steps import ProductSteps
from midterm_project.steps.products_steps import ProductsSteps


class TestProduct:

    def test_add_to_cart(self, app):
        products_step = ProductsSteps(app)
        products_step.open_products_page()

        product_steps = ProductSteps(app)
        product_steps.open_product_page()
        product_steps.choose_color("red")
        product_steps.plus_counter(2)
        product_steps.add_to_cart()