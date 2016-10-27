"""
Created on Oct 27, 2016

@author: mvoitko
"""

import logging


class BasePage:
    """
    Base page representation.
    Contains all actions related to UI interaction.
    All pages may be inherited from this class.
    """
    def __init__(self, driver):
        """
        :type browser: selenium.webdriver.*
        """
        self.driver = driver
        self.logger = logging.getLogger(self.__class__.__name__)
        self.timeout = 15

    def _highlight(self, element):
        """
        Highlight given web element with red border using JS execution.
        WARNING: Contains time.sleep in 1 sec between scrolling to element and highlighting
        :type element: selenium.webdriver.remote.webelement.WebElement
        """
        self.execute_script(element, 'scrollIntoView(true);')
        sleep(1)
        self.execute_script(element, 'setAttribute("style", "color: red; border: 5px solid red;");')
        sleep(1)
        self.execute_script(element, 'setAttribute("style", "");')