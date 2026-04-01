import pytest
from benchmark import benchmark_place_random_cells

def test_benchmark_execution():
    """
    Test that the benchmark function runs without errors and returns a non-negative float.
    """
    width, height = 5, 5
    num_cells = 5
    iterations = 2

    result = benchmark_place_random_cells(width, height, num_cells, iterations)

    assert isinstance(result, float)
    assert result >= 0.0
