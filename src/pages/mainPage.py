"""
Created on Oct 28, 2016

@author: mvoitko
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from src.pages.basePage import BasePage
from src.locators.mainLocators import MainLocators


class MainPage(BasePage):
    """
    Main page representation.
    Contains all actions related to UI interaction.
    """

    def __init__(self, context):
        BasePage.__init__(self, context.driver, url='interesting', locators_dictionary=MainLocators.locators_dictionary)

    def search(self, querry):
        """
        Search given querry.
        """
        self.click_on('search button')
        self.fill('search field', querry).send_keys(Keys.ENTER)