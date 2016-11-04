"""
Created on Oct 28, 2016

@author: mvoitko
"""

import re
import time
import locale
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src import config
from src.utils import helper
from src.pages.basePage import BasePage
from src.locators.mainLocators import MainLocators


class MainPage(BasePage):
    """
    Main Habrahabr page representation.
    Class for UI actions related to this page
    """

    url = config.base_url + 'interesting'
    locators_dictionary = MainLocators.locators_dictionary

    def search(self, querry):
        """
        Search given querry.
        :param querry: str - text to search
        :return: MainPage: selenium.webdriver.*
        """
        self.click_on('search button')
        self.fill('search field', querry)
        self.find('search field').send_keys(Keys.ENTER)
        return MainPage(self.driver)

    def get_search_results(self):
        """
        Get search results.
        :param querry: str - text to search
        :return: results: list of selenium.webdriver.remote.webelement.WebElement
        """
        return self.find_elems('post')

    def sort_by(self, sorting_param):
        """
        Sort search results page by given sorting parameter.
        :param sorting_param: str - sort by parameter
        :return: MainPage: selenium.webdriver.*
        """
        # old_post = self.driver.find_element(*MainLocators.locators_dictionary['POST TITLE'])
        sorting_param = "sort by " + sorting_param
        self.click_on(sorting_param)
        # WebDriverWait(self.driver, self.timeout).until(EC.staleness_of(old_post))
        return MainPage(self.driver)

    def get_posts_timestamps(self):
        """
        Get posts timestamps.
        :return: timestamps: list of datetime objects of posts.
        """
        time.sleep(1)
        timestamps = []
        timestamp_elements = self.find_elems('post timestamp')
        for timestamp in timestamp_elements:
            if re.match(helper.pattern_today, timestamp.text, re.IGNORECASE):
                date_object = helper.parse_today(timestamp.text)
            elif re.match(helper.pattern_yesterday, timestamp.text, re.IGNORECASE):
                date_object = helper.parse_yesterday(timestamp.text)
            elif re.match(helper.pattern_current_year, timestamp.text, re.IGNORECASE):
                date_object = helper.parse_current_year(timestamp.text)
            elif re.match(helper.pattern_full, timestamp.text):
                date_object = helper.parse_full(timestamp.text)
            else:
                raise NoSuchElementException(
                    "Cannot find POST TIMESTAMP locator on the {1} page".format(str(cls)))
            timestamps.append(date_object)
        return timestamps