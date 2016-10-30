"""
Created on Oct 28, 2016

@author: mvoitko
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from src.locators.mainLocators import MainLocators

class MainPage(BasePage):
    """
    Main page representation.
    Contains all actions related to UI interaction.
    """
    def search(self, querry):
        """
        Search given querry.
        """
        self.click_on('search button')
        self.fill('search field', querry).send_keys(Keys.ENTER)