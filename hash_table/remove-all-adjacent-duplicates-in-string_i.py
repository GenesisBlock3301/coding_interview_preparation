from typing import List


class Solution:
    def removeDuplicates(self, s: str) -> str:
        result: List = []
        for char in s:
            if result and result[-1] == char:
                result.pop()
            else:
                result.append(char)
        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()
    s = "abbaca"
    print(solution.removeDuplicates(s))