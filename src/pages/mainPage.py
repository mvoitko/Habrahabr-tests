"""
Created on Oct 28, 2016

@author: mvoitko
"""
import locale
import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
        :return: driver: selenium.webdriver.*
        """
        self.click_on('search button')
        self.fill('search field', querry)
        self.find('search field').send_keys(Keys.ENTER)
        return MainPage(self.driver)

    def get_search_results(self):
        """
        Get search results.
        :param querry: str - text to search
        :return: results: list of elenium.webdriver.remote.webelement.WebElement
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
        Sort search results page.
        :type sorting_param: str - sort by parameter
        """
        sorting_param_list = {
            "relevance": "SORT_BY_RELEVANCE",
            "time": "SORT_BY_TIME",
            "rating": "SORT_BY_RATING"
        }
        self.click_on(sorting_param_list[sorting_param])
        return MainPage(self.driver)

    def get_posts_timestamps(self):
        """
        Get posts timestamps.
        """
        timestamps = []
        for timestamp in self.find_elems('post timestamp'):
            if re.match(pattern_today, timestamp.text):
                date_object = helper.parse_today(timestamp.text)
            elif re.match(pattern_yesterday, timestamp.text):
                date_object = helper.parse_yesterday(timestamp.text)
            date_object = helper.parse_date(timestamp.text)
            timestamps.append(date_object)
        return timestamps