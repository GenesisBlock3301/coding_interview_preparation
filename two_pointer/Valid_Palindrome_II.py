# https://leetcode.com/problems/valid-palindrome-ii/
def valid_palindrome(s):
    start, end = 0, len(s) - 1
    left = left_delete(start,end)
    right = right_delete(start,end)
    return left or right

def left_delete(start,end):
    c = 0
    while start <= end:
        if c > 1:
            return False
        if s[start] != s[end]:
            c += 1
            start += 1
        else:
            start += 1
            end -= 1
    return True

def right_delete(start,end):
    c = 0
    while start <= end:
        if c > 1:
            return False
        if s[start] != s[end]:
            c += 1
            end-= 1
        else:
            start += 1
            end -= 1
    return True


# s = "abal"
# s = "abca"
s = "tebbem"
# s = "cbbcc"
print(valid_palindrome(s))