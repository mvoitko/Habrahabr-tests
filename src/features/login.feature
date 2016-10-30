@wip
@smoke
Feature: Login
	As user
	I want to have possibilty to access to my account with valid email and password

	Scenario Outline: Login with correct credentials
	    Given I have an account for "<email>"
	    # When I fill in "email" with <email>
	    # And I fill in "password" with <password>
	    # And I click login button
	    When I log in
	    Then I should see personalized page

	    Examples:
		    | email                    |
		    | habrtest@mailinator.com  |
		    # | habr_test@mailinator.com |
		    # | 044244244@mailinator.com |