import pytest
from game_of_life import Grid, Game

def test_grid_initialization():
    grid = Grid(10, 10)
    assert grid.width == 10
    assert grid.height == 10
    assert not grid.get_cell(0, 0)
    assert not grid.get_cell(9, 9)

def test_grid_boundaries():
    grid = Grid(10, 10)
    # Testing out-of-bounds get_cell
    assert not grid.get_cell(-1, 0)
    assert not grid.get_cell(10, 0)
    assert not grid.get_cell(0, -1)
    assert not grid.get_cell(0, 10)

def test_set_and_get_cell():
    grid = Grid(10, 10)
    grid.set_cell(5, 5, True)
    assert grid.get_cell(5, 5)
    assert not grid.get_cell(5, 6)

def test_count_alive_neighbors():
    grid = Grid(10, 10)
    grid.set_cell(5, 5, True) # center
    grid.set_cell(4, 5, True) # left
    grid.set_cell(6, 5, True) # right
    grid.set_cell(5, 4, True) # top

    assert grid.count_alive_neighbors(5, 5) == 3
    assert grid.count_alive_neighbors(4, 5) == 2
    # Neighbors of (4, 4) are (4, 5) left, (5, 4) top, (5, 5) center
    assert grid.count_alive_neighbors(4, 4) == 3

def test_underpopulation():
    # Any live cell with fewer than two live neighbours dies
    grid = Grid(10, 10)
    grid.set_cell(5, 5, True)
    game = Game(grid)
    game.next_generation()
    assert not grid.get_cell(5, 5)

def test_survival():
    # Any live cell with two or three live neighbours lives on
    grid = Grid(10, 10)
    grid.set_cell(5, 5, True)
    grid.set_cell(4, 5, True)
    grid.set_cell(6, 5, True)
    game = Game(grid)
    game.next_generation()
    assert grid.get_cell(5, 5)  # 2 neighbors

    grid.set_cell(5, 4, True)
    game.next_generation()
    assert grid.get_cell(5, 5)  # 3 neighbors

def test_overpopulation():
    # Any live cell with more than three live neighbours dies
    grid = Grid(10, 10)
    grid.set_cell(5, 5, True)
    grid.set_cell(4, 5, True)
    grid.set_cell(6, 5, True)
    grid.set_cell(5, 4, True)
    grid.set_cell(5, 6, True)
    game = Game(grid)
    game.next_generation()
    assert not grid.get_cell(5, 5)

def test_reproduction():
    # Any dead cell with exactly three live neighbours becomes a live cell
    grid = Grid(10, 10)
    grid.set_cell(4, 5, True)
    grid.set_cell(6, 5, True)
    grid.set_cell(5, 4, True)
    # (5, 5) is False
    game = Game(grid)
    game.next_generation()
    assert grid.get_cell(5, 5)

def test_place_random_cells():
    width, height = 5, 5
    grid = Grid(width, height)

    # 1. Exactly num_cells are placed
    num_cells = 10
    grid.place_random_cells(num_cells)
    count = sum(cell for row in grid.cells for cell in row)
    assert count == num_cells

    # 2. Handles 0 cells
    grid.place_random_cells(0)
    count = sum(cell for row in grid.cells for cell in row)
    assert count == 0

    # 3. Handles full capacity
    max_cells = width * height
    grid.place_random_cells(max_cells)
    count = sum(cell for row in grid.cells for cell in row)
    assert count == max_cells

    # 4. Raises ValueError for over-capacity
    with pytest.raises(ValueError):
        grid.place_random_cells(max_cells + 1)

    # 5. Ensures the grid is reset before placement
    grid.set_cell(0, 0, True)
    grid.set_cell(0, 1, True)
    grid.place_random_cells(1)
    # After placing 1 random cell, there should be exactly 1 cell alive,
    # not 1 + whatever was there before.
    count = sum(cell for row in grid.cells for cell in row)
    assert count == 1
