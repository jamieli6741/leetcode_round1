from collections import deque
class MonotonicQueue:
    def __init__(self):
        self.queue = deque()
    def pop(self, val):
        if self.queue and val == self.queue[0]:
            self.queue.popleft()
    def push(self, val):
        while self.queue and val > self.queue[-1]:
            self.queue.pop()
        self.queue.append(val)

    def front(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = list()
        queue = MonotonicQueue()
        for i in range(k):
            queue.push(nums[i])
        result.append(queue.front())

        for i in range(k, len(nums)):
            queue.pop(nums[i-k])
            queue.push(nums[i])
            result.append(queue.front())

        return result

if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    sol = Solution()
    print(sol.maxSlidingWindow(nums, k))
