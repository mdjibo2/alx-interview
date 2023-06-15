#!/usr/bin/python3
"""
Determines the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Calculates the fewest number of coins needed to meet the given total
    """
    if total <= 0:
        return 0

    # Create a memoization table to store the results of previous calculations
    memo = {}

    def minCoinsHelper(target):
        if target in memo:
            return memo[target]

        if target < 0:
            return float('inf')

        if target == 0:
            return 0

        min_coins = float('inf')
        for coin in coins:
            min_coins = min(min_coins, minCoinsHelper(target - coin) + 1)

        memo[target] = min_coins
        return min_coins

    result = minCoinsHelper(total)
    return result if result != float('inf') else -1
