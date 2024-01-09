from selenium.webdriver.common.by import By

from midterm_project.steps.base_step import BaseStep
from midterm_project.pages.login_page import LoginPage
from midterm_project.pages.base_page import BasePage
from midterm_project.pages.products_page import ProductsPage


class LoginSteps(BaseStep):
    """ Steps for Login Page"""

    def open_login_page(self):
        """ Step opening login page"""
        self.open_menus()
        self.click_element(BasePage().menu_item_login)
        assert self.get_text(LoginPage.login_title) == "Login"

    def login(self, username, password):
        """ Step logining with username and password"""
        if self.is_element_present(LoginPage.login_title):
            self.fill(LoginPage.input_username, username)
            self.fill(LoginPage.input_password, password)
            self.click_element(LoginPage.login_button)

    def check_successful_login(self):
        """ Step checking if successful login"""
        assert self.get_text(ProductsPage.products_title) == 'Products'

    def check_locked_out(self):
        """ Step checking if locked user login"""
        assert self.get_text(LoginPage.generic_err_msg) == 'Sorry, this user has been locked out.'

    def check_no_exist(self):
        """ Step checking if user does not exist"""
        assert self.get_text(LoginPage.generic_err_msg) == 'Provided credentials do not match any user in this service.'

    def check_err_msg_filed(self, filed):
        """ Step checking if login without credentials filed"""
        if filed == 'password':
            assert self.get_text(LoginPage.password_err_msg) == 'Password is required'
        elif filed == 'username':
            assert self.get_text(LoginPage.username_err_msg) == 'Username is required'

