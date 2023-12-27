# reverse array in place
def reverse(nums):
    start, end = 0, len(nums) - 1
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    return nums


nums = [1, 2, 3, 4, 5]
print(reverse(nums))
