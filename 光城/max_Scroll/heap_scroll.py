import heapq as hp
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums: return []
        out = []
        heap = []
        for i in range(k):
            hp.heappush(heap,(-nums[i],i)) #Heap sorts only according to the cell's first element which is the value of number
        out.append(-heap[0][0])
        print(heap)
        for i in range(k,len(nums)):
            hp.heappush(heap,(-nums[i],i))
            print(heap)

            out.append(-heap[0][0])

        return out



s = Solution()
res = s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
print(res)


