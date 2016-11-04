"""
Created on Oct 30, 2016

@author: mvoitko
"""
from selenium import webdriver
from behave.log_capture import capture

import logging

from src.utils import helper


logging.basicConfig(filename="test.log", level=logging.DEBUG)
__logger__ = logging.getLogger("test")


#@capture
def before_all(context):
    __logger__.info("BEFORE ALL")
    __logger__.info(">" * 20)
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    context.file_content = helper.read_file()
    context.credentials = helper.form_dict_from_file(context.file_content)
    context.usernames = helper.form_dict_from_file(context.file_content, 0, 2)

#@capture
def after_all(context):
    __logger__.info("<" * 20)
    __logger__.info("AFTER FEATURE")
    context.driver.close()
    print("Failed: {}".format(context.failed))

# #@capture
# def before_feature(context, feature):
#     __logger__.info("BEFORE FEATURE")
#     __logger__.info(">"*10)

# #@capture
# def after_feature(context, feature):
#     __logger__.info("<"*10)
#     __logger__.info("AFTER FEATURE")

# #@capture
# def before_scenario(context, scenario):
#     __logger__.info("BEFORE SCENARIO")
#     __logger__.info("="*2+">"*2)

# #@capture
# def after_scenario(context, scenario):
#     __logger__.info("<"*2+"="*2)
#     __logger__.info("AFTER SCENARIO")

# #@capture
# def before_step(context, step):
#     __logger__.info("BEFORE STEP")

# #@capture
# def after_step(context, step):
#     __logger__.info("AFTER STEP")
