class Solution:
    def twoSum(self,nums,target):
        nums_hash = {}

        for index,number in enumerate(nums):
            one_num = nums[index]
            other_num = target-one_num
            if other_num in nums_hash:
                return [nums_hash[other_num],index]
            nums_hash[number] = index
        return []

nums = [3,3,6,7]
target = 10
s = Solution()
a = s.twoSum(nums,target)
print(a)
