@smoke
Feature: Search
    As user
    I want to have possibilty to search through the posts, sort search results by timing or rating

    Scenario: I would like to search for a topic
        Given I am on the home page
        When I search for "behave"
        Then I see first result in the list

    Scenario: I would like to sort search results by timing
        Given I see search results for "behave"
        When I apply sorting by "time"
        Then I see sorted search results
    @wip
    Scenario: I would like to see respective message when no results found
        Given I am on the home page
        When I search for "blahblahblahblahblahblah"
        Then I see "Сожалеем, поиск в топиках не дал результатов" empty state message
