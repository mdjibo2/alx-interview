#!/usr/bin/python3
"""
Calculates the perimeter of the island described in the grid.

Args:
grid (list[list[int]]): A grid representing the island.

Returns:
int: The perimeter of the island.
"""


def island_perimeter(grid):
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                # Check top
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # Check bottom
                if row == len(grid) - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                # Check left
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # Check right
                if col == len(grid[row]) - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
