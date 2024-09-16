#!/usr/bin/python3
"""A function to determine the fewest number of coins needed """


def makeChange(coins, total):
    """This function will take a list of coins and calculate how much change is required
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for i in coin:
            while(total >= i):
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1
