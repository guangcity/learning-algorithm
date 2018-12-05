class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 列表排序，从小到大
        nums.sort()
        # [-4, -1, -1, 0, 1, 2]
        res_list = []
        # 头部循环查找
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                # 最左端
                l = i + 1
                # 最右端
                r = len(nums) - 1
                while l < r:  # 正在查找
                    three_sum = nums[i] + nums[l] + nums[r]
                    if three_sum == 0:
                        res_list.append([nums[i], nums[l], nums[r]])
                        l += 1 # 右移一位
                        r -= 1 # 左移一位
                        while l < r and nums[l] == nums[l - 1]:
                            # 从左往右，相同数值直接跳过
                            l += 1
                        while r > l and nums[r] == nums[r + 1]:
                            # 从右往左，相同数值直接跳过
                            r -= 1
                    elif three_sum > 0:
                        # 大于零，右边数值大，左移
                        r -= 1
                    else:
                        # 小于零，左边数值小，右移
                        l += 1
        return res_list
