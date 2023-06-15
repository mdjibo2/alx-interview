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

    # Create a list to store the minimum number of coins needed for each value
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if min_coins[i - coin] != float('inf'):
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if min_coins[total] == float('inf'):
        return -1

    return min_coins[total]
