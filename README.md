# Python Conway's Game of Life

Welcome to this Python implementation of Conway's Game of Life! This project simulates the classic cellular automaton devised by the British mathematician John Horton Conway in 1970.

The implementation is built using Object-Oriented Programming (OOP) best practices and features a fixed 40x40 grid with hard edges. It prompts the user for the number of simulation iterations and the number of initial live cells to randomly place on the grid, then animates the generations directly in your terminal.

## Python Stack

- **Python 3.10+**: The core language used for the simulation logic and terminal UI.
- **pytest**: The primary framework used for standard unit testing.
- **pytest-bdd**: An extension for `pytest` that implements Behavior-Driven Development (BDD), enabling domain-driven testing using plain-English Gherkin syntax.

## Prerequisites

Before running the application, ensure you have Python installed. You will also need to install the project dependencies.

It is highly recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required testing libraries:

```bash
pip install pytest pytest-bdd
```

## How to Run the Game

To start the terminal simulation, simply run the `main.py` script:

```bash
python main.py
```

The game will prompt you to:
1. **Enter the number of iterations:** How many generations you want to simulate (e.g., `50`).
2. **Enter the number of starting cells:** How many live cells to randomly spawn on the 40x40 grid (e.g., `300`).

The screen will clear and animate the simulation frame by frame.

## How to Run the Tests

This project includes both traditional unit tests and BDD tests to strictly verify the four domain rules of the Game of Life (Underpopulation, Survival, Overpopulation, Reproduction).

To execute all tests, run:

```bash
pytest
```

If you wish to run only the standard unit tests:

```bash
pytest test_game_of_life.py
```

If you wish to run only the Domain-Driven (BDD) tests:

```bash
pytest test_game_of_life_bdd.py
```