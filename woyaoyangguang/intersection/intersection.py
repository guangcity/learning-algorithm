#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
给定两个数组，编写一个函数来计算它们的交集。
示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
'''



'''
思路：
遍历nums1中的元素，判断nums1中的元素是否在nums2中，如果在，将此元素加入到一个新的列表中，
并在nums2中删去这个元素。
'''
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        seen = []
        for i in nums1:
            if i in nums2:
                seen.append(i)
                nums2.remove(i)   #只会移除其中碰到的一个元素

        return seen


a = Solution()
print(a.intersect([1,2,2,2, 1], [2, 2]))
