class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        # return True
        if len(ransomNote) > len(magazine):
            return False

        count_m = [0] * 26
        for c in magazine:
            count_m[ord(c) - ord('a')] += 1

        for c in ransomNote:
            count_m[ord(c) - ord('a')] -= 1
            if count_m[ord(c) - ord('a')] < 0:
                return False

        print(count_m)

        return True

sol = Solution()
print(sol.canConstruct(ransomNote="aa", magazine="aabc"))


