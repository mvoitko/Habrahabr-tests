"""
Created on Oct 28, 2016

@author: mvoitko
"""
import time
from behave import *
from hamcrest import *
from selenium import webdriver

from src.pages.loginPage import LoginPage
from src.pages.mainPage import MainPage
from src.utils import helper


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

@step(u'I am on the home page')
def step_impl(context):
    page = MainPage(context.driver)
    page.open()


@when(u'I search for "{querry}"')
def step_impl(context, querry):
    context.querry = querry
    page = MainPage(context.driver)
    page.search(context.querry)


@then(u'I see first result in the list')
def step_impl(context):
    page = MainPage(context.driver)
    searched_item = page.get_text('searched item')
    assert_that(len(page.get_search_results()), is_(greater_than_or_equal_to(1)))
    assert_that(context.querry.lower(), contains_string(searched_item.lower()))

@given(u'I see search results for "{querry}"')
def step_impl(context, querry):
    context.querry = querry
    page = MainPage(context.driver)
    page.open()
    page.search(context.querry)


@when(u'I apply sorting by "{sorting_param}"')
def step_impl(context, sorting_param):
    context.sorting_param = sorting_param
    page = MainPage(context.driver)
    page.sort_by(sorting_param)

@then(u'I see sorted search results')
def step_impl(context):
    page = MainPage(context.driver)
    posts_timestamps = page.get_posts_timestamps()
    assert_that(posts_timestamps, equal_to(sorted(posts_timestamps, reverse=True)))

@then(u'I see "{empty_state_text}" empty state message')
def step_impl(context, empty_state_text):
    page = MainPage(context.driver)
    message_text = page.get_text('empty state')
    print(message_text)
    assert_that(message_text, equal_to(empty_state_text))