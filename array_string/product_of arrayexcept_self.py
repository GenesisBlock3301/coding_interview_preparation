# https://leetcode.com/problems/product-of-array-except-self/
import math


def product_of_array(nums):
    pass


nums = [1, 2, 3, 4]
# nums = [-1,1,0,-3,3]
# nums = [0,0]
print(math.prod(nums[0:1] + nums[1 + 1:], start=1))
print(product_of_array(nums))
