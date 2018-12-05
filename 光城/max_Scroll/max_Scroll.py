class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_Scroll = []

        nums_len = len(nums)
        for i in range(nums_len):
            if i+k-1 < nums_len:
                max_Scroll.append(max(nums[i:i+k]))
                if i+k==nums_len:
                    break

        return max_Scroll



s = Solution()
res = s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
print(res)

