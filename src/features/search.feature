@smoke
Feature: Search
    As user
    I want to have possibilty to search through the posts, sort search results by timing or rating

    Scenario: I would like to search for a topic
        Given I am on the home page
        When I search for "behave"
        Then I see first result in the list
    @wip
    Scenario: I would like to sort search results by timing
        Given I see search results for "behave"
        When I apply sorting by "time"
        Then I see sorted search results

    Scenario: I would like to see respective message when no results found
        Given I am on the home page
        When I search for "behave"
        Then I see first result in the list
