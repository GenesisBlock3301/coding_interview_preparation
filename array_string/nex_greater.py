# https://leetcode.com/problems/next-greater-element-i/

def next_greater(nums1,nums2):
    result = []
    for i in nums1:
        index = nums2.index(i)
        print(index)
        if index+1 <= len(nums2)-1:
            if nums2[index+1] > nums2[index]:
                # max = nums2[index+1]
                result.append(max)
            else:
                max = -1
        else:
            result.append(-1)
    return result

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(next_greater(nums1,nums2))