# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-10-02 19:20:50
# @Last Modified by:   Liling
# @Last Modified time: 2018-12-12 20:39:03
"""
给定一个字符串，找出不含有重复字符的最长子串的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 无重复字符的最长子串是 "abc"，其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 无重复字符的最长子串是 "b"，其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 无重复字符的最长子串是 "wke"，其长度为 3。
     请注意，答案必须是一个子串，"pwke" 是一个子序列 而不是子串
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or len(s) <= 0:
            return 0
        # charDict存储每个字符以及字符出现的最后的位置, res为当前最长的子串长度, st当前无重复子串的最左边字符的位置
        charDict, res, st = {}, 0, 0
        for i, ch in enumerate(s):
            if ch not in charDict or charDict[ch] < st:
                res = max(res, i - st + 1)
            else:
                st = charDict[ch] + 1
            charDict[ch] = i
        return res

s = Solution()
print(s.lengthOfLongestSubstring('pwwkew'))