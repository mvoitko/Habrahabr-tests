@skip
Feature: Logout
    """
    DEPRACATED since need to handle Google captcha on web app environment config level
    """
    As user
    I want to have possibilty to log out of my account

    Scenario Outline: Logout
        Given I am an authenticated user
        When I enter "<username>" and "<password>"
        And I click logout button
        Then I get on main page