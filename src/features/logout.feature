@skip
Feature: Logout
    As user
    I want to have possibilty to log out of my account

    Scenario Outline: Logout
        Given I am an authenticated user
        When I enter "<username>" and "<password>"
        And I click login button
        Then I get interesting page