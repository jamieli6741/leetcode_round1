class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # version 1: [left,right]
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if target > nums[middle]:   # target in the right interval, update left boundary
                left = middle + 1
            elif target < nums[middle]:   # target in the left interval, update right boundary
                right = middle - 1
            else:
                return middle

        return -1

        # # version 2: [left,right)
        # left = 0
        # right = len(nums)  # 注意，这里不用再-1了，因为是左闭右开，不把-1取消掉，最右边的值取不到
        # while left < right:
        #     middle = left + (right - left) // 2
        #     if target > nums[middle]:   # target in the right interval, update left boundary
        #         left = middle + 1
        #     elif target < nums[middle]:   # target in the left interval, update right boundary
        #         right = middle
        #     else:
        #         return middle
        #
        # return -1


# test case
sol = Solution()
nums = [-1,2,5,34] #[-1] #[2,34]
target = 4 #-1 #5
print(sol.search(nums, target))

# Notes
"""
思路：
有序数组且无重复值，使用二分法查找。难点在于迭代过程中边界值的变化。

提要：
区间的定义就是不变量。target位于边界上时容易出错。

详解：
1. 易错点：边界值的处理，当target刚好位于边界时容易出错。
right的初始取值有两种写法：right = len(nums)和len(nums-1)。由于Python的索引从0开始，所以实际索引取不到len(nums)。
无论是用哪种写法，在移动左右边界时，要考虑这样一个问题：原有的边界[left,right]或[left,right)的边界值，是否已经被检查过了。
如果还没被检查过，更新左右边界为middle；如果已经被检查过了，根据情况对middle +/- 1。
2. middle值溢出(C++和Java中会发生)：写成middle = left + (right - left) // 2 而不是 (left + right)/2。
3. 自己写时出现的问题：把case分得太细，拖慢运行速度。nums数量为1和2的情况不必单独列出来，while循环left <= right或者left < right已经可以包含。

心得：
1. 注意二分法的使用前提：有序数组，无重复元素。
2. 就算是easy的题也还是要好好写test case。
"""