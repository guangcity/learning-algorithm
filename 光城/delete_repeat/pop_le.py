class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = 0

        for i in range(len(nums)):
            if nums[length]==nums[i]:


        length += 1
        return length