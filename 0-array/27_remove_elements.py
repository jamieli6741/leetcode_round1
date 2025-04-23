class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        fastIndex = 0
        slowIndex = 0
        while fastIndex < len(nums):
            if nums[fastIndex] != val:
                nums[slowIndex] = nums[fastIndex]
                slowIndex += 1

            fastIndex += 1
        return slowIndex



sol = Solution()
nums = [3,2]
val = 3

print(sol.removeElement(nums, val))
print(nums)


"""
#### 思路
题目强调“in-place”，即不可创建新数组，因此必须只能修改原数组。
数组的元素在内存地址中是连续的，不能单独删除数组中的某个元素，只能覆盖。这里复现此过程即可。

#提要
暴力法——双重for循环法（一个for循环遍历数组元素 ，第二个for循环更新数组）的时间复杂度太高，更优解法是使用双指针。
双指针法（快慢指针法）： 通过一个快指针和慢指针在一个for循环下完成两个for循环的工作。

#详解
快指针：遍历原数组元素M=nums，看是否可以属于新数组M'（新数组就是不含有目标元素val的数组）
慢指针：指向更新新数组M'下标的位置（用于“框定”不含目标元素的新数组）

在遍历原数组过程中（fast++）：
- 如果当前元素不等于目标元素val的值，把该元素放入新数组（nums[slow]=nums[fast]），慢指针slow值+1；
- 否，则不放入新数组(对原数组nums不执行任何操作），慢指针值slow值不变

遍历完成后，slow值指向的索引值正好为新数组的大小，直接输出slow即可。

#心得
自己解时想的也是一种类似于双指针的算法，想的是遇到等于目标元素的原数组元素时，就从后往前找一个同样不等于目标元素的值（快慢指针面对面朝中间走），把两者swap，但是实现起来过于复杂。
而快慢指针向同一个方向走的解法写起来更简洁。
用库函数一行就能解决，但是底层的原理也需要适当了解（特别是这题还设计数组在内存上的存储方式）。
"""
