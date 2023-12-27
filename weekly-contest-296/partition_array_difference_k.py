# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

def partition_find_difference(nums, k):
    nums.sort()
    n = len(nums)
    ans = 1
    start = nums[0]
    i = 1
    while i < n:
        if nums[i] - start > k:
            ans += 1
            start = nums[i]
        i += 1
    return ans


nums = [3, 6, 1, 2, 5]
k = 2
print(partition_find_difference(nums, k))
