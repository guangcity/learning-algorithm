
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        new_list = sorted(nums1)
        return new_list
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
s = Solution()
m=3
n=3
t = s.merge(nums1,m,nums2,n)
print(t)
