class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = 0
        for each_num in nums:
            if each_num != nums[length]:
                length += 1
                nums[length] = each_num

        length += 1
        return length