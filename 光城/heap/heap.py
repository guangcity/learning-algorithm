class KthLargest(object):

    def __init__(self, k, nums):
        self.heapList = [0]
        self.currentSize = 0
        self.k = k
        l = nums[:k]
        print(l)
        self.heapList = self.heapify(l)
        print(self.heapList)
        rest = nums[k:]
        print(rest)
        for num in rest:
            if num < self.heapList[1]:
                continue
            self.heapList=self.heappushpop(num)
            print(self.heapList)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        print(len(self.heapList))
        if len(self.heapList)-1 < self.k:
            self.heapList = self.heappush(val)
        elif val > self.heapList[1]:
            self.heapList=self.heappushpop(val)
        return self.heapList[1]

    def updateHeap(self, i):
        while (i * 2) <= self.currentSize:
            if i * 2 + 1 > self.currentSize:
                j =  i * 2
            else:
                if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                    j = i * 2
                else:
                    j = i * 2 + 1
            if self.heapList[i] > self.heapList[j]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[j]
                self.heapList[j] = tmp
            i = j

    def heapify(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.updateHeap(i)
            i = i - 1
        return self.heapList

    def heappushpop(self, val):
        self.heapList.append(val)
        self.currentSize += 1
        print(self.heapList)
        self.heapList.remove(self.heapList[1])
        self.heapList.remove(self.heapList[0])
        self.heapList = self.heapify(self.heapList)
        self.currentSize -= 1
        return self.heapList


    def heappush(self, val):
        self.heapList.append(val)
        self.currentSize += 1
        self.heapList.remove(self.heapList[0])
        self.heapList = self.heapify(self.heapList)
        return self.heapList
# Your KthLargest object will be instantiated and called as such:
k = 3
arr = [4,5,8,2,3,5,10,9]

kthLargest = KthLargest(3,arr)

print(kthLargest.add(4))
