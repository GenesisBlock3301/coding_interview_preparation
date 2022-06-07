# https://leetcode.com/problems/longest-palindromic-substring/ 

def longest_palindrome(s):
    s = list(s)
    if s == s[::-1]:
        return "".join(s)
    n = len(s)
    palindroms = []
    arr = []
    for i in range(n):
        arr.append(s[i])
        for k in range(i+1,n):
            arr.append(s[k])
            l = "".join(arr)
            if l not in palindroms:
                if l == l[::-1]:
                    palindroms.append(l)
        arr = []
    print(palindroms)

    if palindroms:
        maxList = max(palindroms, key = len)
        return "".join(maxList)
    else:
        return s[0]


# s = "babad"
# s = "cbbd"
# s = "a"
# s = "ac"

# s = "bacabab"
s = "abadd"

print(longest_palindrome(s))