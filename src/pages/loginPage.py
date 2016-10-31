"""
Created on Oct 29, 2016

@author: mvoitko
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from src.pages.basePage import BasePage
from src.pages.mainPage import MainPage
from src.locators.loginLocators import LoginLocators


class LoginPage(BasePage):
    """
    Login Habrahabr page representation.
    Class for UI actions related to this page
    """

    locators_dictionary = LoginLocators.locators_dictionary

    # def switch_to_iframe(self):
    #     frame = self.find('iframe')
    #     self.driver.switch_to_frame(frame)

    def check_capthca(self):
        """
        Handle Google Captcha
        """
        try:
            self.driver.switch_to_frame('undefined')
            element = WebdriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located((By.ID, 'recaptcha-anchor')))
            action = ActionChains(self.driver).move_to_element(element)
            action.perform()
            self.driver.switch_to_default_content()
            self.driver.implicitly_wait(20)
        finally:
            print('Fail')

    def login(self, email, password):
        """
        Login with given credentials.
        :param email: str - user email
        :param password: str - user password
        :return: element: selenium.webdriver.remote.webelement.WebElement
        """
        self.fill('email field', email)
        self.fill('password field', password)
        self.check_capthca()
        self.click_on('login button')
        return MainPage(self.context.driver)
