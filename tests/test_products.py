import pytest

from midterm_project.steps.products_steps import ProductsSteps


class TestProducts:

    @pytest.mark.parametrize('sort_name', ['asc', 'desc'])
    @pytest.mark.parametrize("sort_by", ["price", "name"])
    def test_sorting_by_price_asc(self, app, sort_by, sort_name):
        products_steps = ProductsSteps(app)
        products_steps.open_products_page()
        products_steps.open_sort_tab()
        products_steps.choose_sort(sort_name=sort_name, sort_by=sort_by)
        products_steps.check_sorted(sort_name=sort_name, sort_by=sort_by)