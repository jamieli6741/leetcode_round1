import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 统计元素出现频率
        map_ = {}
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1

        # 用固定大小为k的小顶堆，扫描所有频率的数值
        pri_queue = []
        for key, freq in map_.items():
            heapq.heappush(pri_queue, (freq, key))
            if len(pri_queue) > k:  # 如果堆的大小大于k，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_queue)

        # 找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        result = [0]*k
        for i in range(k-1,-1,-1):
            result[i] = heapq.heappop(pri_queue)[1]  # 把key加入result而不是freq

        return result