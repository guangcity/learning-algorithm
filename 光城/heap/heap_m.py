
import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.heap = nums[:k]
        print(self.heap)
        heapq.heapify(self.heap)
        print(self.heap)
        rest = nums[k:]
        print(rest)
        for num in rest:
            if num < self.heap[0]:
                continue
            heapq.heappushpop(self.heap, num)
        print(self.heap)
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        print(self.heap)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
k = 3
arr = [4,5,8,10]

kthLargest = KthLargest(3,arr)

print(kthLargest.add(3))
