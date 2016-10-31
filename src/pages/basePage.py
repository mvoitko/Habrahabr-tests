"""
Created on Oct 27, 2016

@author: mvoitko
"""
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

from src.config import *


class BasePage:
    """
    Base page representation.
    Contains all actions related to UI interaction.
    All pages may be inherited from this class.
    """

    def __init__(self, driver, url=base_url, locators_dictionary=None):
        """
        :type driver: selenium.webdriver.*
        """
        self.url = base_url + url
        self.driver = driver
        self.timeout = 15
        self.locators_dictionary = locators_dictionary

    def open(self):
        """
        Open page url.
        :type element: selenium.webdriver.remote.webelement.WebElement
        """
        self.driver.get('http://habrahabr.ru/login')

    def _find_elem_by_key(self, key):
        """
        Find respective locator for the element in locators dictionary.
        :type tuple: (strategy, value)
        """
        key = key.upper().replace(" ", "_")
        if key in self.locators_dictionary:
            element_locator = self.locators_dictionary[key]
            return element_locator
        else:
            raise AttributeError(
                "Cannot find {0} locator on the {1} page".format(key, str(self)))

    def find(self, key):
        """
        Find element with specified locator.
        :type element: selenium.webdriver.remote.webelement.WebElement
        """
        locator = self._find_elem_by_key(key)
        print(locator)
        WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on(self, key):
        """
        Click on element with specified locator.
        """
        element = self.find(key)
        element.click()

    def fill(self, key, value):
        """
        Fill element with specified value.
        """
        element = self.find(key)
        element.clear()
        element.send_keys(value)

    def get_text(self, key):
        """
        Get element text.
        :type str:
        """
        element = self.find(key)
        return element.text

    def get_page_title(self):
        """
        Get page title.
        :type str:
        """
        return self.driver.title

    def get_current_url(self):
        """
        Get page title.
        :type str:
        """
        return self.driver.current_url

    def _highlight(self, element):
        """
        Highlight given web element with red border using JS execution.
        WARNING: Contains time.sleep in 1 sec between scrolling to element and highlighting
        :type element: selenium.webdriver.remote.webelement.WebElement
        """
        self.execute_script(element, 'scrollIntoView(true);')
        sleep(1)
        self.execute_script(
            element, 'setAttribute("style", "color: red; border: 5px solid red;");')
        sleep(1)
        self.execute_script(element, 'setAttribute("style", "");')
