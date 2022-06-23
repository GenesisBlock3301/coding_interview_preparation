
""" 
time O(n)
space O(n)
"""


def majority_element(nums):
    dic = dict()
    majority = 0
    n = len(nums)
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
        if dic[i] > (n//2):
            majority = i
    return majority


def majority2(nums):
    count_table = [0]*(10**9)
    for i in nums:
        count_table[i]+=1
    
    return max(count_table)

    # nums = [2,2,1,1,1,2,2]
nums = [3, 2, 3]
# print(majority_element(nums))
print(majority2(nums))
