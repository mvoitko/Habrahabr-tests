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

    def __init__(self, driver):
        """
        :type driver: selenium.webdriver.*
        """
        self.driver = driver
        self.timeout = 20
        self.logger = logging.getLogger(self.__class__.__name__)

    def open(cls):
        """
        Open page url.
        :type url: str - URL to open
        :return: element: selenium.webdriver.remote.webelement.WebElement
        """
        cls.driver.get(cls.url)

    def _find_locator_by_key(cls, key):
        """
        Find respective locator for the element in locators dictionary.
        :param key: str - web element key
        :return: tuple of (strategy, value)
        """
        key = key.upper().replace(" ", "_")
        if key in cls.locators_dictionary:
            try:
                element_locator = cls.locators_dictionary[key]
                return element_locator
            except:
                raise NoSuchElementException(
                    "Cannot find {0} locator on the {1} page".format(key, str(cls)))

    def find(cls, key):
        """
        Find element with specified locator.
        :param key: str - web element key
        :return: element: selenium.webdriver.remote.webelement.WebElement
        """
        locator = cls._find_locator_by_key(key)
        return WebDriverWait(cls.driver, cls.timeout).until(
            EC.presence_of_element_located(locator))

    def find_elems(cls, key):
        """
        Find element with specified locator.
        :param key: str - web element key
        :return: elements: list of selenium.webdriver.remote.webelement.WebElement
        """
        locator = cls._find_locator_by_key(key)
        return WebDriverWait(cls.driver, cls.timeout).until(
            EC.presence_of_all_elements_located(locator))

    def click_on(self, key):
        """
        Click on web element with specified key.
        :type key: str - web element key
        """
        element = self.find(key)
        element.click()

    def fill(self, key, value):
        """
        Fill value in web element with key
        :type key: str - web element key
        :type value: str - value to fill in
        """
        element = self.find(key)
        element.clear()
        element.send_keys(value)

    def get_text(self, key):
        """
        Get text of web element with specified key
        :param key: str - web element key
        :return text: str - element text
        """
        return self.find(key).text

    def get_page_title(self):
        """
        Get text of web element with specified key
        :return title: str - web page title
        """
        return self.driver.title