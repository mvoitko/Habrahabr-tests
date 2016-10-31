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
    Main Habrahabr page representation.
    Class for UI actions related to this page
    """

    url = 'interesting'
    locators_dictionary = MainLocators.locators_dictionary

    def search(self, querry):
        """
        Search given querry.
        :param querry: str - text to search
        :return: element: selenium.webdriver.remote.webelement.WebElement
        """
        self.click_on('search button')
        self.fill('search field', querry)
        self.find('search field').send_keys(Keys.ENTER)
        return MainPage(self.driver)