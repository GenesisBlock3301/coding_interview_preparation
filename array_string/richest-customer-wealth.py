from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = sum(accounts[0])
        for i in range(1, len(accounts)):
            result = max(result, sum(accounts[i]))
        return result


s = Solution()
accounts = [[1, 2, 3], [3, 2, 1]]
accounts = [[1, 5], [7, 3], [3, 5]]
accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
print(s.maximumWealth(accounts))
