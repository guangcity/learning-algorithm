'''
给定一个排序数组,你需要在原地删除重复出现的元素,使得每个元素只出现一次,返回移除后数组的新长度.

示例：
给定数组　nums=[1,1,2]
函数应该返回新长度２,并且原数组nums的前两个元素被修改为１,2.
你不需要考虑数组中超出新长度后面的元素.
'''

'''
思路：
如果列表中数字为１个,则直接返回该列表长度;
如果列表长度大于１,则需要判断.列表的索引位置为s,当前索引位置的下一位索引为f,
如果当前位置的索引s和下一位置的索引f对应的值不同,则将j位置对应的值更新到s位置,
重新输出的新长度为s+1.
'''
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return len(nums)
        s=0
        for f in range(1,len(nums)):
            if nums[s]!=nums[f]:
                s+=1
                nums[s]=nums[f]
        return s+1