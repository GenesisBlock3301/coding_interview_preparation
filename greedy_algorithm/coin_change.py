# https://pythonwife.com/greedy-algorithms-in-python/

"""
We are given a number of coins of different denominations and the total amount of money. Find the minimum number of
coins that are needed to make up the given amount.
"""
"""
Implementation of Coin Change Problem
The Coin Change Problem makes use of the Greedy Algorithm in the following manner:

-> Find the biggest coin that is less than the given total amount.
-> Add the coin to the result and subtract it from the total amount to get the pending amount.
-> If the pending amount is zero, print the result.
-> Else, repeat the mentioned steps till the pending amount reduces to zero.
"""
"""
Time and Space Complexity
The time complexity for the Coin Change Problem is O(N) because we iterate through all the elements of the given list of
 coin denominations. The space complexity is O(1) as no additional memory is required."""


def coin_change(arr, total_value):
    arr.sort()
    i = len(arr)-1
    val = total_value
    while True:
        coin = arr[i]
        if val >= coin:
            print(coin)
            val -= coin
        i -= 1
        if val == 0:
            break


coins = [1, 2, 5, 10, 20, 50, 100, 1000]
coin_change(coins, 122)
