# https://leetcode.com/contest/weekly-contest-296/problems/replace-elements-in-an-array/

def replace_element(_nums, _operations):
    for i in _operations:
        if i[0] in _nums:
            index = _nums.index(i[0])
            _nums[index] = i[1]
    return _nums


nums = [1, 2, 4, 6]
operations = [[1, 3], [4, 7], [6, 1]]
print(replace_element(nums, operations))
