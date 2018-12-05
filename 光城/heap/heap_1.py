class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            if i * 2 + 1 > self.currentSize:
                mc =  i * 2
            else:
                if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                    mc = i * 2
                else:
                    mc = i * 2 + 1
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc



    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def heapify(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
        print("heapify")
        print(self.heapList)

    def heappushpop(self,val):
        self.heapList.append(val)
        self.currentSize+=1
        self.heapify(self.heapList[1:])
        print(self.heapList)
        self.heapList.remove(self.heapList[1])
        self.currentSize-=1
        print(self.heapList)
        print(self.currentSize)

    def heappush(self,val):
        self.heapList.append(val)
        self.currentSize+=1
        self.heapify(self.heapList[1:])
        print(self.heapList)
        print(self.currentSize)
bh = BinHeap()
bh.heapify([9,5,6,2,3])
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())


