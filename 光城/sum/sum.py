class Solution:
    def twoSum(self,nums,target):
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(i+1,len_nums):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []


nums = [1,4,6,7]
target = 10
s = Solution()
a = s.twoSum(nums,target)
print(a)
