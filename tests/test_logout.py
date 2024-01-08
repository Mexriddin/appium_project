from midterm_project.steps.logout_steps import LogoutSteps


class TestLogout:
    def test_logout(self, app):
        logout_steps = LogoutSteps(app)
        logout_steps.logout()
        logout_steps.check_logout()

