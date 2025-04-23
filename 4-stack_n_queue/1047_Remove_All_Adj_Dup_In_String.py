class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = list()
        for item in s:
            if stack and item == stack[-1]:
                stack.pop()
            else:
                stack.append(item)

        return ''.join(stack)


sol = Solution()
print(sol.removeDuplicates(""))