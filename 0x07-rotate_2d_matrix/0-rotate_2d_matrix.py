#!/usr/bin/python3
"""
Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.
    """
    n = len(matrix)

    # Iterate through each layer of the matrix
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer

        # Iterate through each element in the layer
        for i in range(first, last):
            # Store the top element
            temp = matrix[first][i]

            # Move left element to top
            matrix[first][i] = matrix[last - i + first][first]

            # Move bottom element to left
            matrix[last - i + first][first] = matrix[last][last - i + first]

            # Move right element to bottom
            matrix[last][last - i + first] = matrix[i][last]

            # Move top element to right
            matrix[i][last] = temp
