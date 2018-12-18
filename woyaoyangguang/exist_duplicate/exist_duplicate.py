#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
给定一个整数数组,判断是否存在重复元素.
如果任何值在数组中出现至少两次,函数返回true.如果数组中每个元素不同,则返回false.

示例 1:
输入: [1,2,3,1]
输出: true
示例 2:
输入: [1,2,3,4]
输出: false
'''

'''
思路:
设定两个集合,通过循环数组判断元素是否在集合中，如果不在seen,将集合添加到seen集合中,
如果在将元素,放入到另一集合duplicated中,这个集合中的元素都是数组中重复的元素，然后
对其做一个判断，如果不为空,返回True,如果为空,返回False.
'''
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen=set()
        duplicated=set()
        for x in nums:
            if x not in seen:
                seen.add(x)
            else:
                duplicated.add(x)
        if duplicated:
            return True
        else:
            return False



a=Solution()
print(a.containsDuplicate([1,2,3,4]))
