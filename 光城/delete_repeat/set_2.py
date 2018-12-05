class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums_len = len(list(set(nums)))

        i = 0
        for each in sorted(list(set(nums))):
            nums[i] = each
            i += 1
        return nums_len
    # ls = list(set(nums))
    # ls.sort_list()
    # for i in range(nums_len):
    #     nums[i]=ls[i]

    # return nums_len