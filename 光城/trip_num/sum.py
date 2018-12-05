class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        print(sorted(nums))
        s_list = []
        length = len(nums)

        for i in range(length):
            if i==0 or nums[i] > nums[i - 1]:
                low = i+1
                high = length - 1
                while low < high:
                    s = nums[i] + nums[low] + nums[high]
                    if s==0:
                        s_list.append([nums[i],nums[low],nums[high]])
                        low+=1
                        high-=1
                        while low < high and nums[low] == nums[low - 1]:
                            low += 1
                        while low < high and nums[high] == nums[high + 1]:
                            high -= 1
                    elif s<0:
                        low+=1
                    elif s>0:
                        high-=1
        return s_list

s = Solution()
nums = [0,0,0,0]
s_list = s.threeSum(nums)
print(s_list)