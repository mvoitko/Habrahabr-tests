"""
Created on Oct 28, 2016

@author: mvoitko
"""
from behave import *
from hamcrest import *

from src.pages.loginPage import LoginPage
from src.pages.mainPage import MainPage
from src.utils.helper import *


# use_step_matcher('re')

@given(u'I have an account for "{email}"')
def step_impl(context, email):
    assert_that(whether_in_file(email, context.file_content) is True)
    context.email = email


@when(u'I log in')
def step_impl(context):
    page = LoginPage(context.driver)
    page.open()
    page.login(context.email, context.credentials[context.email])


@then(u'I should see personalized page')
def step_impl(context):
    page = MainPage(context.driver)
    username = page.get_text('username')
    assert_that(username, contains_string(context.usernames[context.email]))

@given(u'I am on the home page')
def step_impl(context):
    page = MainPage(context.driver)
    page.open()


@when(u'I search for "{querry}"')
def step_impl(context, querry):
    context.querry = querry
    page = MainPage(context.driver)
    page.search(context.querry)


@then(u'I should be on the results page')
def step_impl(context):
    page = MainPage(context.driver)
    current_url = page.get_current_url()
    page_title = page.get_page_title()
    assert_that(page_title, contains_string(context.querry))

# @then(u'the first search result should be visible')
# def step_impl(context):
