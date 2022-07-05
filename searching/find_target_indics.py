# https://leetcode.com/problems/find-target-indices-after-sorting-array/
class Solution:
    def binary(self,nums, low, high, target, ans):
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                if mid not in ans:
                    ans.append(mid)
                    self.binary(nums, low, mid-1, target, ans)
                    self.binary(nums, mid+1, high, target, ans)
            if nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
    def targetIndices(self, nums, target: int):
        nums.sort()
        ans = []
        l=0
        h = len(nums)-1
        self.binary(nums,l,h,target,ans)
        ans.sort()
        return ans

# less than and equal
def find_target(nums,target):
    less_than = equal = 0
    for i in nums:
        if i < target:
            less_than+=1
        elif target == i:
            equal+=1
    return list(range(less_than,less_than+equal))

nums = [1,2,5,2,3]
target = 2
print(find_target(nums,target))