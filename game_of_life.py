import random

DEFAULT_WIDTH = 40
DEFAULT_HEIGHT = 40

class Grid:
    def __init__(self, width: int = DEFAULT_WIDTH, height: int = DEFAULT_HEIGHT):
        """Initializes a grid with the given width and height."""
        self.width = width
        self.height = height
        # Initialize grid with False (dead cells)
        self.cells = [[False for _ in range(self.width)] for _ in range(self.height)]

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
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # Skip the cell itself
                if self.get_cell(x + dx, y + dy):
                    count += 1
        return count

    def place_random_cells(self, num_cells: int):
        """Randomly places a given number of alive cells on the grid."""
        if num_cells > self.width * self.height:
            raise ValueError("Number of cells exceeds grid capacity.")

        # Reset grid
        self.cells = [[False for _ in range(self.width)] for _ in range(self.height)]

        placed = 0
        while placed < num_cells:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if not self.cells[y][x]:
                self.cells[y][x] = True
                placed += 1


class Game:
    def __init__(self, grid: Grid):
        self.grid = grid

    def next_generation(self):
        """Advances the game to the next generation based on Conway's Game of Life rules."""
        # Create a new grid state to populate
        new_cells = [[False for _ in range(self.grid.width)] for _ in range(self.grid.height)]

        for y in range(self.grid.height):
            for x in range(self.grid.width):
                is_alive = self.grid.get_cell(x, y)
                alive_neighbors = self.grid.count_alive_neighbors(x, y)

                # Rule 1: Underpopulation - Any live cell with fewer than two live neighbours dies.
                # Rule 2: Survival - Any live cell with two or three live neighbours lives on.
                # Rule 3: Overpopulation - Any live cell with more than three live neighbours dies.
                if is_alive and (alive_neighbors == 2 or alive_neighbors == 3):
                    new_cells[y][x] = True

                # Rule 4: Reproduction - Any dead cell with exactly three live neighbours becomes a live cell.
                elif not is_alive and alive_neighbors == 3:
                    new_cells[y][x] = True

        # Update grid with the new state
        self.grid.cells = new_cells
