class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [-1] * len(nums)
        left, right, current = 0, len(nums) - 1, len(nums) - 1
        while current >= 0:
            if nums[right] ** 2 >= nums[left] ** 2:
                result[current] = nums[right] * nums[right]
                right -= 1
            else:
                result[current] = nums[left] * nums[left]
                left += 1
            current -= 1

        return result


nums = [-4,-1,0,3,10]
sol = Solution()
print(sol.sortedSquares(nums))

# 还是双指针的解题思路，巧妙利用原数组为有序数组，最大值在两端这一特性。
# 只注意到复杂度，想到快速排序的实现上去了，这个解法更简洁。