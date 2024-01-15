# https://leetcode.com/problems/word-break/
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.can_break(s, wordDict, {})

    def can_break(self, s: str, wordDict: List[str], dp) -> bool:
        if not s:
            return True
        if s not in dp:
            for word in wordDict:
                is_can_break = False
                if s.startswith(word):
                    if len(word) == len(s):
                        is_can_break = True
                        break
                    else:
                        is_can_break = self.can_break(s[len(word):], wordDict, dp)
                        if is_can_break:
                            break
            dp[s] = is_can_break
        return dp[s]

# Example usage
solution = Solution()
# s = "leetcode"
# wordDict = ["leet", "code"]

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(solution.wordBreak(s, wordDict))
