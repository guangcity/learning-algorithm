
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        high = m+n-1
        m=m-1
        n=n-1
        while m>=0 and n>=0:
            if nums1[m]>nums2[n]:
                nums1[high] = nums1[m]
                high-=1
                m-=1
            else:
                nums1[high] = nums2[n]
                high -= 1
                n -= 1

        while n>=0:
            nums1[high] = nums2[n]
            high -= 1
            n -= 1
        return nums1
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
s = Solution()
m=3
n=3
t = s.merge(nums1,m,nums2,n)
print(t)
