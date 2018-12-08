# -*- coding: utf-8 -*-


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] < nums[low]:
                if target < nums[mid] or target >= nums[low]:
                    high = mid
                else:
                    low = mid + 1
            elif nums[mid] > nums[high - 1]:
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else:
                    high = mid
            else:
                if target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid
        return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [8, 1, 2, 3, 4, 5, 6, 7]
    target = 6
    assert solution.search(nums, target) == 6
