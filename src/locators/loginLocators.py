"""
Created on Oct 30, 2016

@author: mvoitko
"""
from selenium.webdriver.common.by import By


class LoginLocators:
    """
    A class for login page locators.
    Contains all login page locators.
    : type : dict
    """
    locators_dictionary: {
        "EMAIL_FIELD": (By.ID, 'email_field'),
        "PASSWORD_FIELD" : (By.NAME, 'password'),
        "LOGIN_BUTTON" = (By.NAME, 'go')
    }