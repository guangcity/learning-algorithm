class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import sys
        sys.setrecursionlimit(100000)  # 这里设置为十万
        return self.zheban(nums, target, 0, len(nums) - 1)

    def zheban(self, nums, target, low, high):
        if high < low:
            return -1
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[low]:
            if nums[mid] >= target and target >= nums[low]:
                return self.zheban(nums, target, low, mid - 1)
            else:
                return self.zheban(nums, target, mid + 1, high)
        else:
            if nums[mid] <= target and target <= nums[high]:
                return self.zheban(nums, target, mid + 1, high)
            else:
                return self.zheban(nums, target, low, mid - 1)