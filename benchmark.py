import time
import random
from game_of_life import Grid

def benchmark_place_random_cells(width, height, num_cells, iterations=100):
    grid = Grid(width, height)

    start_time = time.perf_counter()
    for _ in range(iterations):
        grid.place_random_cells(num_cells)
    end_time = time.perf_counter()

    avg_time = (end_time - start_time) / iterations
    print(f"Grid {width}x{height}, {num_cells} cells: Average time over {iterations} iterations: {avg_time:.6f} seconds")
    return avg_time

if __name__ == "__main__":
    # Test with a few different scenarios
    print("Benchmarking current implementation...")
    # Sparse grid
    benchmark_place_random_cells(100, 100, 100)
    # Medium grid
    benchmark_place_random_cells(100, 100, 5000)
    # Dense grid (where the while loop should struggle most)
    benchmark_place_random_cells(100, 100, 9900)
