"""
Created on Oct 28, 2016

@author: mvoitko
"""
import locale
import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

from src import config
from src.pages.basePage import BasePage
from src.locators.mainLocators import MainLocators
from src.utils import helper


# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

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
        results = self.find_elems('posts')
        results_texts = []
        if len(results) >= 1:
            for element in results:
                results_texts.append(element.text)
        print(results_texts)
        return results_texts

    def sort_by(self, sorting_param):
        """
        Sort search results page by given sorting parameter.
        :param sorting_param: str - sort by parameter
        :return: MainPage: selenium.webdriver.*
        """
        sorting_param = "sort by " + sorting_param
        self.click_on(sorting_param)
        return MainPage(self.driver)

    def get_posts_timestamps(self):
        """
        Get posts timestamps.
        :return: timestamps: list of datetime objects of posts.
        """

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
                    "Cannot find {0} locator on the {1} page".format(key, str(cls)))
            timestamps.append(date_object)
        print(timestamps)
        return timestamps