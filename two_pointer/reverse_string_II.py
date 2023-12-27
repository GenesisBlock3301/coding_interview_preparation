# https://leetcode.com/problems/reverse-string-ii/

def reverse_II(s, k):
    if k > len(s):
        return s
    if len(s) == k:
        return s[::-1]
    start, end = 0, len(s) - 1
    s = list(s)
    while start < end:
        st, en = start, (start + k) - 1
        print("==", st, en, len(s[st:en]))
        while st < en:
            print("before", s[st], s[en])
            s[st], s[en] = s[en], s[st]
            print("after", s[st], s[en])
            st += 1
            en -= 1
        print(start, start + k)
        start += 2 * k
    return "".join(s)


# s = "abcdefg"
# k = 8
# s = "abcd"
# k = 2
# s = "abcdef"
# k = 3
s = "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"
k = 39
print(reverse_II(s, k))
