class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ptr = 0
        char = list(s)
        while ptr < len(s):
            char = char[:ptr] + char[ptr:ptr + k][::-1] + char[ptr + k:]
            ptr += 2*k

        return ''.join(char)

    # 非常不简便的方法
    # def reverse_unit_strs(self, s, start, end):
    #     s = list(s)
    #     while start < end:
    #         s[start], s[end] = s[end], s[start]
    #         start += 1
    #         end -= 1
    #     return "".join(s)
    #
    # def reverseStr(self, s, k):
    #     """
    #     :type s: str
    #     :type k: int
    #     :rtype: str
    #     """
    #     n_2k, n_remains = divmod(len(s), 2 * k)
    #     if n_2k > 0:
    #         start, end = 0, 2 * k - 1
    #
    #         # 2nk部分
    #         while end < len(s):
    #             left = start
    #             right = start + k - 1
    #             s = self.reverse_unit_strs(s, left, right)
    #             start += 2 * k
    #             end += 2 * k
    #
    #     # 剩下部分
    #     if n_remains < k:
    #         # print(n_2k * 2 * k)
    #         # print(n_2k * 2 * k + n_remains - 1)
    #         s = self.reverse_unit_strs(s, n_2k * 2 * k, n_2k * 2 * k + n_remains - 1)
    #     else:
    #         s = self.reverse_unit_strs(s, n_2k * 2 * k, n_2k * 2 * k + k - 1)
    #
    #     return s




sol = Solution()
print(sol.reverseStr("abcdefghijklmn", 3))
print("cbadefihgjklnm")