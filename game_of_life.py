import random

DEFAULT_WIDTH = 40
DEFAULT_HEIGHT = 40

class Grid:
    def __init__(self, width: int = DEFAULT_WIDTH, height: int = DEFAULT_HEIGHT):
        """Initializes a grid with the given width and height."""
        if width <= 0 or height <= 0:
            raise ValueError("Grid dimensions must be positive integers.")
        self.width = width
        self.height = height
        # Initialize grid with False (dead cells)
        self.cells = self._create_empty_grid()

    def _create_empty_grid(self):
        """Creates a new empty grid (all False)."""
        return [[False] * self.width for _ in range(self.height)]

    def set_cell(self, x: int, y: int, is_alive: bool):
        """Sets the state of a specific cell."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.cells[y][x] = is_alive
        else:
            raise ValueError(f"Coordinates ({x}, {y}) are out of bounds.")

    def get_cell(self, x: int, y: int) -> bool:
        """Gets the state of a specific cell. Returns False if out of bounds (hard edges)."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.cells[y][x]
        return False

    def count_alive_neighbors(self, x: int, y: int) -> int:
        """Counts the number of alive neighbors around a cell."""
        count = 0
        cells = self.cells

        y_start = y - 1 if y > 0 else 0
        y_end = y + 2 if y < self.height - 1 else self.height
        x_start = x - 1 if x > 0 else 0
        x_end = x + 2 if x < self.width - 1 else self.width

        for iy in range(y_start, y_end):
            row = cells[iy]
            for ix in range(x_start, x_end):
                if iy == y and ix == x:
                    continue
                if row[ix]:
                    count += 1
        return count

    def place_random_cells(self, num_cells: int):
        """Randomly places a given number of alive cells on the grid."""
        if num_cells > self.width * self.height:
            raise ValueError("Number of cells exceeds grid capacity.")

        # Reset grid
        self.cells = self._create_empty_grid()

        # Get a random sample of indices and map them to coordinates
        selected_indices = random.sample(range(self.width * self.height), num_cells)

        for index in selected_indices:
            y, x = divmod(index, self.width)
            self.cells[y][x] = True


class Game:
    def __init__(self, grid: Grid):
        self.grid = grid

    def next_generation(self):
        """Advances the game to the next generation based on Conway's Game of Life rules."""
        grid = self.grid
        width = grid.width
        height = grid.height
        cells = grid.cells

        # Create a new grid state to populate
        new_cells = grid._create_empty_grid()

        for y in range(height):
            for x in range(width):
                # Count neighbors using Grid method
                alive_neighbors = grid.count_alive_neighbors(x, y)
                is_alive = cells[y][x]

                # Rule 1-3: Survival
                if is_alive:
                    if 2 <= alive_neighbors <= 3:
                        new_cells[y][x] = True
                # Rule 4: Reproduction
                elif alive_neighbors == 3:
                    new_cells[y][x] = True

        # Update grid with the new state
        grid.cells = new_cells
