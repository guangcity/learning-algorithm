#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        seen = []
        for i, j in enumerate(nums):
            if j == 0:
                print(i)
                b = nums.pop(i)
                seen.append(b)
        nums.extend(seen)
        return nums


#遇到一个问题，比如[0,0,1]这样的数据时，用上面的判断就不会得到有效的效果。
c = Solution()
print(c.moveZeroes([0, 0,1]))
