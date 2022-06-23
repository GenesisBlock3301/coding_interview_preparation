# https://leetcode.com/problems/power-of-two/

def powr_two(n):
    for i in range(n):
        if 2**i == n:
            return True
    return False

n = 3
print(powr_two(n))