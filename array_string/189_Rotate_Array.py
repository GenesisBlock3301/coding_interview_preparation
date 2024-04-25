from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(arr) - 1
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]


s = Solution()
arr = []

print(s.rotate(arr, 3))
print(arr)