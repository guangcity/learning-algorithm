## 01.TwoSum两数之和

### 题目描述

给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

### 思路

第一种思路是比较直观也是复杂度比较高的解法，遍历列表中的每个元素，在剩下的元素中找有没有使得两个数之和为目标值的数。

```python
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
        	res = nums[i+1:]
        	resnum = target-nums[i]
        	if resnum in res:
        		j = res.index(resnum)
        		return [i,i+j+1]
```

这种解法的时间复杂度是$O(n^2)$，因为需要遍历，遍历的同时还要在剩下的元素中查找。空间复杂度是O(1)。



第二种思路是用哈希，也是要遍历列表，但是遍历的同时将当前值及其index存入哈希字典，并且在哈希字典中查找有没有想要的值。

```python
class Solution():
    def twoSum(self, nums, target):
        hashdict = {}
        for i, item in enumerate(nums):
            if (target - item) in hashdict:
                return (hashdict[target - item], i)
            hashdict[item] = i
        return (-1, -1)
```

这种解法的时间复杂度是O(n)，空间复杂度是O(n)。

