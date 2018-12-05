class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1 = self.cal_multipy(nums)
        arr2 = self.cal_multipy(nums[::-1])[::-1]
        for i in range(len(nums)):
            nums[i]=arr1[i]*arr2[i]
        return nums
    def cal_multipy(self, nums):
        t=1
        arr = []
        for i in range(len(nums)):
            if i==0:
                arr.append(1)
            else:
                arr.append(t)
            t *= nums[i]
        return arr



s = Solution()
nums=[]
t = s.productExceptSelf(nums)
print(t)