class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # only add an open parenthesis when n_open < n
        # only add a close parenthesis when n_closed < n_open
        # valid IIF n_open == n_closed == n

        res = []

        def backtrack(n_open, n_close, curRes):
            if n_open == n_close == n:
                res.append(curRes)
                return

            if n_open < n:
                backtrack(n_open + 1, n_close, curRes + "(")

            if n_close < n_open:
                backtrack(n_open, n_close + 1, curRes + ")")

        backtrack(0, 0, "")

        return res


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))