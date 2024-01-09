from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


s = Solution()
nums = [1, 2, 3, 4]
nums = [1,1,1,1,1]
print(s.runningSum(nums))
