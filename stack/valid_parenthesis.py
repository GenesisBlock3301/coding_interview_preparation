# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        stack = []
        for i in s:
            if i in opening:
                stack.append(i)
            elif i in closing:
                pos = closing.index(i)
                if len(stack) > 0 and opening[pos] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
