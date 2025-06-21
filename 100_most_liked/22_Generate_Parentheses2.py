class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # only add an open parenthesis when n_open < n
        # only add a close parenthesis when n_closed < n_open
        # valid IIF n_open == n_closed == n

        stack = []  # to store each possible solution
        res = []

        def backtrack(n_open, n_close):
            if n_open == n_close == n:
                res.append("".join(stack))
                return

            if n_open < n:
                stack.append("(")
                backtrack(n_open + 1, n_close)
                stack.pop()

            if n_close < n_open:
                stack.append(")")
                backtrack(n_open, n_close + 1)
                stack.pop()

        backtrack(0, 0)

        return res


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))