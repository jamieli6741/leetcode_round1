## 数组
#### [《代码随想录》数组：二分查找](https://programmercarl.com/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE)

#### 思路
- 有序数组且无重复值，使用二分法查找。难点在于迭代过程中边界值的变化。
- 区间的定义就是不变量。target位于边界上时容易出错。

#### 详解
1. 易错点：边界值的处理，当target刚好位于边界时容易出错。
right的初始取值有两种写法：right = len(nums)和len(nums-1)。由于Python的索引从0开始，所以实际索引取不到len(nums)。
无论是用哪种写法，在移动左右边界时，要考虑这样一个问题：原有的边界[left,right]或[left,right)的边界值，是否已经被检查过了。如果还没被检查过，更新左右边界为middle；如果已经被检查过了，根据情况对middle +/- 1。
2. middle值溢出(C++和Java中会发生)：写成middle = left + (right - left) // 2 而不是 (left + right)/2。
3. 自己写时出现的问题：把case分得太细，拖慢运行速度。nums数量为1和2的情况不必单独列出来，while循环left <= right或者left < right已经可以包含。

```Python
class Solution(object):
    def search(self, nums, target):
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
```

```Python
class Solution(object):
    def search(self, nums, target):
        # version 2: [left,right)
        left = 0
        right = len(nums)  # 注意，这里不用再-1了，因为是左闭右开，不把-1取消掉，最右边的值取不到
        while left < right:
            middle = left + (right - left) // 2
            if target > nums[middle]:   # target in the right interval, update left boundary
                left = middle + 1
            elif target < nums[middle]:   # target in the left interval, update right boundary
                right = middle
            else:
                return middle

        return -1
```

#### 心得
1. 注意二分法的使用前提：有序数组，无重复元素。
2. 就算是easy的题也还是要好好写test case。




### [《代码随想录》数组：移除元素](https://notes.kamacoder.com/questions/501948)

#### 思路
题目强调“in-place”，即不可创建新数组，因此必须只能修改原数组。
数组的元素在内存地址中是连续的，不能单独删除数组中的某个元素，只能覆盖。这里复现此过程即可。

#### 提要
暴力法——双重for循环法（一个for循环遍历数组元素 ，第二个for循环更新数组）的时间复杂度太高，更优解法是使用双指针。
双指针法（快慢指针法）： 通过一个快指针和慢指针在一个for循环下完成两个for循环的工作。


#### 详解

快指针：遍历原数组元素M=nums，看是否可以属于新数组M'（新数组就是不含有目标元素val的数组）
慢指针：指向更新新数组M'下标的位置（用于“框定”不含目标元素的新数组）

在遍历原数组过程中（fast++）：
- 如果当前元素不等于目标元素val的值，把该元素放入新数组（nums[slow]=nums[fast]），慢指针slow值+1；
- 否，则不放入新数组(对原数组nums不执行任何操作），慢指针值slow值不变

遍历完成后，slow值指向的索引值正好为新数组的大小，直接输出slow即可。

```Python
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
```


#### 心得
- 自己解时想的也是一种类似于双指针的算法，想的是遇到等于目标元素的原数组元素时，就从后往前找一个同样不等于目标元素的值（快慢指针面对面朝中间走），把两者swap，但是实现起来过于复杂。而快慢指针向同一个方向走的解法写起来更简洁。
- 用库函数一行就能解决，但是底层的原理也需要适当了解（特别是这题还设计数组在内存上的存储方式）。


### [《代码随想录》数组：有序数组的平方](https://notes.kamacoder.com/questions/501949)
#### 思路
还是双指针的解题思路，巧妙利用原数组为有序数组，最大值在两端这一特性。

#### 提要
双指针一前一后指向数组的两端，一一对比平方值，把较大的数填入新数组最后一个非空位置。

#### 详解
```Python
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
```

#### 心得
最开始自己想的时候只关注到了复杂度，想到快速排序的实现上去了，没有这个解法更简洁。
双指针还要进一步熟悉，老是想不起来用。


### [《代码随想录》数组：长度最小的子数组](https://notes.kamacoder.com/questions/501950)
#### 思路
使用滑动窗口确定和大于target的最小连续数组。

#### 提要
要点在于如何使用一个for循环完成不断搜索区间的过程。
避免暴力解的方法：for循环滑动窗口的终止位置，根据当前窗口确定如何移动起始位置。

#### 详解
窗口的起始位置如何移动：如果当前窗口的值大于等于s了，窗口就要向前移动了（也就是该缩小了）。
窗口的结束位置如何移动：窗口的结束位置就是遍历数组的指针，也就是for循环里的索引。
```Python
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        sum = 0
        subLength = float('inf')	# 最短子数组长度初始化为最大长度
        for right in range(len(nums)):	# 遍历数组
            sum += nums[right]  # 这里是right，新加入滑动窗口的元素位置
            while sum >= target:	# 注意使用while，以不断进行搜索
                subLength = min(subLength, right-left+1)	# 更新最小数组长度
                sum -= nums[left]   # 起始位置向右滑动一位
                left += 1
        
        return subLength if subLength != float('inf') else 0	# 注意没有最小数组的情况
```

#### 心得
暴力解比较容易想到，双重for循环分别遍历起始位置。这里的滑动窗口解法可以看成对暴力解的简化，根据条件减少了第二层for循环的次数。每个元素在滑动窗后进来操作一次，出去操作一次，每个元素都是被操作两次，时间复杂度由暴力解的O(n^2)变为O(2n)。


### [《代码随想录》数组：螺旋矩阵II](https://notes.kamacoder.com/questions/501951)
#### 思路
螺旋排列其实就是大圈套小圈，顺时针一圈圈向中心填充。没什么更精妙的算法，主要是得处理好边界，参照“循环不变量”的思路，制定一个不变的规则处理每条边(每画一条边都要坚持一致的左闭右开，或者左开右闭的原则)。

#### 提要
每次画圈开始需要确定的值：画圈起始位置[start_x, start_y]，每条边结束位置n-offset。offset和当前圈数loop相关，loop=n//2。
另外，需要考虑n为奇数的情况，此时需要单独填充最中心位置的数值。

#### 详解
```Python
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [[0 for _ in range(n)] for _ in range(n)]
        start_x, start_y = 0, 0
        loop = n // 2
        count = 1
        for offset in range(1, loop+1):
            for y in range(start_y, n - offset):
                nums[start_x][y] = count
                count += 1

            for x in range(start_x, n - offset):
                nums[x][n - offset] = count
                count += 1

            for y in range(n - offset, start_y, -1):
                nums[n - offset][y] = count
                count += 1

            for x in range(n - offset, start_x, -1):
                nums[x][start_y] = count
                count += 1

            start_x += 1
            start_y += 1

        if n % 2 == 1:
            nums[loop][loop] = count

        return nums
```

#### 心得
大致思路能想到，但是具体实现时边界处理得还是有问题。没想到用offset控制每个圆圈的边界，只想到了每次边界索引递减，直到n//2。另外，大循环的终止条件想得也不够好，想的是count到n^2停止，这样远没有通过loop数控制简洁易实现。

## 链表
### [《代码随想录》链表：移除链表元素](https://notes.kamacoder.com/questions/501956)
#### 思路
前置知识点：https://programmercarl.com/%E9%93%BE%E8%A1%A8%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html

移除链表中节点其实就是改变指针指向节点。需要注意，移除头节点的情况要单独处理。

#### 提要
![image.png](http://cdn.notes.kamacoder.com/f19dc86e-8288-4353-8c21-8e2b080d8bee.png)
移除头节点的两种方法：
- 直接使用原来的链表来进行删除操作。
- 设置一个虚拟头结点在进行删除操作。

#### 详解

```Python
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode(next=head)
        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy_head.next
```


### [《代码随想录》链表：设计链表](https://notes.kamacoder.com/questions/501957)
#### 思路
这题不考察算法，根据链表的特性来写就好。注意边界。

#### 提要
链表索引开始于0。采用在头部添加虚拟节点的方法，需要格外注意索引。

#### 详解

```Python
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):
    def __init__(self): # 设置虚拟节点，初始化size值
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        current_node = self.dummy_head.next # 从实际上的第一个节点开始（索引=1）
        for i in range(index):  # 结束时实际的索引为1+index，正好为需要取名义上的第index个节点（因为索引0被dummy_head占了）
            current_node = current_node.next

        return current_node.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        current_node = self.dummy_head
        while current_node.next:    # 直接用是否后面还有节点判断是否到了末端
            current_node = current_node.next

        current_node.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return

        current_node = self.dummy_head  # 从实际索引为0的dummy_head开始
        for i in range(index):  # 添加索引的位置为实际上的index-1，就是题意要求的，加在index前
            current_node = current_node.next
        new_node = ListNode(val, current_node.next)
        current_node.next = new_node
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return

        current_node = self.dummy_head
        for i in range(index):
            current_node = current_node.next

        current_node.next = current_node.next.next
        self.size -= 1
```


### [《代码随想录》链表：翻转链表](https://notes.kamacoder.com/questions/501958)
#### 思路
翻转链表就是改变指针指向。

首先定义一个cur指针，指向头结点，再定义一个pre指针，初始化为null。
然后就要开始反转了，首先要把 cur->next 节点用tmp指针保存一下，也就是保存一下这个节点。
为什么要保存一下这个节点呢，因为接下来要改变 cur->next 的指向了，将cur->next 指向pre ，此时已经反转了第一个节点了。
接下来，就是循环走如下代码逻辑了，继续移动pre和cur指针。
最后，cur 指针已经指向了null，循环结束，链表也反转完毕了。 此时我们return pre指针就可以了，pre指针就指向了新的头结点。
reference: https://notes.kamacoder.com/questions/501958

采用双指针法更清晰：

```Python
# 双指针法
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pre = None
        current = head
        while current:  # 直到原链表的最后一个节点的next，就是NULL
            tmp = current.next
            current.next = pre
            pre = current
            current = tmp
        
        return pre
```
另外也可以用递归法，原理其实一样的，就是写法不同。
```Python
# 递归法
class Solution:
    def reverseList(self, head):
        return self.reverse(head, None)

    def reverse(self, cur, pre):
        if cur == None:
            return pre
        temp = cur.next
        cur.next = pre
        return self.reverse(temp, cur)
```


