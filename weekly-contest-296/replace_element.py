# https://leetcode.com/contest/weekly-contest-296/problems/replace-elements-in-an-array/

def replace_element(nums,operations):
    for i in operations:
        if i[0] in nums:
            index = nums.index(i[0])
            nums[index] = i[1]
    return nums

nums = [1,2,4,6]
operations = [[1,3],[4,7],[6,1]]
print(replace_element(nums,operations))