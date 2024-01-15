from typing import List


class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num > 0:
            if num % 2 == 0:
                num = num // 2
                step += 1
            else:
                num -= 1
                step += 1
        return step


s = Solution()
num = 14
num = 8
num = 123
print(s.numberOfSteps(num))
