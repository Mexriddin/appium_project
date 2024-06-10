import allure
import pytest
from midterm_project.steps.products_steps import ProductsSteps


@allure.epic("Products")
class TestProducts:

    @allure.title("The products sorting test")
    @allure.description("A test for sorting products by {sort_by} and {sort_name}")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize('sort_name', ['asc', 'desc'])
    @pytest.mark.parametrize("sort_by", ["price", "name"])
    def test_sorting(self, app, sort_by, sort_name):
        products_steps = ProductsSteps(app)
        products_steps.open_products_page()
        products_steps.open_sort_tab()
        products_steps.choose_sort(sort_name=sort_name, sort_by=sort_by)
        products_steps.check_sorted(sort_name=sort_name, sort_by=sort_by)

    @allure.title("The product review test")
    @allure.description("The test evaluates the product stars")
    def test_review_product(self, app):
        products_steps = ProductsSteps(app)
        products_steps.open_products_page()
        products_steps.review_product()
        products_steps.check_review()