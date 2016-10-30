"""
Created on Oct 29, 2016

@author: mvoitko
"""
from src.pages.basePage import BasePage
from src.utils.helper import *


class LoginPage(BasePage):
    """
    Login page representation.
    Contains all actions related to UI interaction.
    """
    credentials = form_user_dict()
    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver,
            url='login')

    def login(self, email, password):
        """
        Login with given credentials.
        """
        self.fill('email field', email)
        self.fill('password field', credentials[email])
        self.click_on('login button')