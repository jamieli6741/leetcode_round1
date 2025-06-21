class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        length = 0
        flag = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ' and flag == 0:
                start = i
                flag = 1
            elif s[i] == ' ' and flag == 1:
                length = start - i

            if length != 0:
                break

        return length


sol = Solution()
print(sol.lengthOfLastWord('Hello World'))