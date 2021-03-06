@skip
Feature: Login
	"""
	DEPRACATED since need to handle Google captcha on web app environment config level
	"""
	As user
    I want to have possibilty to log in to my account

	Scenario Outline: Login with correct credentials
	    Given I have an account for "<email>"
	    When I log in
	    Then I should see personalized page

	    Examples:
		    | email                    |
		    | habrtest@mailinator.com  |
		    | habr_test@mailinator.com |
		    | 044244244@mailinator.com |