class Solution:
    def twoSum(self,nums,target):
        l = len(nums)
        t = {nums[i]: i for i in range(l)}
        for a in range(l):
            one_unm = nums[a]
            other_one = target - one_unm
            if other_one in t and a != t[other_one]:
                return [a, t[other_one]]

nums = [1,4,6,7]

target = 10
s = Solution()
a = s.twoSum(nums,target)
print(a)
