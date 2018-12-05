class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        val = 0x7FFFFFFF
        for i in range(length):
            # 重复的不计算
            low = i + 1
            high = length - 1
            while low < high:
                sum = nums[i] + nums[low] + nums[high]
                result = abs(sum - target)
                if result<val:
                    t = sum
                    val=result
                if sum == target:
                    return t
                elif sum < target:
                    low += 1
                elif sum>target:
                    high -= 1
        return t


s = Solution()
nums = [0,2,1,-3]
target = 1
res = s.threeSumClosest(nums,target)
print(res)
a = [1]
d = set(a).__hash__(1)
print("-----------")
print(d)