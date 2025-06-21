class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        d2char = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        curStr = []

        def backtrack(i):
            if len(curStr) == len(digits):
                res.append("".join(curStr))
                return

            for c in d2char[digits[i]]:
                curStr.append(c)
                backtrack(i+1)
                curStr.pop()

        if digits:
            backtrack(0)

        return res


if __name__ == '__main__':
    digits = '23'
    print(Solution().letterCombinations(digits))