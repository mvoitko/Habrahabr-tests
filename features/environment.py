from selenium import webdriver
from behave.log_capture import capture

import logging


logging.basicConfig(filename="test.log", level=logging.DEBUG)
__logger__ = logging.getLogger("test")

def before_all(context):
    __logger__.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    __logger__.info("BEFORE ALL")
    context.driver = webdriver.Chrome()

def after_all(context):
    __logger__.info("AFTER FEATURE")
    __logger__.info("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    context.driver.quit()

@capture
def before_feature(context, feature):
    __logger__.info(">>>>>>>>>>>>>>>>")
    __logger__.info("BEFORE FEATURE")


@capture
def after_feature(context, feature):
    __logger__.info("AFTER FEATURE")
    __logger__.info("<<<<<<<<<<<<<<<<")


def before_scenario(context, scenario):
    __logger__.info("==>>")
    __logger__.info("BEFORE SCENARIO")
    context.dict = dict()


def after_scenario(context, scenario):
    __logger__.info("AFTER SCENARIO")
    __logger__.info("<<==")


def before_step(context, step):
    __logger__.info("BEFORE STEP")


def after_step(context, step):
    __logger__.info("AFTER STEP")