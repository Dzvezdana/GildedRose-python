Feature: General business rules

  Scenario: Item degrades by one per day
    Given an item with quality 10 and sell by date tomorrow
    When 1 day passed
    Then the item has quality 9
    And the item has sell by date today

  Scenario: Item where sell by date has passed
    Given an item with quality 10 and sell by date yesterday
    When 1 day passed
    Then the item has quality 8

  Scenario: Item quality is never negative
    Given an item with quality 0 and sell by date yesterday
    When 1 day passed
    Then the item has quality 0

  Scenario: Item can never have a quality higher than 50
    Given an item with quality 51 and sell by date tomorrow
    When 1 day passed
    Then the item has quality 50