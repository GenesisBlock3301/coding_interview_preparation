# https://pythonwife.com/greedy-algorithms-in-python/
"""
Fractional Knapsack Problem: We are given a set of items, each with a weight and a value. Determine the number of each
item to include in a collection such that the total weight is less than or equal to a given limit and the total value is
as large as possible.
"""
"""Implementation of Fractional Knapsack Problem
The Fractional Knapsack Problem makes use of the Greedy Algorithm in the following manner:

-> Calculate the density for each item. It is defined as the ration of value to weight of the given item.
-> Sort the items based on this ratio.
-> Select items with the highest ratio sequentially until the space in the collection allows.
-> Add the remaining items as much as possible.
"""


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

    def __str__(self):
        return f"{self.weight - self.value - self.ratio}"


def fractional_knapsack(items, total_limit):
    items.sort(key=lambda x: x.ratio, reverse=True)
    used_capacity = 0
    total_value = 0
    for i in items:
        if used_capacity + i.weight <= total_limit:
            used_capacity += i.weight
            total_value += i.value
        else:
            unused_capacity = total_limit - used_capacity
            value = unused_capacity*i.ratio
            used_capacity += unused_capacity
            total_value += value
        if used_capacity == total_limit:
            break
    return total_value


item1 = Item(20, 100)
item2 = Item(30, 120)
item3 = Item(10, 60)
cList = [item1, item2, item3]

print(fractional_knapsack(cList, 50))
