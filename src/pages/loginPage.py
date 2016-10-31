"""
Created on Oct 29, 2016

@author: mvoitko
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from src.pages.basePage import BasePage
from src.pages.mainPage import MainPage
from src.locators.loginLocators import LoginLocators


class LoginPage(BasePage):
    """
    Login page representation.
    Contains all actions related to UI interaction.
    """

    def __init__(self, context):
        BasePage.__init__(self, context.driver, url='login',
                          locators_dictionary=LoginLocators.locators_dict)

    # def switch_to_iframe(self):
    #     frame = self.find('iframe')
    #     self.driver.switch_to_frame(frame)

    def check_capthca(self):
        try:
            self.driver.switch_to_frame('undefined')
            element = self.driver.find_element_by_id('recaptcha-anchor')
            action = ActionChains(self.driver).move_to_element(element)
            action.perform()
            self.driver.switch_to_default_content()
            self.driver.implicitly_wait(20)
        finally:
            print('Fail')

    def login(self, email, password):
        """
        Login with given credentials.
        :type webdriver:
        """
        self.fill('email field', email)
        self.fill('password field', password)
        self.check_capthca()
        self.click_on('login button')
        return MainPage(self.driver)
