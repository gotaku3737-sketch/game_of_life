import pytest
from main import render_grid
from game_of_life import Grid

def test_render_grid_1x1_dead(capsys):
    grid = Grid(1, 1)
    grid.set_cell(0, 0, False)
    render_grid(grid)
    captured = capsys.readouterr()
    assert captured.out == ". \n\n"

def test_render_grid_1x1_alive(capsys):
    grid = Grid(1, 1)
    grid.set_cell(0, 0, True)
    render_grid(grid)
    captured = capsys.readouterr()
    assert captured.out == "O \n\n"

def test_render_grid_2x2_mixed(capsys):
    grid = Grid(2, 2)
    grid.set_cell(0, 0, True)
    grid.set_cell(1, 0, False)
    grid.set_cell(0, 1, False)
    grid.set_cell(1, 1, True)
    render_grid(grid)
    captured = capsys.readouterr()
    # Expected:
    # O .
    # . O
    #
    assert captured.out == "O . \n. O \n\n"
