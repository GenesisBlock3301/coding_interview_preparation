# https://leetcode.com/problems/find-all-anagrams-in-a-string/
from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):

        m, n = len(s), len(p)
        # Convert list of anagram letters to a Counter (hashtable)
        countP = Counter(p)
        ans = []
        window = None

        for i in range(0, m - n + 1):
            if i == 0:
                # Initialize window with beginning of s => length = length of anagram letters
                window = Counter(s[:n])
            else:
                # Move window to right: 1. remove character on the left
                window[s[i - 1]] -= 1
                # 2. add character on the right
                window[s[i + n - 1]] += 1

                # Check if window is anagram (direct comparison of counters does not work with 0 entries)
            if len(window - countP) == 0:
                ans.append(i)


