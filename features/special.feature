Feature: Items that has special rules

  Scenario: Aged Brie increase in quality
    Given an item of type "Aged Brie" with quality 35 and sell by date in the future
    When 1 day passed
    Then the item has quality 36

  @wip # Is this cool, the Sulfuras should always be 80
  Scenario: Sulfuras increase in quality
    Given an item of type "Sulfuras, Hand of Ragnaros" with quality 35 and sell by date in the future
    When 1 day passed
    Then the item has quality 35

  @skip # This is a bug, as in not following spec
  Scenario: Sulfuras increase in quality
    Given an item of type "Sulfuras" with quality 13 and sell by date in the future
    When 1 day passed
    Then the item has quality 13

