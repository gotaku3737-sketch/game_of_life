Feature: Game of Life Domain Rules

  Scenario Outline: Underpopulation
    Given a grid with a live cell at <x>, <y>
    And the cell has <neighbors> live neighbors
    When the next generation is calculated
    Then the cell at <x>, <y> should be dead

    Examples:
      | x | y | neighbors |
      | 5 | 5 | 0         |
      | 5 | 5 | 1         |

  Scenario Outline: Survival
    Given a grid with a live cell at <x>, <y>
    And the cell has <neighbors> live neighbors
    When the next generation is calculated
    Then the cell at <x>, <y> should be alive

    Examples:
      | x | y | neighbors |
      | 5 | 5 | 2         |
      | 5 | 5 | 3         |

  Scenario Outline: Overpopulation
    Given a grid with a live cell at <x>, <y>
    And the cell has <neighbors> live neighbors
    When the next generation is calculated
    Then the cell at <x>, <y> should be dead

    Examples:
      | x | y | neighbors |
      | 5 | 5 | 4         |
      | 5 | 5 | 5         |
      | 5 | 5 | 8         |

  Scenario Outline: Reproduction
    Given a grid with a dead cell at <x>, <y>
    And the cell has <neighbors> live neighbors
    When the next generation is calculated
    Then the cell at <x>, <y> should be alive

    Examples:
      | x | y | neighbors |
      | 5 | 5 | 3         |
