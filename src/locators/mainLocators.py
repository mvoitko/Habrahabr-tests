"""
Created on Oct 30, 2016

@author: mvoitko
"""
from selenium.webdriver.common.by import By


class MainLocators:
    """
    A class for main page locators.
    Contains all main page locators.
    :type dict:
    """

    locators_dictionary = {

        "SEARCH_BUTTON": (By.ID, 'search-form-btn'),

        "SEARCH_FIELD": (By.ID, 'search-form-field'),

        "SEARCHED_ITEM": (By.CLASS_NAME, 'searched-item'),

        "SEARCH_RESULTS": (By.CLASS_NAME, 'search_results'),

        "POST": (By.CLASS_NAME, 'post'),

        "SORT_BY_TIME": (By.CSS_SELECTOR, 'ul.sort_menu *:nth-child(3)'),

        "SORT_BY_RELEVANCE": (By.CSS_SELECTOR, 'ul.sort_menu *:nth-child(2)'),

        "SORT_BY_RATING": (By.CSS_SELECTOR, 'ul.sort_menu *:nth-child(4)"]'),

        "POST_TIMESTAMP": (By.CSS_SELECTOR, '.post__time_published'),

        "POST TITLE": (By.CSS_SELECTOR, '.post__title_link'),

        "EMPTY_STATE": (By.CLASS_NAME, 'search-results-title'),

        "USER_NAME": (By.CSS_SELECTOR, 'dt>a'),

        "LOGIN_BUTTON": (By.ID, 'login'),

        "SIGN_UP": (By.CSS_SELECTOR, '.btn.btn_x-large.btn_navbar_registration')

    }
