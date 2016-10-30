"""
Created on Oct 28, 2016

@author: mvoitko
"""
from behave import *
from hamcrest import *

from src.pages.loginPage import LoginPage
from src.utils.helper import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# use_step_matcher('re')

@given(u'I have an account for "{email}"')
def step_impl(context, email):
    assert_that(whether_in_file(email) is True)

@when(u'I log in')
def step_impl(context):
    page = LoginPage(context)
    page.login(email, )

# @when(u'I click "([^"]*)"')
# def step_impl(context, element):
#     page.click_on(element)

# @then(u'I get <page_name> page')
# def step_impl(context, page_name):
