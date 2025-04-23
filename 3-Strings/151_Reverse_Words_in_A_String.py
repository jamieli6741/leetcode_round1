class Solution(object):
    def single_reverse(self, s, start:int, end:int):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # # 简单调库法：空间复杂度O(n)，时间复杂度O(n)
        # # 调库法1：拆分字符串 + 反转列表
        # words = s.split() # split() 产生新列表，空间复杂度O(n)，时间复杂度O(n)
        # return ' '.join(words[::-1])  # words[::-1]产生新列表，join() 产生新字符串，空间复杂度O(2n)；空间复杂度O(n)

        # # 调库法2：反转整个字符串，将字符串拆分为单词，并反转每个单词
        # s = s[::-1]
        # # split()函数能够自动忽略多余的空白字符
        # s = ' '.join(word[::-1] for word in s.split())
        # return s

        # # 将字符串转换为列表后，使用双指针去除空格
        s = list(s)
        result = ""
        fast = 0
        s.reverse()
        while fast < len(s):
            if s[fast] != " ":
                if len(result) != 0:    # 在每个单词开头加一个空格
                    result += " "
                while fast < len(s) and s[fast] != " ":
                    result += s[fast]
                    fast += 1
            else:   # 遇上空格跳过，相当于删除了空格
                fast += 1

        # 反转每个单词
        fast = slow = 0
        result = list(result)
        while fast <= len(result):  # 注意这里有等号，因为对于最后一个单词，fast要取到总长度后面一位才能反转
            if fast == len(result) or result[fast] == " ":
                self.single_reverse(result, slow, fast - 1)
                slow = fast + 1
                fast += 1
            else:
                fast += 1

        return "".join(result)







if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords(' Hello  world '))