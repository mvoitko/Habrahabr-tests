"""
Created on Oct 28, 2016

@author: mvoitko
"""
from behave import *
from hamcrest import *

from src.pages.loginPage import LoginPage
from src.utils.helper import *


# use_step_matcher('re')

@given(u'I have an account for "{email}"')
def step_impl(context, email):
    context.email = email
    assert_that(whether_in_file(email) is True)


@when(u'I log in')
def step_impl(context):
    page = LoginPage(context)
    page.open()
    page.login(context.email, credentials[context.email])


@then(u'I should see personalized page')
def step_impl(context):
    page = MainPage(context)
    username = page.get_text('username')
    assert_that(username, contains_string(usernames[context.email]))
