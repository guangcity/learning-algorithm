#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
输入：[0,1,0,3,12]
输出：[1,3,12,0,0]
'''


'''
思路：
用nums.count(0)得出数组中零的个数,然后将数组中的零去掉，
然后将０的个数，补足到数组新的数组中。
'''

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n=nums.count(0)
        for i in range(n):
            nums.remove(0)
        nums.extend([0]*n)

