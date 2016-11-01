@wip
@smoke
Feature: Search
    As user
    I want to have possibilty to search through the posts

 Scenario: I would like to search for a topic
    Given I am on the home page
    When I search for "behave"
    Then I see first result in the list