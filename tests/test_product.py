import allure

from midterm_project.steps.product_steps import ProductSteps


@allure.epic("Product")
class TestProduct:

    @allure.title("The test of adding an item to the cart")
    @allure.description("Test adding an item to the shopping cart by selecting a property")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_to_cart(self, app):
        product_steps = ProductSteps(app)
        product_steps.open_product_page()
        product_steps.choose_color("red")
        product_steps.plus_counter(2)
        product_steps.add_to_cart()
        product_steps.check_added_to_cart()