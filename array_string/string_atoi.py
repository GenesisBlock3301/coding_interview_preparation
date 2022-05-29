#https://leetcode.com/problems/string-to-integer-atoi/

def string_to_atoi(s):
    result = 0
    n = len(s)
    if n == 0:
        return 0
    s = s.lstrip()
    mul = 1
    start = 0
    if s[0] == '-':
        mul = -1
        start = 1
    elif s[0] == '+':
        start = 1

    for i in s[start:]:
        print(i,start)
        if not (ord(i) >= 48 and ord(i) <= 57):
            return result*mul
        result = (result*10)+(ord(i)-ord("0"))
        min_int_32 = 2 ** 31

        if result*mul <= -min_int_32:
            return -min_int_32
        elif result*mul >= min_int_32-1:
            return min_int_32-1
    return result*mul


print(string_to_atoi("+1"))
