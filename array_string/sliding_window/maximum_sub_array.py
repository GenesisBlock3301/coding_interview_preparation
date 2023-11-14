# https://leetcode.com/problems/maximum-subarray/

def max_subarray_sum(nums):
    max_sum = nums[0]
    result = [nums[0]]
    start = 0
    end = 1
    current_sum = nums[0]
    for end in range(1, len(nums)):
        # If current value greater than subarray sum
        # That means there is another greatest subarray
        if nums[end] > current_sum + nums[end]:
            current_sum = nums[end]
            start = end
        else:
            # If current value not greater than subarray sum
            # That means we need to extend current subarray
            current_sum += nums[end]

        if current_sum > max_sum:
            max_sum = current_sum
            result = nums[start:end+1]
    return result

# nums = [5, 4, -1, 7, 8]
# nums = [1,-1]
# nums =  [-2,1,-3,-55, 4444]
nums = [-2,-1]
print("Largest subarray sum:", max_subarray_sum(nums))
