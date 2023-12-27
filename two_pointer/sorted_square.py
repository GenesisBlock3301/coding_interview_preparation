# Given an integer array sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.


def square_sorted(nums):
    n = len(nums)
    start, end = 0, n-1
    res = [0]*n
    index = n-1
    while end >= 0 and start >= 0:
        if abs(nums[start]) > abs(nums[end]):
            res[index] = nums[start]*nums[start]
            start += 1
        else:
            res[index] = nums[end]*nums[end]
            end -= 1
        index -= 1
    return res


nums = [-10, 1, 2, 3, 4, 5]
print(square_sorted(nums))
