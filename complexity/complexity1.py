# log n

from operator import le


arr = [1,2,3,4,5,6,7, 8]
target = 3
mid = (0+len(arr))/2
"""
n = 8
n = 4
n = 2
n = 1
2^3 = 8
log8 = 3
logN = k
2^k = N
"""
a = [1,2,3,4,5]
b = [2,3,4,5]
for i in range(len(a)):
    for j in range(len(b)):
        print(i,j)
# O(a*b)

s = "sifat"
s1 = ""
# O(n*2)
for i in s:
    s1+=i
    """
    s1="s"
    s1="si"
    s1=""
    """