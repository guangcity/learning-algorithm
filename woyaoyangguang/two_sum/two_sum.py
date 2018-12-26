'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9

所以返回 [0, 1]
'''

'''思路:
求差值、把差值存进字典里作为键、索引作为值，第一次循环理解：d[7]=0 即字典d={7:0}，表示为索引0需要数组里值为7的元素配对。
在第二次num[1]为7的时候,就返回d={7:0}对应的索引值0,且当前nums数组中７对应的索引值为1,这样即达到所满足的条件.
'''


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        index_dict={}
        for i in range(n):

            x=target-nums[i]
            if nums[i] in index_dict:

                return index_dict[nums[i]],i
            else:
                index_dict[x]=i




a=Solution()
b=a.twoSum(nums=[2,7,11,15],target=9)
print(b)