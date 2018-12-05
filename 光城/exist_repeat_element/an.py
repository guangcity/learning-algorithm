class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        data_dict = {}
        for k, v in enumerate(nums):
            print("-----")
            print(k,v)
            print(nums.count(v))
            data_dict[nums.count(v)]=k

        for i in data_dict:
            if i >1:
                return True
        return False



s = Solution()
nums = [2,14,18,22,22]
t = s.containsDuplicate(nums)
print(t)