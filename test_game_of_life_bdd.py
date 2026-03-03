from pytest_bdd import scenarios, given, when, then, parsers
from game_of_life import Grid, Game

scenarios('game_of_life.feature')

@given(parsers.parse('a grid with a live cell at {x:d}, {y:d}'), target_fixture='context')
def grid_with_live_cell(x, y):
    grid = Grid(10, 10)
    grid.set_cell(x, y, True)
    return {'grid': grid, 'x': x, 'y': y, 'game': Game(grid)}

@given(parsers.parse('a grid with a dead cell at {x:d}, {y:d}'), target_fixture='context')
def grid_with_dead_cell(x, y):
    grid = Grid(10, 10)
    grid.set_cell(x, y, False)
    return {'grid': grid, 'x': x, 'y': y, 'game': Game(grid)}

@given(parsers.parse('the cell has {neighbors:d} live neighbors'))
def set_live_neighbors(context, neighbors):
    x, y = context['x'], context['y']
    grid = context['grid']

    # Offsets for neighbors
    neighbor_offsets = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0),           (1, 0),
        (-1, 1),  (0, 1),  (1, 1)
    ]

    # Set the required number of neighbors to alive
    for i in range(neighbors):
        dx, dy = neighbor_offsets[i]
        grid.set_cell(x + dx, y + dy, True)

@when('the next generation is calculated')
def calculate_next_generation(context):
    game = context['game']
    game.next_generation()

@then(parsers.parse('the cell at {x:d}, {y:d} should be dead'))
def cell_should_be_dead(context, x, y):
    assert not context['grid'].get_cell(x, y)

@then(parsers.parse('the cell at {x:d}, {y:d} should be alive'))
def cell_should_be_alive(context, x, y):
    assert context['grid'].get_cell(x, y)
