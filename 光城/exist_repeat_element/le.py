class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_list = []
        for i in nums:
            if i in nums_list:
                return True
            nums_list.append(i)
        return False

s = Solution()
nums = [2,14,18,22,22]
t = s.containsDuplicate(nums)
print(t)