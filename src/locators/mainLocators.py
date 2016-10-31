"""
Created on Oct 30, 2016

@author: mvoitko
"""
from selenium.webdriver.common.by import By


class MainLocators:
    """
    A class for main page locators.
    Contains all main page locators.
    : type dict:
    """

    locators_dictionary = {
        "SEARCH_BUTTON": (By.ID, 'search-form-btn'),
        "SEARCH_FIELD": (By.ID, 'search-form-field'),
        "USER_NAME": (By.CSS_SELECTOR, 'dt>a'),
        "LOGIN_BUTTON": (By.ID, 'login'),
        "SIGN_UP": (By.CSS_SELECTOR,
                    '.btn.btn_x-large.btn_navbar_registration')
    }
