"""
Created on Oct 27, 2016

@author: mvoitko
"""
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

from src import config


class BasePage:
    """
    Base page representation.
    Contains all actions related to UI interaction.
    All pages may be inherited from this class.
    """
    def __init__(self, driverm, base_url='http://www.habrahabr.ru/'):
        """
        :type driver: selenium.webdriver.*
        """
        self.base_url = base_url
        self.driver = driver
        self.timeout = 15
        # self.logger = logging.getLogger(self.__class__.__name__)

    def open(self, url):
        """
        Open given web page.
        :type element: selenium.webdriver.remote.webelement.WebElement
        """
        url = self.base_url + url
        self.driver.get(url)

    def _find_elem_by_key(self, key):
        """
        Find respective locator for the element in locators dictionary.
        :type tuple: (method, value)
        """
        key = key.replace(" ", "_")
        if key in self.locators_dictionary:
            element_locator = locators_dictionary[key]
        else:
            raise AttributeError("Cannot find {0} locator on the {1} page".format(key, str(self)))
        return element_locator

    def find(self, key):
        """
        Find element with specified locator.
        :type element: selenium.webdriver.remote.webelement.WebElement
        """
        locator = self.driver._find_elem_by_key(key)
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(*locator))

    def click_on(self, key):
        """
        Click on element with specified locator.
        :type element: selenium.webdriver.remote.webelement.WebElement
        """
        element = self.driver.find(key)
        element.click()

    def fill(self, key, value):
        """
        Fill element with specified value.
        :type element: selenium.webdriver.remote.webelement.WebElement
        """
        element = self.driver.find(key)
        element.clear()
        element.send_keys(value)

    def _highlight(self, element):
        """
        Highlight given web element with red border using JS execution.
        WARNING: Contains time.sleep in 1 sec between scrolling to element and highlighting
        :type element: selenium.webdriver.remote.webelement.WebElement
        """
        self.execute_script(element, 'scrollIntoView(true);')
        sleep(1)
        self.execute_script(element, 'setAttribute("style", "color: red; border: 5px solid red;");')
        sleep(1)
        self.execute_script(element, 'setAttribute("style", "");')