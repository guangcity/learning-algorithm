#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 方法一、利用队列的思想，先进先出，不断滑动窗口[i:i+k]
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        win = []
        n = len(nums)

        if nums != []:
            for i in range(n - k + 1):
                win.append(max(nums[i:i + k]))

        return win

# 利用hea实现队列操作，先进先出
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq

        win = []
        hea = []# 注意不能写成：win = hea = []

        n = len(nums)

        hea.append(0)

        for num in nums[0:k - 1]:
            hea.append(num)

        if nums != []:
            for i in range(k - 1, n):
                hea.append(nums[i])
                hea.pop(0)
                win.append(max(hea))

        return win
# 方法三、利用双向队列（效率最高）
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        win = []
        hea = []

        n = len(nums)

        for i in range(k - 1):  # 先建立第一个窗口的前k-1个
            while hea != [] and nums[hea[-1]] < nums[i]:  # 一直比较新数及队尾元素，若队尾较小则出队
                hea.pop()
            hea.append(i)  #新数的索引入队

        if nums != []:
            for i in range(k - 1, n):
                if hea != [] and (i - hea[0]) == k:  # 队列中最大值的索引与新数的索引如果溢出窗口k，则队头出队
                    hea.pop(0)
                while hea != [] and nums[hea[-1]] < nums[i]:
                    hea.pop()
                hea.append(i)
                win.append(nums[hea[0]])    # 队头的索引指示该窗口下的最大值

        return win

# 方法四、利用堆思想，跟方法三雷同

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq   # 需要这个模块建立堆

        win = []
        hea = []

        n = len(nums)

        for i in range(n):
            while hea != [] and (i - hea[0][1]) > k - 1:  # 如果堆顶点对应的索引溢出，删除堆顶点（即删除最大值）
                heapq.heappop(hea)
            heapq.heappush(hea, (-nums[i], i))  #同时将数值和索引输入堆，以便判断堆顶点的索引是否溢出
            if i > k - 2:  # 在堆至少为窗口大小时，才开始输出最大值
                win.append(-hea[0][0])

        return win