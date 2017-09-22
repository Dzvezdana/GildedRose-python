Feature: Items that has special rules

  Scenario: Aged Brie increase in quality
    Given an item of type "Aged Brie" with quality 35 and sell by date in the future
    When 1 day passed
    Then the item has quality 36

