import allure
from midterm_project.steps.logout_steps import LogoutSteps


@allure.epic("Logout")
class TestLogout:
    @allure.title("Logout test")
    @allure.description("Successful logout test")
    def test_logout(self, app):
        logout_steps = LogoutSteps(app)
        logout_steps.logout()
        logout_steps.check_logout()

