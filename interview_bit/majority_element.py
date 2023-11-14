import math


def majorityElement(A):
    majority = math.floor(len(A) / 2)
    dic = dict()
    _max = float('-inf')
    element = None
    for i in A:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
        if _max < dic[i]:
            _max = dic[i]
            element = i
    if _max > majority:
        return element


# A = [3, 1, 2]
A = [ 1, 1, 1, 2, 2 ]
print(majorityElement(A))
