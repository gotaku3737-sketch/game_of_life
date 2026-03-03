import time
import os
from game_of_life import Grid, Game

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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
        if starting_cells <= 0 or starting_cells > 40 * 40:
            print("Number of starting cells must be positive and less than or equal to 1600 (40x40).")
            return

    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # Initialize the grid
    grid = Grid(40, 40)
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
