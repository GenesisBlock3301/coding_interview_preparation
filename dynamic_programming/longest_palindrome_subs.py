# https://leetcode.com/problems/longest-palindromic-substring/ 

def longest_palindrome(_s):
    _s = list(_s)
    if _s == _s[::-1]:
        return "".join(_s)
    n = len(_s)
    palindromes = []
    arr = []
    for i in range(n):
        arr.append(_s[i])
        for k in range(i + 1, n):
            arr.append(_s[k])
            l = "".join(arr)
            if l not in palindromes:
                if l == l[::-1]:
                    palindromes.append(l)
        arr = []
    print(palindromes)

    if palindromes:
        maxList = max(palindromes, key=len)
        return "".join(maxList)
    else:
        return _s[0]


# s = "babad"
# s = "cbbd"
# s = "a"
# s = "ac"

# s = "bacabab"
s = "abadd"

print(longest_palindrome(s))
