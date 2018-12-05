class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums_len = len(list(set(nums)))

        ls = list(set(nums))
        ls.sort()
        for i in range(nums_len):
            nums[i]=ls[i]

        return nums_len