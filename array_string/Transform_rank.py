# https://leetcode.com/problems/rank-transform-of-an-array/


def transform_rank(nums):
    dic = dict()
    c = 0
    n = len(nums)
    for i in sorted(nums):
        if i not in dic:
            c += 1
            dic[i] = c

    # val = []

    for i in range(len(nums)):
        if nums[i] in dic:
            nums[i] = dic[nums[i]]
            # val.append(dic[i])
    return nums


# nums = [40,10,20,30]
nums = [100, 100, 100]
print(transform_rank(nums))
