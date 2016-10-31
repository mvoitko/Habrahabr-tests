"""
Created on Oct 30, 2016

@author: mvoitko
"""
from selenium import webdriver
from behave.log_capture import capture

import logging


logging.basicConfig(filename="test.log", level=logging.DEBUG)
__logger__ = logging.getLogger("test")

#@capture
def before_all(context):
    __logger__.info("BEFORE ALL")
    __logger__.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()

#@capture
def after_all(context):
    __logger__.info("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    __logger__.info("AFTER FEATURE")
    # context.driver.quit()

# #@capture
# def before_feature(context, feature):
#     __logger__.info("BEFORE FEATURE")
#     __logger__.info(">>>>>>>>>>>>>>")

# #@capture
# def after_feature(context, feature):
#     __logger__.info("<<<<<<<<<<<<<")
#     __logger__.info("AFTER FEATURE")

# #@capture
# def before_scenario(context, scenario):
#     __logger__.info("BEFORE SCENARIO")
#     __logger__.info("==>>")

# #@capture
# def after_scenario(context, scenario):
#     __logger__.info("<<==")
#     __logger__.info("AFTER SCENARIO")

# #@capture
# def before_step(context, step):
#     __logger__.info("BEFORE STEP")

# #@capture
# def after_step(context, step):
#     __logger__.info("AFTER STEP")