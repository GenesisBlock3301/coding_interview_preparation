# https://leetcode.com/problems/jump-game-ii/

def jump(nums, memo, index=0):
    if index == len(nums) - 1:
        return 0
    result = 1001
    for i in range(1, nums[index]):
        if index + i < len(nums):
            result = min(result, 1+jump(nums, memo, index+i))
            print(result)
    memo[index] = result
    return result


arr = [2, 3, 1, 1, 4]
val = jump(arr, [0]*(len(arr)-1),0)
print(val)
