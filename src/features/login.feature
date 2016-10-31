@wip
@smoke
Feature: Login
	As user
	I want to have possibilty to access to my account with valid credentials

	Scenario Outline: Login with correct credentials
	    Given I have an account for "<email>"
	    When I log in
	    Then I should see personalized page

	    Examples:
		    | email                    |
		    | max.voitko@gmail.com     |
		    # | habrtest@mailinator.com  |
		    # | habr_test@mailinator.com |
		    # | 044244244@mailinator.com |