"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is: [ [-1, 0, 1], [-1, -1, 2] ]
"""
"""
解题思路：
1，先将数组排序。
2，排序后，可以按照TwoSum的思路来解题。怎么解呢？可以将num[i]的相反数即-num[i]作为target，然后从i+1到len(num)-1的数组元素中寻找两个数使它们的和为-num[i]就可以了。下标i的范围是从0到len(num)-3。
3，这个过程要注意去重。
4，时间复杂度为O(N^2)。
"""


class Solution(object):
  def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()
    for i in range(0, len(nums)):
      if i > 0 and nums[i] == nums[i - 1]:
        continue
      target = 0 - nums[i]
      start, end = i + 1, len(nums) - 1
      while start < end:
        if nums[start] + nums[end] > target:
          end -= 1
        elif nums[start] + nums[end] < target:
          start += 1
        else:
          res.append((nums[i], nums[start], nums[end]))
          end -= 1
          start += 1
          while start < end and nums[end] == nums[end + 1]:
            end -= 1
          while start < end and nums[start] == nums[start - 1]:
            start += 1
    return res
