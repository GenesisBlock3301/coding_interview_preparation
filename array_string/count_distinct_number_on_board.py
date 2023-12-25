# https://leetcode.com/problems/count-distinct-numbers-on-board/

class Solution:
    def distinctIntegers(self, n: int) -> int:
        if n == 1 or n == 2:
            return 1
        i = 3
        x = n
        while x <= n:
            if x % i == 1:
                return i
            i += 1


if __name__ == '__main__':
    s = Solution()
    n = 5
    print(s.distinctIntegers(5))
