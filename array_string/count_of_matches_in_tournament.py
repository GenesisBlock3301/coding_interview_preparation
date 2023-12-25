class Solution:
    def numberOfMatches(self, n: int) -> int:
        s = 0
        while n > 1:
            if n % 2 != 0:
                m = (n - 1) // 2
                s += m
                n = (n-1)//2 + 1
            else:
                m = n//2
                s += m
                n = (n-1)//2 + 1
        return s


s = Solution()
n = 7
print(s.numberOfMatches(n))