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
        "POSTS": (By.CLASS_NAME, 'post'),
        "SORT_BY_TIME": (By.CSS_SELECTOR, 'a[href*="behave&order_by=date"]'),
        "SORT_BY_RELEVANCE": (By.CSS_SELECTOR, 'a[href*="behave&order_by=relevance"]'),
        "SORT_BY_RATING": (By.CSS_SELECTOR, 'a[href*="behave&order_by=rating"]'),
        "POST_TIMESTAMP": (By.CLASS_NAME, 'post__time_published'),
        "USER_NAME": (By.CSS_SELECTOR, 'dt>a'),
        "LOGIN_BUTTON": (By.ID, 'login'),
        "SIGN_UP": (By.CSS_SELECTOR, '.btn.btn_x-large.btn_navbar_registration')
    }
