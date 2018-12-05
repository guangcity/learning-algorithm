class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]*len(nums)
        low=1
        high=1
        for i in range(len(nums)):
            res[i]*=low
            res[len(nums)-i-1]*=high
            low*=nums[i]
            high*=nums[len(nums)-i-1]

        return res


s = Solution()
nums=[1,2,3,4]
t = s.productExceptSelf(nums)
print(t)