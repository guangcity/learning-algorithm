# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-10-02 19:07:51
# @Last Modified by:   Liling
# @Last Modified time: 2018-10-02 19:16:24
"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
        	res = nums[i+1:]
        	resnum = target-nums[i]
        	if resnum in res:
        		j = res.index(resnum)
        		return [i,i+j+1]

class Solution():
    def twoSum(self, nums, target):
        hashdict = {}
        for i, item in enumerate(nums):
            if (target - item) in hashdict:
                return (hashdict[target - item], i)
            hashdict[item] = i
        return (-1, -1)
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))