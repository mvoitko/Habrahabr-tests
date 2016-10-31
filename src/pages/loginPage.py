"""
Created on Oct 29, 2016

@author: mvoitko
"""
from selenium import webdriver

from src.pages.basePage import BasePage
from src.pages.mainPage import MainPage
from src.locators.loginLocators import LoginLocators as ll


class LoginPage(BasePage):
    """
    Login page representation.
    Contains all actions related to UI interaction.
    """

    def __init__(self, context):
        BasePage.__init__(self, context.driver, url='login',
                          locators_dictionary=ll.locators_dict)

    # def switch_to_iframe(self):
    #     frame = self.find('iframe')
    #     self.driver.switch_to_frame(frame)

    def check_capthca(self):
        try:
            self.driver.switch_to_frame('undefined')
            self.driver.find_element_by_id('checkbox_id').click()
            self.driver.switch_to_default_content()
        finally:
            pass

    def login(self, email, password):
        """
        Login with given credentials.
        :type webdriver
        """
        self.fill('email field', email)
        self.fill('password field', password)
        # self.check_capthca()
        self.click_on('login button')
        return MainPage(self.driver)
