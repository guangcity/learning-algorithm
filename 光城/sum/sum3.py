class Solution:
    def twoSum(self,nums,target):
        len_nums = len(nums)
        for i in range(len_nums):
            one_num = nums[i]
            other_num = target-one_num
            if other_num in nums[:i]:
                other_index = nums.index(other_num)
                return [other_index,i]
        return []

nums = [1,4,6,7]

target = 10
s = Solution()
a = s.twoSum(nums,target)
print(a)
