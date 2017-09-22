Feature: Backstage pass

  Scenario Outline: Backstage passes quality curve
    Given a backstage pass and quality <quality> and sell by date in <days left> days
    When 1 day passed
    Then the item has quality <new quality>

    Examples: happy case
      | quality | days left | new quality |
      | 14      | 11        | 15          |
      | 14      | 10        | 16          |
      | 14      | 5         | 17          |
      | 14      | 0         | 0           |
