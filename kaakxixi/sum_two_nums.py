"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
"""方法1是使用list查询差值"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            num = target - nums[i]
            if num in nums and nums.index(num) != i:
                return [i,nums.index(num)]


"""方法2是使用dict查询差值"""
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """           
        #创建一个空字典
        dic = {}
        for i in range(len(nums)):
            num = target - nums[i]
            #字典d中存在nums[i]时,hash查找复杂度为1
            if nums[i] in dic:
                return dic[nums[i]],i
            #否则往字典增加键/值对
            else:
                dic[num] = i
        #边往字典增加键/值对，边与nums[i]进行对比