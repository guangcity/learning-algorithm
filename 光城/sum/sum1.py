class Solution:
    def twoSum(self,nums,target):
        len_nums = len(nums)
        for i in range(len_nums):
            one_num = nums[i]
            other_num = target-one_num
            if other_num in nums[i+1:]:
                other_index = nums[i+1:].index(other_num)+i+1
                return [i,other_index]
        return []

nums = [1,4,6,7]

target = 10
s = Solution()
a = s.twoSum(nums,target)
print(a)
