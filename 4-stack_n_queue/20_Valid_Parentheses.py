from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif not stack or stack[-1] != c:
                return False
            else:
                stack.pop()

        return len(stack) == 0



test_str = "([])"
sol = Solution()
print(sol.isValid(test_str))