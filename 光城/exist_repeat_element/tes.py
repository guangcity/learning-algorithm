class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                return True
            nums_dict[nums[i]] = 1
        return False



s = Solution()
nums = [2,14,18,22,22]
t = s.containsDuplicate(nums)
print(t)