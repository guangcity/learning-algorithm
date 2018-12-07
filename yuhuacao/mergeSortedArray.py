"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note: 
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""
"""
主要思路：设置遍历数组1和数组2的指针i=m-1，j=n-1，设置更新数组1的指针k=m+n-1。遍历数组，如果数组1中的值大于数组2，或者数组2遍历到头了，并且数组1没有到头，则更新数组1，nums1[k] = nums1[i–]，否则nums1[k] = nums2[j–]。当k小于0时遍历结束。
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i=m-1
        j=n-1
        k=m+n-1
        while k>=0:
            if (j<0 or nums1[i]>nums2[j]) and i>=0:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
