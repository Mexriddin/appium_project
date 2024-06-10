import allure
import pytest
from midterm_project.steps.login_steps import LoginSteps
from midterm_project.utils.utils import (generate_no_exist_user_data,
                                         get_locked_out_user_data,
                                         generate_invalid_login_data,
                                         get_valid_login_data)


@allure.epic("Login")
class TestLogin:

    @allure.title("The blocked user's login test")
    @allure.description("A negative login test with the data of a blocked user")
    @pytest.mark.negative
    def test_login_locked_user(self, app):
        login_steps = LoginSteps(app)
        login_steps.open_login_page()
        locked_user = get_locked_out_user_data()
        login_steps.login(locked_user.username, locked_user.password)
        login_steps.check_locked_out()

    @allure.title("The no exist user's login test")
    @allure.description("A negative login test with the data of a non-existing user")
    @pytest.mark.negative
    def test_login_no_exist_user(self, app):
        login_steps = LoginSteps(app)
        login_steps.open_login_page()
        no_exist_user = generate_no_exist_user_data()
        login_steps.login(no_exist_user.username, no_exist_user.password)
        login_steps.check_no_exist()

    @allure.title("The user's login with empty {without_field} field test")
    @allure.description("Negative login test without filling in {without_field} field")
    @pytest.mark.negative
    @pytest.mark.parametrize('without_field',
                             ['both', 'username', 'password'],
                             ids=['without_both_filed', 'without username', 'without password'])
    def test_invalid_login(self, app, without_field):
        login_steps = LoginSteps(app)
        login_steps.open_login_page()
        invalid_login_data = generate_invalid_login_data(without_field)
        login_steps.login(invalid_login_data.username, invalid_login_data.password)
        login_steps.check_err_msg_filed(without_field)

    @allure.title("Successful login test")
    @allure.description("A positive login test with valid data for a successful login")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_login_active_user(self, app):
        login_steps = LoginSteps(app)
        login_steps.open_login_page()
        login_data = get_valid_login_data()
        login_steps.login(login_data.username, login_data.password)
        login_steps.check_successful_login()
