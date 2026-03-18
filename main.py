import time
import os
import subprocess
from game_of_life import Grid, Game, DEFAULT_WIDTH, DEFAULT_HEIGHT

def clear_screen():
    if os.name == 'nt':
        subprocess.run(['cmd', '/c', 'cls'])
    else:
        subprocess.run(['clear'])

def render_grid(grid: Grid):
    for y in range(grid.height):
        row = ""
        for x in range(grid.width):
            row += "O " if grid.get_cell(x, y) else ". "
        print(row)
    print()

def main():
    print("Welcome to Conway's Game of Life!")
    print("-" * 35)

    # Prompt the user
    try:
        iterations = int(input("Enter the number of iterations: "))
        if iterations <= 0:
            print("Number of iterations must be positive.")
            return

        starting_cells = int(input("Enter the number of starting cells: "))
        max_cells = DEFAULT_WIDTH * DEFAULT_HEIGHT
        if starting_cells <= 0 or starting_cells > max_cells:
            print(f"Number of starting cells must be positive and less than or equal to {max_cells} ({DEFAULT_WIDTH}x{DEFAULT_HEIGHT}).")
            return

    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # Initialize the grid
    grid = Grid(DEFAULT_WIDTH, DEFAULT_HEIGHT)
    grid.place_random_cells(starting_cells)

    # Initialize game
    game = Game(grid)

    print("\nStarting simulation in 2 seconds...")
    time.sleep(2)

    for i in range(iterations):
        clear_screen()
        print(f"Iteration: {i + 1}/{iterations}")
        render_grid(grid)
        game.next_generation()
        time.sleep(0.3)  # Delay between frames

    print("Simulation complete.")

if __name__ == "__main__":
    main()
