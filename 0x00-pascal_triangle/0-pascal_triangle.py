#!/usr/bin/python3
"""
Pascal Triangle function in python
"""


def pascal_triangle(n):
    """Return a list of lists of integers representing the Pascal's triangle of n.

    Args:
        n (int): The number of rows to include in the Pascal's triangle.

    Returns:
        list: A list of lists, where each inner list contains the integers for a row
            in the Pascal's triangle.

    Raises:
        None.

    Examples:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        >>> pascal_triangle(0)
        []
        >>> pascal_triangle(-3)
        []

    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle

